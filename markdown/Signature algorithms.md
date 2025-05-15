 | SignatureScheme [^9]              | IANA         | TLS version limit | ('NIST', '')            [^1] | ('NIST', 'from') | ('BSI', 'client/server signatures ') [^2] | ('BSI', 'use up to') | ('ANSSI', '')       [^3] | ('ANSSI', 'conditions') | ('ACN', 'Recommended') | ('ACN', 'Compatibility') | ('MOZILLA (+AgID)', 'Modern') | ('MOZILLA (+AgID)', 'Intermediate') | ('MOZILLA (+AgID)', 'Old') |
 | :-------------------------------- | :----------- | ----------------: | :--------------------------- | :--------------- | :---------------------------------------- | :------------------- | :----------------------- | ----------------------: | :--------------------- | :----------------------- | :---------------------------- | :---------------------------------- | :------------------------- |
 | rsa_pkcs1_sha1                    | 0x0201       |                   | must not                     |                  | \<Not mentioned\>                         |                      | must not                 |                         | must not               | must not                 | \<Not mentioned\>             | \<Not mentioned\>                   | \<Not mentioned\>          |
 | rsa_pkcs1_sha224                  | 0x0301 [^4]  |                   | must not                     | [^5]             | \<Not mentioned\>                         |                      | must not                 |                         | must not               | must not                 | \<Not mentioned\>             | \<Not mentioned\>                   | \<Not mentioned\>          |
 | rsa_pkcs1_sha256                  | 0x0401       |               1.2 | must not                     | [^6]             | \<Not mentioned\>                         |                      | optional                 |                         | must not               | optional                 | \<Not mentioned\>             | \<Not mentioned\>                   | \<Not mentioned\>          |
 | rsa_pkcs1_sha384                  | 0x0501       |               1.2 | must not                     | [^7]             | \<Not mentioned\>                         |                      | optional                 |                         | must not               | optional                 | \<Not mentioned\>             | \<Not mentioned\>                   | \<Not mentioned\>          |
 | rsa_pkcs1_sha512                  | 0x0601       |               1.2 | must not                     | [^8]             | \<Not mentioned\>                         |                      | optional                 |                         | must not               | optional                 | \<Not mentioned\>             | \<Not mentioned\>                   | \<Not mentioned\>          |
 | rsa_pkcs1_sha256                  | 0x0401       |               1.3 | must not                     | [^10]            | \<Not mentioned\>                         |                      | must not                 |                         | must not               | must not                 | \<Not mentioned\>             | \<Not mentioned\>                   | \<Not mentioned\>          |
 | rsa_pkcs1_sha384                  | 0x0501       |               1.3 | must not                     | [^11]            | \<Not mentioned\>                         |                      | must not                 |                         | must not               | must not                 | \<Not mentioned\>             | \<Not mentioned\>                   | \<Not mentioned\>          |
 | rsa_pkcs1_sha512                  | 0x0601       |               1.3 | must not                     | [^12]            | \<Not mentioned\>                         |                      | must not                 |                         | must not               | must not                 | \<Not mentioned\>             | \<Not mentioned\>                   | \<Not mentioned\>          |
 | rsa_pss_rsae_sha256               | 0x0804 [^13] |                   | recommended                  | [^14]            | recommended                               | YEAR 2031+           | recommended              |                         | optional               | recommended              | \<Not mentioned\>             | \<Not mentioned\>                   | \<Not mentioned\>          |
 | rsa_pss_rsae_sha384               | 0x0805 [^15] |                   | recommended                  | [^16]            | recommended                               | YEAR 2031+           | recommended              |                         | optional               | recommended              | \<Not mentioned\>             | \<Not mentioned\>                   | \<Not mentioned\>          |
 | rsa_pss_rsae_sha512               | 0x0806 [^17] |                   | recommended                  | [^18]            | recommended                               | YEAR 2031+           | recommended              |                         | optional               | recommended              | \<Not mentioned\>             | \<Not mentioned\>                   | \<Not mentioned\>          |
 | ed25519                           | 0x0807       |                   | \<Not mentioned\>            | [^19]            | \<Not mentioned\>                         |                      | recommended              |                         | recommended            | \<Not mentioned\>        | \<Not mentioned\>             | \<Not mentioned\>                   | \<Not mentioned\>          |
 | ed448                             | 0x0808       |                   | \<Not mentioned\>            | [^20]            | \<Not mentioned\>                         |                      | recommended              |                         | recommended            | \<Not mentioned\>        | \<Not mentioned\>             | \<Not mentioned\>                   | \<Not mentioned\>          |
 | rsa_pss_pss_sha256                | 0x0809 [^21] |                   | recommended                  | [^22]            | recommended                               | YEAR 2031+           | recommended              |                         | optional               | recommended              | \<Not mentioned\>             | \<Not mentioned\>                   | \<Not mentioned\>          |
 | rsa_pss_pss_sha384                | 0x080A [^23] |                   | recommended                  | [^24]            | recommended                               | YEAR 2031+           | recommended              |                         | optional               | recommended              | \<Not mentioned\>             | \<Not mentioned\>                   | \<Not mentioned\>          |
 | rsa_pss_pss_sha512                | 0x080B [^25] |                   | recommended                  | [^26]            | recommended                               | YEAR 2031+           | recommended              |                         | optional               | recommended              | \<Not mentioned\>             | \<Not mentioned\>                   | \<Not mentioned\>          |
 | ecdsa_secp256r1_sha256            | 0x0403       |                   | recommended                  | [^27]            | recommended                               | YEAR 2031+           | recommended              |                         | recommended            | recommended              | \<Not mentioned\>             | \<Not mentioned\>                   | \<Not mentioned\>          |
 | ecdsa_secp384r1_sha384            | 0x0503       |                   | recommended                  | [^28]            | recommended                               | YEAR 2031+           | recommended              |                         | recommended            | recommended              | \<Not mentioned\>             | \<Not mentioned\>                   | \<Not mentioned\>          |
 | ecdsa_secp521r1_sha512            | 0x0603       |                   | recommended                  | [^29]            | recommended                               | YEAR 2031+           | recommended              |                         | recommended            | recommended              | \<Not mentioned\>             | \<Not mentioned\>                   | \<Not mentioned\>          |
 | ecdsa_brainpoolP256r1tls13_sha256 | 0x081A       |                   | \<Not mentioned\>            | [^30]            | recommended                               | YEAR 2031+           | recommended              |                         | \<Not mentioned\>      | \<Not mentioned\>        | \<Not mentioned\>             | \<Not mentioned\>                   | \<Not mentioned\>          |
 | ecdsa_brainpoolP384r1tls13_sha384 | 0x081B       |                   | \<Not mentioned\>            | [^31]            | recommended                               | YEAR 2031+           | recommended              |                         | \<Not mentioned\>      | \<Not mentioned\>        | \<Not mentioned\>             | \<Not mentioned\>                   | \<Not mentioned\>          |
 | ecdsa_brainpoolP512r1tls13_sha512 | 0x081C       |                   | \<Not mentioned\>            | [^32]            | recommended                               | YEAR 2031+           | recommended              |                         | \<Not mentioned\>      | \<Not mentioned\>        | \<Not mentioned\>             | \<Not mentioned\>                   | \<Not mentioned\>          |

[^1]: Partly deduced from
    3.2.1 Server Certificate Profile (Table 3.1 of 800-52r2)
    together with supported groups and NIST SP 800-131Ar2.
[^2]: BSI-TR-02102-2, 3.4.3
[^3]: Table 2.6
[^4]: This signature algorithm does not exist in the IANA table it only exists in the IETF one
[^5]: [Key Agreement and Key Transport schemes based off pkcs1.5 are deprecated from 2023 and must not be used from 2024]
[^6]: [Key Agreement and Key Transport schemes based off pkcs1.5 are deprecated from 2023 and must not be used from 2024]
[^7]: [Key Agreement and Key Transport schemes based off pkcs1.5 are deprecated from 2023 and must not be used from 2024]
[^8]: [Key Agreement and Key Transport schemes based off pkcs1.5 are deprecated from 2023 and must not be used from 2024]
[^9]: This table contains the signature algorithms used by the TLS protocol. It does not refer to the ones used inside the X.509 certificates. 
[^10]: [Key Agreement and Key Transport schemes based off pkcs1.5 are deprecated from 2023 and must not be used from 2024]
[^11]: [Key Agreement and Key Transport schemes based off pkcs1.5 are deprecated from 2023 and must not be used from 2024]
[^12]: [Key Agreement and Key Transport schemes based off pkcs1.5 are deprecated from 2023 and must not be used from 2024]
[^13]: OID 1.2.840.113549.1.1.11 (deducted from RFC8446)
[^14]: approved in 800-52 (tabella 3.1)
[^15]: OID 1.2.840.113549.1.1.12 (deducted from RFC8446)
[^16]: approved in 800-52 (tabella 3.1)
[^17]: OID 1.2.840.113549.1.1.13 (deducted from RFC8446)
[^18]: approved in 800-52 (tabella 3.1)
[^19]: not mentioned until 2023 (800-186)
[^20]: not mentioned until 2023 (800-186)
[^21]: OID 1.2.840.113549.1.1.10 (deducted from RFC8446)
[^22]: approved in 800-52 (tabella 3.1)
[^23]: OID 1.2.840.113549.1.1.10 (deducted from RFC8446)
[^24]: approved in 800-52 (table 3.1)
[^25]: OID 1.2.840.113549.1.1.10 (deducted from RFC8446)
[^26]: approved in 800-52 (table 3.1)
[^27]: ecdsa and sha (>= 256) were approved in 800-52, secp* in 800-56A
[^28]: ecdsa and sha (>= 256) were approved in 800-52, secp* in 800-56A
[^29]: ecdsa and sha (>= 256) were approved in 800-52, secp* in 800-56A
[^30]: not mentioned until 2023 (800-186)
[^31]: not mentioned until 2023 (800-186)
[^32]: not mentioned until 2023 (800-186)
