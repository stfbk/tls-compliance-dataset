 | Certificate signature algorithm      | IANA | TLS version | ('NIST', '')    [^1] | ('NIST', 'Condition')                                            | ('BSI', '')     [^2] | ('BSI', 'Condition')                   [^5]              | ('ANSSI', '')   [^3] | ('MOZILLA (+AgID)', 'Modern') [^4] | ('MOZILLA (+AgID)', 'Intermediate') | ('MOZILLA (+AgID)', 'Old') |
 | :----------------------------------- | ---: | ----------: | :------------------- | :--------------------------------------------------------------- | :------------------- | :------------------------------------------------------- | :------------------- | :--------------------------------- | :---------------------------------- | :------------------------- |
 | anonymous                            |    0 |         1.2 | must not        [^6] |                                                                  | \<Not mentioned\>    |                                                          | must not        [^7] | \<Not mentioned\>                  | \<Not mentioned\>                   | \<Not mentioned\>          |
 | rsa                             [^8] |    1 |         1.2 | must                 | THIS or CertificateSignature ecdsa and CHECK_KEY_TYPE rsa  [^9]  | recommended          | THIS or CertificateSignature dsa;ecdsa AND YEAR 2025     | optional             | \<Not mentioned\>                  | \<Not mentioned\>                   | \<Not mentioned\>          |
 | dsa                                  |    2 |         1.2 | \<Not mentioned\>    | CHECK_KEY_TYPE dsa                                         [^10] | recommended          | THIS or CertificateSignature rsa;ecdsa     AND YEAR 2029 | \<Not mentioned\>    | \<Not mentioned\>                  | \<Not mentioned\>                   | \<Not mentioned\>          |
 | ecdsa                                |    3 |         1.2 | must                 | THIS or CertificateSignature rsa and CHECK_KEY_TYPE ecdsa [^11]  | recommended          | THIS or CertificateSignature rsa;dsa                     | recommended          | \<Not mentioned\>                  | \<Not mentioned\>                   | \<Not mentioned\>          |

[^1]: SP800-52 section 3.2
[^2]: BSI-TR-02102-2, 3.3.3 + 3.4.3
[^3]: R8
[^4]: Being a list of recommendations:
    
    not mentioned --> not recommended
[^5]: Not explicitally mentioned but required to match the mechanical check of the conditions with the NIST case
[^6]: TLS servers conforming to this specification shall be configured with an RSA signature certificate or an ECDSA signature certificate
[^7]: R8+R5
[^8]: We consider RSASSA-PSS as a subset of RSA (as stated in ANSSI v1.2 R8)
[^9]: At a minimum, TLS servers conforming to this specification shall be configured with an RSA signature certificate or an ECDSA signature certificate.
[^10]: recommended  "if key is DH"
[^11]: At a minimum, TLS servers conforming to this specification shall be configured with an RSA signature certificate or an ECDSA signature certificate.
