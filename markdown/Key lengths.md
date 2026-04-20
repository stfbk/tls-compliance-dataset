| Use                                               | Algorithms      | Minimum key length (bits) | ('NIST', '')          | ('NIST', 'Use up to year') | ('BSI', '') [^1]            | ('BSI', 'Use up to year') | ('ANSSI', '')     | ('ANSSI', 'Use up to year') | ('ACN', 'Recommended') | ('ACN', 'Compatibility') | ('ENISA', '')     | ('ENISA','use up to') | ('MOZILLA (+AGID)', 'Modern') [^2] | ('MOZILLA (+AGID)', 'Intermediate') | ('MOZILLA (+AGID)', 'Old') |
| ------------------------------------------------- | --------------- | ------------------------- | --------------------- | -------------------------- | --------------------------- | ------------------------- | ----------------- | --------------------------- | :--------------------- | :----------------------- | :---------------- | :-------------------- | ---------------------------------- | ----------------------------------- | -------------------------- |
| Signature keys for certificates and key agreement | ECDSA           | 224                       | recommended           | YEAR 2030                  | \<Not mentioned\>     [^3]  |                           | \<Not mentioned\> |                             | \<Not mentioned\>      | \<Not mentioned\>        | <Not mentioned>   |                       | \<Not mentioned\>                  | \<Not mentioned\>                   | \<Not mentioned\>          |
|                                                   | ECDSA           | 256                       | recommended           | YEAR 2031+                 | recommended                 | YEAR 2032+                | recommended       | YEAR 2030                   | recommended            | recommended              | recommended [^17] |                       | \<Not mentioned\>                  | \<Not mentioned\>                   | \<Not mentioned\>          |
|                                                   | EdDSA           | 256 [^4]                  | \<Not mentioned\>     |                            | \<Not mentioned\>           |                           | recommended       |                             | recommended            | \<Not mentioned\>        | <Not mentioned>   |                       | \<Not mentioned\>                  | \<Not mentioned\>                   | \<Not mentioned\>          |
|                                                   | EdDSA           | 456 [^5]                  | \<Not mentioned\>     |                            | \<Not mentioned\>           |                           | recommended       |                             | recommended            | \<Not mentioned\>        | <Not mentioned>   |                       | \<Not mentioned\>                  | \<Not mentioned\>                   | \<Not mentioned\>          |
|                                                   | DSA        [^6] | 2048                      | recommended     [^7]  | YEAR 2030                  | must not            [^9]    |                           | \<Not mentioned\> |                             | \<Not mentioned\>      | \<Not mentioned\>        | not recommended   | YEAR 2025             | \<Not mentioned\>                  | \<Not mentioned\>                   | \<Not mentioned\>          |
|                                                   | DSA             | 3072                      | recommended     [^10] | YEAR 2031+                 | recommended         [^11]   | YEAR 2029                 | \<Not mentioned\> |                             | \<Not mentioned\>      | \<Not mentioned\>        | recommended       |                       | \<Not mentioned\>                  | \<Not mentioned\>                   | \<Not mentioned\>          |
|                                                   | RSA             | 2048                      | recommended           | YEAR 2030                  | must not            [^12]   |                           | recommended       | YEAR 2030                   | optional               | recommended              | not recommended   | YEAR 2025             | \<Not mentioned\>                  | recommended                         | \<Not mentioned\>          |
|                                                   | RSA             | 3072                      | recommended           | YEAR 2031+                 | recommended         [^13]   | YEAR 2032+                | \<Not mentioned\> |                             | optional               | recommended              | recommended       |                       | \<Not mentioned\>                  | \<Not mentioned\>                   | \<Not mentioned\>          |
|                                                   | RSA             | 1024                      | \<Not mentioned\>     |                            | \<Not mentioned\>           |                           | \<Not mentioned\> |                             | must not               | must not                 | <Not mentioned>   |                       | \<Not mentioned\>                  | \<Not mentioned\>                   | recommended                |
| Static and ephemeral Diffie-Hellman keys          | ECDH            | 224                       | \<Not mentioned\>     |                            | \<Not mentioned\>     [^14] |                           | \<Not mentioned\> |                             | <Not mentioned>        | <Not mentioned>          | <Not mentioned>   |                       | \<Not mentioned\>                  | \<Not mentioned\>                   | \<Not mentioned\>          |
|                                                   | ECDH            | 256                       | \<Not mentioned\>     |                            | recommended                 | YEAR 2032+                | \<Not mentioned\> |                             | recommended            | recommended              | recommended [^18] |                       | \<Not mentioned\>                  | \<Not mentioned\>                   | \<Not mentioned\>          |
|                                                   | DH              | 1024                      | \<Not mentioned\>     |                            | \<Not mentioned\>           |                           | \<Not mentioned\> |                             | must not               | must not                 | <Not mentioned>   |                       | not recommended                    | not recommended                     | recommended                |
|                                                   | DH              | 2048                      | \<Not mentioned\>     |                            | must not            [^15]   |                           | optional          |                             | optional               | recommended              | not recommended   | YEAR 2025             | not recommended                    | recommended                         | not recommended            |
|                                                   | DH              | 3072                      | \<Not mentioned\>     |                            | recommended         [^16]   | YEAR 2032+                | optional          |                             | optional               | recommended              | recommended       |                       | not recommended                    | not recommended                     | not recommended            |
|                                                   | DH              | 4096                      | \<Not mentioned\>     |                            | \<Not mentioned\>           |                           | optional          |                             | optional               | recommended              | recomended        |                       | not recommended                    | not recommended                     | not recommended            |
|                                                   | DH              | 6144                      | \<Not mentioned\>     |                            | \<Not mentioned\>           |                           | optional          |                             | optional               | recommended              | recomended        |                       | not recommended                    | not recommended                     | not recommended            |
|                                                   | DH              | 8192                      | \<Not mentioned\>     |                            | \<Not mentioned\>           |                           | optional          |                             | optional               | recommended              | recomended        |                       | not recommended                    | not recommended                     | not recommended            |

[^1]: TR-02102-2 section 3.6.1
    and
    TR-02102-1, version 2023-1, Table 3.1
[^2]: Being a list of recommendations:

    not mentioned --> not recommended
[^3]: Not mentioned starting from version 2023-01 of TR-02102-2
[^4]: Key size for Ed25519
[^5]: Key size for Ed448
[^6]: DSA is the algorithm, DSS is its standardization made by NIST

    Source: FIPS 186-5
[^7]: NIST refers to DSA as DSS
[^8]: "A key length of ≥ 3000 bits will be mandatory from 2023 for cryptographic DLIES and DSA implementations that are to be compliant with this Technical Guideline."

    Change mandated by BSI-TR-02102-1, version 2023-1, Table 3.1
[^9]: "A key length of ≥ 3000 bits will be mandatory from 2023 for cryptographic DLIES and DSA implementations that are to be compliant with this Technical Guideline."

    Change mandated by BSI-TR-02102-1, version 2023-1, Table 3.1
[^10]: NIST refers to DSA as DSS, This is translated as recommended since the must is limited to the context of the DSA keys
[^11]: "A key length of ≥ 3000 bits will be mandatory from 2023 for cryptographic DLIES and DSA implementations that are to be compliant with this Technical Guideline."

    Change mandated by BSI-TR-02102-1, version 2023-1, Table 3.1.
[^12]: "Transitionally, also the use of RSA-keys with a length of ≥ 2000 bits will remain compliant until the end of 2023; from 2024 onwards, an RSA key length of ≥ 3000 bits will be mandatory."

    Change mandated by BSI-TR-02102-1, version 2023-1, Table 3.1
[^13]: "Transitionally, also the use of RSA-keys with a length of ≥ 2000 bits will remain compliant until the end of 2023; from 2024 onwards, an RSA key length of ≥ 3000 bits will be mandatory."

    Change mandated by BSI-TR-02102-1, version 2023-1, Table 3.1.


​    
​    
    This is translated as recommended since the must is limited to the context of the RSA keys
[^14]: Not mentioned starting from version 2023-01 of TR-02102-2
[^15]: "A key length of ≥ 3000 bits will be mandatory from 2023 for cryptographic DLIES and DSA implementations that are to be compliant with this Technical Guideline."

    Change mandated by BSI-TR-02102-1, version 2023-1, Table 3.1
[^16]: "A key length of ≥ 3000 bits will be mandatory from 2023 for cryptographic DLIES and DSA implementations that are to be compliant with this Technical Guideline."

    Change mandated by BSI-TR-02102-1, version 2023-1, Table 3.1.


​    
    This is translated as recommended since the must is limited to the context of the DH keys

[^17]: Derived from the Groups table
[^18]: Derived from the Groups table
