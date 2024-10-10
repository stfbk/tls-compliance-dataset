import io
import zipfile
from pyexcel_ods3 import save_data
import odf
from odf import style
import odf.element
from odf.element import Element
from odf.namespaces import nsdict
from odf.opendocument import load as odf_load
from odf.table import Table
from utils.configs import converters
from utils.filler_utils import read_dataframes

styles = {
    "must": "#afd095",
    "must not": "#ffa6a6",
    "recommended": "#b4c7dc",
    "not recommended": "#ffffa6",
}


def _escape_complete(data, entities=None):
    """ Escape &, ", <, and > in a string of data.

        You can escape other strings of data by passing a dictionary as
        the optional entities parameter.  The keys and values must all be
        strings; each key will be replaced with its corresponding value.
    """
    if entities is None:
        entities = {}
    data = data.replace("&", "&amp;")
    data = data.replace("<", "&lt;")
    data = data.replace(">", "&gt;")
    data = data.replace('"', "&quot;")
    data = data.replace("'", "&apos;")
    for chars, entity in entities.items():
        data = data.replace(chars, entity)
    return data

# the escape function in the library is not complete, so we need to replace it
odf.element._escape = _escape_complete

CALCEXTNS = 'urn:org:documentfoundation:names:experimental:calc:xmlns:calcext:1.0'
CALCEXT_NAME = 'calcext'
nsdict[CALCEXTNS] = CALCEXT_NAME

if __name__ == "__main__":
    dataframe = read_dataframes({"converters": converters, "dtype": str})
    ods_data = {}
    for name, df in dataframe.items():
        df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
        df = df.to_dict()
        sheet_data = []

        # Extract headers from the keys of inner dictionaries
        headers = [key[0] for key in df.keys()]
        headers2 = [key[1] for key in df.keys()]
        sheet_data.append(headers)
        sheet_data.append(headers2)

        # Gather rows based on the first element of the tuples
        for index in range(max(len(inner_dict) for inner_dict in df.values())):
            row = [df[key].get(index, "") for key in df.keys()]
            row = [x if str(x) != "nan" else "" for x in row]
            sheet_data.append(row)

        ods_data[name] = sheet_data
    save_data("output_clean.ods", ods_data)

    # save the data in memory
    content = io.BytesIO()
    save_data(content, ods_data)

    root: odf.opendocument.OpenDocument = odf_load(content)
    for style_name, style_color in styles.items():
        new_style = style.Style(
            name=style_name, family="table-cell", parentstylename="Default")
        bg_color = style.TableCellProperties()
        bg_color.setAttribute("backgroundcolor", style_color)
        new_style.addElement(bg_color)

        root.styles.addElement(new_style)

    for sheet in root.spreadsheet.getElementsByType(Table):
        # this is the element containing the conditional formattings
        conditional_formattings = Element(
            qname=(CALCEXTNS, "conditional-formats"))
        for style_name in styles:
            sheet_name = sheet.getAttribute('name')
            if " " in sheet_name:
                sheet_name = "'"+sheet_name+"'"
            base_cell_address = f"{sheet_name}.B3"
            target_range_address = f"{sheet_name}.B3:{sheet_name}.IV65536"
            # this is a single conditional formatting
            conditional_formatting = Element(
                qname=(CALCEXTNS, "conditional-format"))
            conditional_formatting.setAttrNS(
                CALCEXTNS, "target-range-address", target_range_address)
            # prepare the condition's element
            condition = Element(qname=(CALCEXTNS, "condition"))
            condition.setAttrNS(CALCEXTNS, "apply-style-name", style_name)
            condition.setAttrNS(CALCEXTNS, "value", f'="{style_name}"')
            condition.setAttrNS(
                CALCEXTNS, "base-cell-address", base_cell_address)
            # add the condition to the conditional formatting
            conditional_formatting.appendChild(condition)
            # add the conditional formatting to the conditional formattings
            conditional_formattings.appendChild(conditional_formatting)

        sheet.appendChild(conditional_formattings)


    output_buffer = io.BytesIO()
    root.save(output_buffer)
    archive = zipfile.ZipFile(output_buffer, "r")
    archive_final = zipfile.ZipFile("requirements.ods", "w")
    added = set()
    for file in archive.infolist():
        if file.filename in added:
            continue
        added.add(file.filename)
        content = archive.read(file)
        if file.filename in ["content.xml", "meta.xml", "styles.xml"]:
            if file.filename == "content.xml":
                content = content.replace(b"<table:table-column />", b"")
                content = content.replace(b"office:value-type=\"string\"",
                    b"office:value-type=\"string\" calcext:value-type=\"string\"")
            content = content.replace(b"'", b"\"")
            archive_final.writestr(file, content)

        elif file.filename == "META-INF/manifest.xml":
            content = content.split(b"><")
            content.pop(-2)
            content.pop(-2)
            content = b"><".join(content)
            content = content.replace(b"'", b"\"")
            archive_final.writestr(file, content)
        elif file.filename == "mimetype":
            archive_final.writestr(file, content,
                                compress_type=zipfile.ZIP_STORED)
        else:
            archive_final.writestr(file, content)
    archive_final.close()
