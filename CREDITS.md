This file lists the main contributions. For the full list of contributions, please refer to the commit log.

* Alessandro Tomasi ([@wry-run](https://www.github.com/wry-run))
  - initial data extraction and structuring from
    - ANSSI - Recommandations de sécurité relatives à TLS `v1.2`
    - BSI - `TR-02102-2` and `TR-03116-4`
    - NIST - `SP 800-52 Rev. 2`

* Salvatore Manfredi ([@NetBender](https://www.github.com/NetBender))
  - data review, formatting and translation
  - data extraction from
    - ACN - `v1.0` and related updates
    - AgID - `AgID-RACCSECTLS-01`
    - Mozilla - Recommended configurations `v5.6` and related updates
    - NIST - `SP 800-131A Rev. 2`

* Riccardo Germenia ([@Odinmylord](https://www.github.com/Odinmylord))
  - data review, format standardization
  - addition of contextual notes to store references and reasonings
  - data extraction from
    - ACN - `v1.0` and related updates
    - CNSA - `1.0` and `2.0`
    - ENISA -  `v2.0`
    - Mozilla - Recommended configurations `v5.7` and related updates
    - NIST - `SP 800-131A Rev. 2` and `SP 800-186`
  - dataset structuring
    - database schema definition (Prisma)
    - reproducible scheme generation
    - reproducible SQLite database generation