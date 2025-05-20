| Use                                               | Algorithms      | Minimum key length (bits)      | ('NIST', '')          | ('NIST', 'Use up to year') | ('BSI', '')             [^1] | ('BSI', 'Use up to year')       | ('BSI (from 1/1/2024)', '') [^2] | ('BSI (from 1/1/2024)', 'Use up to year') | ('ANSSI', '')     | ('ANSSI', 'Use up to year') | ('ACN', 'Recommended') | ('ACN', 'Compatibility') | ('ENISA', '')     | ('ENISA','use up to') | ('MOZILLA (+AGID)', 'Modern') [^3] | ('MOZILLA (+AGID)', 'Intermediate') | ('MOZILLA (+AGID)', 'Old') |
| ------------------------------------------------- | --------------- | ------------------------------ | --------------------- | -------------------------- | ---------------------------- | ------------------------------- | -------------------------------- | ----------------------------------------- | ----------------- | --------------------------- | :--------------------- | :----------------------- | :---------------- | :-------------------- | ---------------------------------- | ----------------------------------- | -------------------------- |
| Signature keys for certificates and key agreement | ECDSA           | 224                            | recommended           | YEAR 2030                  | \<Not mentioned\> [^4]       |                                 | \<Not mentioned\>     [^5]       |                                           | \<Not mentioned\> |                             | \<Not mentioned\>      | \<Not mentioned\>        | <Not mentioned>   |                       | \<Not mentioned\>                  | \<Not mentioned\>                   | \<Not mentioned\>          |
|                                                   | ECDSA           | 256                            | recommended           | YEAR 2031+                 | recommended                  | YEAR 2029+                      | recommended                      | YEAR 2029+                                | recommended       | YEAR 2030                   | recommended            | recommended              | recommended [^24] |                       | \<Not mentioned\>                  | \<Not mentioned\>                   | \<Not mentioned\>          |
|                                                   | EdDSA      [^6] | -1                        [^7] | \<Not mentioned\>     |                            | \<Not mentioned\>            |                                 | \<Not mentioned\>                |                                           | \<Not mentioned\> |                             | \<Not mentioned\>      | \<Not mentioned\>        | <Not mentioned>   |                       | \<Not mentioned\>                  | \<Not mentioned\>                   | \<Not mentioned\>          |
|                                                   | DSA        [^8] | 2048                           | recommended     [^9]  | YEAR 2030                  | must not        [^10]        |                                 | must not            [^11]        |                                           | \<Not mentioned\> |                             | \<Not mentioned\>      | \<Not mentioned\>        | not recommended   | YEAR 2025             | \<Not mentioned\>                  | \<Not mentioned\>                   | \<Not mentioned\>          |
|                                                   | DSA             | 3076                           | recommended     [^12] | YEAR 2031+                 | recommended     [^13]        | YEAR 2029+                      | recommended         [^14]        | YEAR 2029+                                | \<Not mentioned\> |                             | \<Not mentioned\>      | \<Not mentioned\>        | recommended       |                       | \<Not mentioned\>                  | \<Not mentioned\>                   | \<Not mentioned\>          |
|                                                   | RSA             | 2048                           | recommended           | YEAR 2030                  | recommended                  | YEAR 2023                 [^15] | must not            [^16]        |                                           | recommended       | YEAR 2030                   | optional               | recommended              | not recommended   | YEAR 2025             | \<Not mentioned\>                  | recommended                         | \<Not mentioned\>          |
|                                                   | RSA             | 3076                           | recommended           | YEAR 2031+                 | recommended                  | YEAR 2029+                      | recommended         [^17]        | YEAR 2029+                                | \<Not mentioned\> |                             | optional               | recommended              | recommended       |                       | \<Not mentioned\>                  | \<Not mentioned\>                   | \<Not mentioned\>          |
|                                                   | RSA             | 1024                           | \<Not mentioned\>     |                            | \<Not mentioned\>            |                                 | \<Not mentioned\>                |                                           | \<Not mentioned\> |                             | must not               | must not                 | <Not mentioned>   |                       | \<Not mentioned\>                  | \<Not mentioned\>                   | recommended                |
| Static and ephemeral Diffie-Hellman keys          | ECDH            | 224                            | \<Not mentioned\>     |                            | \<Not mentioned\> [^18]      |                                 | \<Not mentioned\>     [^19]      |                                           | \<Not mentioned\> |                             | recommended            | recommended              | <Not mentioned>   |                       | \<Not mentioned\>                  | \<Not mentioned\>                   | \<Not mentioned\>          |
|                                                   | ECDH            | 256                            | \<Not mentioned\>     |                            | recommended                  | YEAR 2029+                      | recommended                      | YEAR 2029+                                | \<Not mentioned\> |                             | recommended            | recommended              | recommended [^25] |                       | \<Not mentioned\>                  | \<Not mentioned\>                   | \<Not mentioned\>          |
|                                                   | DH              | 1024                           | \<Not mentioned\>     |                            | \<Not mentioned\>            |                                 | \<Not mentioned\>                |                                           | \<Not mentioned\> |                             | must not               | must not                 | <Not mentioned>   |                       | \<Not mentioned\>                  | \<Not mentioned\>                   | recommended                |
|                                                   | DH              | 2048                           | \<Not mentioned\>     |                            | must not        [^20]        |                                 | must not            [^21]        |                                           | \<Not mentioned\> |                             | recommended            | recommended              | not recommended   | YEAR 2025             | \<Not mentioned\>                  | recommended                         | \<Not mentioned\>          |
|                                                   | DH              | 3072                           | \<Not mentioned\>     |                            | recommended     [^22]        | YEAR 2029+                      | recommended         [^23]        | YEAR 2029+                                | \<Not mentioned\> |                             | recommended            | recommended              | recommended       |                       | \<Not mentioned\>                  | \<Not mentioned\>                   | \<Not mentioned\>          |

[^1]: TR-02102-2 section 3.6.1
[^2]: TR-02102-2 section 3.6.1
    and
    TR-02102-1, version 2023-1, Table 3.1
[^3]: Being a list of recommendations:

    not mentioned --> not recommended
[^4]: Not mentioned starting from version 2023-01 of TR-02102-2
[^5]: Not mentioned starting from version 2023-01 of TR-02102-2
[^6]: not mentioned in any target guideline.
    First mentioned in SP800-131
[^7]: non specificato
[^8]: DSA is the algorithm, DSS is its standardization made by NIST

    Source: FIPS 186-5
[^9]: NIST refers to DSA as DSS
[^10]: "A key length of ≥ 3000 bits will be mandatory from 2023 for cryptographic DLIES and DSA implementations that are to be compliant with this Technical Guideline."

    Change mandated by BSI-TR-02102-1, version 2023-1, Table 3.1
[^11]: "A key length of ≥ 3000 bits will be mandatory from 2023 for cryptographic DLIES and DSA implementations that are to be compliant with this Technical Guideline."

    Change mandated by BSI-TR-02102-1, version 2023-1, Table 3.1
[^12]: NIST refers to DSA as DSS
[^13]: "A key length of ≥ 3000 bits will be mandatory from 2023 for cryptographic DLIES and DSA implementations that are to be compliant with this Technical Guideline."

    Change mandated by BSI-TR-02102-1, version 2023-1, Table 3.1
    
    
    
    This is translated as recommended since the must is limited to the context of the DSA keys
[^14]: "A key length of ≥ 3000 bits will be mandatory from 2023 for cryptographic DLIES and DSA implementations that are to be compliant with this Technical Guideline."

    Change mandated by BSI-TR-02102-1, version 2023-1, Table 3.1.
    
    
    This is translated as recommended since the must is limited to the context of the DSA keys
[^15]: As an interim arrangement, the usage of RSA keys of length at least 2000 bits will however
    remain compliant with this Technical Guideline through 2023.
[^16]: "Transitionally, also the use of RSA-keys with a length of ≥ 2000 bits will remain compliant until the end of 2023; from 2024 onwards, an RSA key length of ≥ 3000 bits will be mandatory."

    Change mandated by BSI-TR-02102-1, version 2023-1, Table 3.1
[^17]: "Transitionally, also the use of RSA-keys with a length of ≥ 2000 bits will remain compliant until the end of 2023; from 2024 onwards, an RSA key length of ≥ 3000 bits will be mandatory."

    Change mandated by BSI-TR-02102-1, version 2023-1, Table 3.1.
    
    
    
    This is translated as recommended since the must is limited to the context of the RSA keys
[^18]: Not mentioned starting from version 2023-01 of TR-02102-2
[^19]: Not mentioned starting from version 2023-01 of TR-02102-2
[^20]: "A key length of ≥ 3000 bits will be mandatory from 2023 for cryptographic DLIES and DSA implementations that are to be compliant with this Technical Guideline."

    Change mandated by BSI-TR-02102-1, version 2023-1, Table 3.1
[^21]: "A key length of ≥ 3000 bits will be mandatory from 2023 for cryptographic DLIES and DSA implementations that are to be compliant with this Technical Guideline."

    Change mandated by BSI-TR-02102-1, version 2023-1, Table 3.1
[^22]: "A key length of ≥ 3000 bits will be mandatory from 2023 for cryptographic DLIES and DSA implementations that are to be compliant with this Technical Guideline."

    Change mandated by BSI-TR-02102-1, version 2023-1, Table 3.1
    
    
    This is translated as recommended since the must is limited to the context of the DH keys
[^23]: "A key length of ≥ 3000 bits will be mandatory from 2023 for cryptographic DLIES and DSA implementations that are to be compliant with this Technical Guideline."

    Change mandated by BSI-TR-02102-1, version 2023-1, Table 3.1.
    
    
    This is translated as recommended since the must is limited to the context of the DH keys

[^24]: Derived from the Groups table
[^25]: Derived from the Groups table
