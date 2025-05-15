 | Certificate signature algorithm | IANA | ('NIST', '')    [^1] | ('NIST', 'Condition')                                               | ('BSI', '')     [^2] | ('BSI', 'Condition')                   [^5]                  | ('ANSSI', '')   [^3] | ('ACN', 'Recommended') | ('ACN', 'Compatibility') | ('MOZILLA (+AgID)', 'Modern') [^4] | ('MOZILLA (+AgID)', 'Intermediate') | ('MOZILLA (+AgID)', 'Old') |
 | :------------------------------ | ---: | :------------------- | :------------------------------------------------------------------ | :------------------- | :----------------------------------------------------------- | :------------------- | :--------------------- | :----------------------- | :--------------------------------- | :---------------------------------- | :------------------------- |
 | anonymous                       |    0 | must not        [^6] |                                                                     | \<Not mentioned\>    |                                                              | must not        [^7] | \<Not mentioned\>      | \<Not mentioned\>        | \<Not mentioned\>                  | \<Not mentioned\>                   | \<Not mentioned\>          |
 | rsa                             |    1 | must not [^12]       |                                                                     | recommended          | THIS or CertificateSignature dsa;ecdsa;rsa-pss AND YEAR 2025 | not recommended      | optional               | optional                 | \<Not mentioned\>                  | \<Not mentioned\>                   | \<Not mentioned\>          |
 | rsa-pss                         |    1 | must                 | THIS or CertificateSignature ecdsa and CHECK_KEY_TYPE rsa [^9]      | recommended          | THIS or CertificateSignature dsa;ecdsa;rsa                   | optional             | optional               | recommended              | \<Not mentioned\>                  | \<Not mentioned\>                   | \<Not mentioned\>          |
 | dsa                             |    2 | \<Not mentioned\>    | CHECK_KEY_TYPE dsa                                        [^10]     | recommended          | THIS or CertificateSignature rsa;ecdsa;rsa-pss AND YEAR 2029 | \<Not mentioned\>    | \<Not mentioned\>      | \<Not mentioned\>        | \<Not mentioned\>                  | \<Not mentioned\>                   | \<Not mentioned\>          |
 | ecdsa                           |    3 | must                 | THIS or CertificateSignature rsa-pss and CHECK_KEY_TYPE ecdsa [^11] | recommended          | THIS or CertificateSignature rsa;dsa;rsa-pss                 | recommended          | recommended            | recommended              | \<Not mentioned\>                  | \<Not mentioned\>                   | \<Not mentioned\>          |

[^1]: SP800-52 section 3.2
[^2]: BSI-TR-02102-2, 3.3.3 + 3.4.3
[^3]: R8
[^4]: Being a list of recommendations:
    
    not mentioned --> not recommended
[^5]: Not explicitally mentioned but required to match the mechanical check of the conditions with the NIST case
[^6]: TLS servers conforming to this specification shall be configured with an RSA signature certificate or an ECDSA signature certificate
[^7]: R8+R5
[^9]: At a minimum, TLS servers conforming to this specification shall be configured with an RSA signature certificate or an ECDSA signature certificate.
[^10]: recommended  "if key is DH"
[^11]: At a minimum, TLS servers conforming to this specification shall be configured with an RSA signature certificate or an ECDSA signature certificate.
[^12]: Since all the signature algorithms using RSA-PKCS1 are deprecated, the use of RSA-PSS is considered as a MUST.
