# TLS Compliance Dataset

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/) [![DOI](https://zenodo.org/badge/813592465.svg)](https://doi.org/10.5281/zenodo.15011610)

The content of this repository is the result of the gathering, translation, standardization and structuring of a set of technical requirements extracted from five cybersecurity agencies' guidelines.

The examined guidelines are:
- **AgID** [AgID-RACCSECTLS-01](https://cert-agid.gov.it/wp-content/uploads/2020/11/AgID-RACCSECTLS-01.pdf)
- **ANSSI** [v1.2](https://cyber.gouv.fr/sites/default/files/2017/07/anssi-guide-recommandations_de_securite_relatives_a_tls-v1.2.pdf)
- **BSI** [TR-02102-2](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/TechGuidelines/TG02102/BSI-TR-02102-2.html) and [TR-03116-4](https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeRichtlinien/TR03116/BSI-TR-03116-4.html)
- **Mozilla** [v5.7](https://wiki.mozilla.org/Security/Server_Side_TLS)
- **NIST** [SP 800-52 Rev. 2](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-52r2.pdf) (and related documents)


The result of this process is a dataset that can be audited, inspected and peer reviewed.

#### Glossary
- Configurable element - each element whose availability can be set by the system administrator (e.g., specific protocol versions);
- Guideline - a document issued by a national cybersecurity agency that contains technical requirement for various configurable elements;
- Level - the requirement level that every guideline assigns to each configurable element;
- Profile - a use case defined by a guideline (e.g., customer-facing and government-facing service);
- Variant - subset of elements that can have alternative configurations levels (e.g., prioritization of ephemeral keys use);
- Condition - an additional requirement that restricts the use of a configurable element (e.g., "use *element* up to year 2030").

## Dataset Structure
The dataset is composed of multiple `.md` files that are used to store different sets of configurable elements. Each file contains a table with the following structure:
| Configurable Element | (Guideline<sub>1</sub>, Profile<sub>1</sub>) | (Guideline<sub>1</sub>, Profile<sub>1</sub>)   | ... | (Guideline<sub>n</sub>, Profile<sub>n</sub>) | (Guideline<sub>n</sub>, Profile<sub>n</sub>)   |
| -------------------- | --------------------- | ----------------------- | --- | --------------------- | ----------------------- |
| Element<sub>1</sub>  | Level<sub>1,1</sub>   | Condition<sub>1,1</sub> | ... | Level<sub>1,n</sub>   | Condition<sub>1,n</sub> |
| Element<sub>2</sub>  | Level<sub>2,1</sub>   | Condition<sub>2,1</sub> | ... | Level<sub>2,n</sub>   | Condition<sub>2,n</sub> |
| ...                  | ...                   | ...                     | ... | ...                   | ...                     |
| Element<sub>n</sub>  | Level<sub>n,1</sub>   | Condition<sub>n,1</sub> | ... | Level<sub>n,n</sub>   | Condition<sub>n,n</sub> |


#### Additional Information
For additional information on how to add a new guideline or a new table to the dataset, please refer to the [Standard Compliance Module](<docs/Standard_Compliance_Module.md>).

### Configurable Elements

Each file lists the requirements level of

- Certificates-related
	- [Certificate.md](<markdown/Certificate.md>): common fields;
	- [Certificate Extensions.md](<markdown/Certificate Extensions.md>): specific extensions;
	- [Certificate Signature.md](<markdown/Certificate Signature.md>): algorithms that can be used to sign a certificate;
- [Cipher Suites.md](<markdown/Cipher Suites.md>): cipher suites;
- [Hash Algorithms.md](<markdown/Hash Algorithms.md>): the hash algorithms that can be used together with the respective [signatures](<markdown/Signature Algorithms.md>);
- [Key Lengths.md](<markdown/Key Lengths.md>): the key lengths that can be used for both key exchange and signature algorithms;
- [Misc.md](<markdown/Misc.md>): other configurable elements that do not fall into a specific category (e.g., vulnerability-specific mitigations);
- [Protocol.md](<markdown/Protocol.md>): SSL and TLS versions;
- [Signature Algorithms.md](<markdown/Signature Algorithms.md>): the signature algorithms that can be used for forward secrecy;
- [TLS Extensions.md](<markdown/TLS extensions.md>): the TLS extensions that can be used during a secure transmission.

## Reproducibility
To enable reproducibility of the dataset, the repository also contains a set of scripts that can be used to generate a SQLite database that maps the dataset.

- `schema_creator.py`: reads the dataset and by using [Prisma Client Python](https://prisma-client-py.readthedocs.io/en/stable/) creates an empty SQLite database with the tables needed to store the dataset. The database will be stored in a file called `requirements.db` (in the root directory of the repository);
- `database_filler.py`: reads the dataset and fills all the tables of `requirements.db` with the data contained in the dataset.

## How to contribute
Please refer to the [Wiki](https://github.com/stfbk/tls-compliance-dataset/wiki) page.


## Related Projects

This dataset is the result of a study aimed to design a methodology to assess the compliance level of new and existing webservers. More detail about the methodology and the process behind its creation can be found in the paper *[Automating Compliance for Improving TLS Security Postures: An Assessment of Public Administration Endpoints](https://www.scitepress.org/Link.aspx?doi=10.5220/0012764700003767)*:

```BibTex
@conference{secrypt24,
	author={Riccardo Germenia. and Salvatore Manfredi. and Matteo Rizzi. and Giada Sciarretta. and Alessandro Tomasi. and Silvio Ranise.},
	title={Automating Compliance for Improving TLS Security Postures: An Assessment of Public Administration Endpoints},
	booktitle={Proceedings of the 21st International Conference on Security and Cryptography - SECRYPT},
	year={2024},
	pages={450-458},
	publisher={SciTePress},
	organization={INSTICC},
	doi={10.5220/0012764700003767},
	isbn={978-989-758-709-2},
	issn={2184-7711},
}
```

The content of this dataset is an integral part of [TLSAssistant](https://github.com/stfbk/tlsassistant), an open-source modular framework capable of identifying a wide range of TLS vulnerabilities and assessing compliance with multiple guidelines. Its actionable report can assist the user in correctly and easily fixing their configurations.
