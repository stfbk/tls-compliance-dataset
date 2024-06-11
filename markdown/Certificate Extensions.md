 | Extension                        | ('NIST', '')      | ('NIST', 'critical') [^2] | ('NIST', 'condition')                                                                                                                                                                                                                                                                                | ('BSI', '')     [^1] | ('BSI', 'critical') | ('BSI', 'condition')                                                                                                    | ('ANSSI', '')         | ('ANSSI', 'condition')                                     | ('MOZILLA', '')   |
 | :------------------------------- | :---------------- | :------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------- | :------------------ | :---------------------------------------------------------------------------------------------------------------------- | :-------------------- | :--------------------------------------------------------- | :---------------- |
 | authorityKeyIdentifier           | recommended       |                           | CHECK_AKI                                                                                                                                                                                                                                                                                      [^3]  | \<Not mentioned\>    |                     |                                                                                                                         | must            [^4]  |                                                            | \<Not mentioned\> |
 | subjectKeyIdentifier       [^5]  | recommended       |                           | NOTE_ALWAYS The guidelines state `Same as in Public-Key Cryptography Standards [PKCS 10] request or calculated by the issuing CA`. The tool can not verify this condition since this specific check can only be performed by monitoring the endpoint during the certificate issuing phase      [^6]  | \<Not mentioned\>    |                     |                                                                                                                         |                       |                                                            | \<Not mentioned\> |
 | keyUsage                   [^7]  | recommended       | yes                       | (VALUE CertificateExtensions Digital Signature in keyUsage OR VALUE CertificateExtensions Key Agreement in keyUsage) and NOTE_FALSE Invalid keyUsage, allowed key usages are digital signature if using RSA certificate and key agreement if using ECDH or DH certificate                      [^8]  | must                 | yes                 |                                                                                                                         | must            [^9]  |                                                            | \<Not mentioned\> |
 | extendedKeyUsage           [^10] | must        [^11] |                           | NOTE_FALSE Issue detected: {reason} within certificate #{cert} AND VALUE CertificateExtensions TLS Web Server Authentication in extendedKeyUsage                                                                                                                                               [^12] | recommended          |                     |                                                                                                                         | must            [^13] |                                                            | \<Not mentioned\> |
 | extendedKeyUsage           [^14] | must not          |                           | (NOTE_TRUE Issue detected: {reason} within certificate #{cert} AND VALUE CertificateExtensions Any Extended Key Usage in extendedKeyUsage) OR CHECK_SAME_KEYUSAGE                                                                                                                              [^15] | \<Not mentioned\>    |                     |                                                                                                                         |                       |                                                            | \<Not mentioned\> |
 | Certificate Policies             | optional          |                           |                                                                                                                                                                                                                                                                                                      | \<Not mentioned\>    |                     |                                                                                                                         | \<Not mentioned\>     |                                                            | \<Not mentioned\> |
 | subjectAltName             [^16] | must        [^17] |                           | VALUE CertificateExtensions DNS in subjectAltName OR VALUE CertificateExtensions IP Address in subjectAltName                                                                                                                                                                                  [^18] | must not             |                     | NOTE_TRUE Issue detected: {reason} within certificate #{cert} and VALUE CertificateExtensions * in subjectAltName [^19] | must            [^20] |                                                            | \<Not mentioned\> |
 | authorityInfoAccess        [^21] | must        [^22] |                           | VALUE CertificateExtensions OCSP - URI in authorityInfoAccess and NOTE_FALSE the authorityInfoAccess extension must have a field CA Issuers containing HTTP URL for certificates issued to issuing CA                                                                                          [^23] | must                 |                     | THIS or CertificateExtensions CRL Distribution Points                                                                   | must                  | THIS or CertificateExtensions CRL Distribution Points      | \<Not mentioned\> |
 | authorityInfoAccess              | must        [^24] |                           | VALUE CertificateExtensions CA ISSUERS - URI in authorityInfoAccess and NOTE_FALSE the authorityInfoAccess extension must have the Online Certificate Status Protocol and it must contain HTTP URL for the issuing CA OCSP responder                                                           [^25] |                      |                     |                                                                                                                         |                       |                                                            | \<Not mentioned\> |
 | crlDistributionPoints      [^26] | optional          |                           | VALUE CertificateExtensions IP in crlDistributionPoints OR VALUE CertificateExtensions URI in crlDistributionPoints                                                                                                                                                                            [^27] | must                 |                     | THIS or CertificateExtensions Authority Information Access                                                              | must                  | THIS or CertificateExtensions Authority Information Access | \<Not mentioned\> |
 | crlDistributionPoints            | must not          |                           | NOTE_TRUE Issue detected: {reason} within certificate #{cert} AND (VALUE CertificateExtensions Relative Name in crlDistributionPoints OR VALUE CertificateExtensions CRL Issuer in crlDistributionPoints OR VALUE CertificateExtensions Reasons in crlDistributionPoints) AND DISABLE_IF False [^28] |                      |                     |                                                                                                                         |                       |                                                            | \<Not mentioned\> |
 | ct_precert_scts            [^29] | optional    [^30] |                           |                                                                                                                                                                                                                                                                                                      |                      |                     |                                                                                                                         | \<Not mentioned\>     |                                                            | \<Not mentioned\> |
 | OCSP must staple extension [^31] | optional    [^32] |                           |                                                                                                                                                                                                                                                                                                      |                      |                     |                                                                                                                         | \<Not mentioned\>     |                                                            | \<Not mentioned\> |

[^1]: BSI TR-03116-4
[^2]: Each extension in a certificate is designated as either critical or non-critical.  A certificate-using system MUST reject the certificate if it encounters a critical extension it does not recognize or a critical extension that contains information that it cannot process.  A non-critical extension MAY be ignored if it is not recognized, but MUST be processed if it is recognized.  The following sections present recommended extensions used within Internet certificates and stand
    
    https://www.rfc-editor.org/rfc/rfc5280 section 4.2
[^3]: Same as subject key identifier in issuing CA certificate; Prohibited: Issuer DN, Serial Number tuple
[^4]: R32
[^5]: Subject Key Identifier (SKI)
[^6]: Same as in Public-Key Cryptography Standards (PKCS) 10 request or calculated by the issuing CA
[^7]: Key Usage
[^8]: RSA, ECDSA, or DSA signature certificate: digital signature;
    ECDH or DH certificate: key agreement
[^9]: R27
[^10]: Extended Key Usage
[^11]: server
[^12]: id-kp-serverAuth {1 3 6 1 5 5 7 3 1}
    http://oid-info.com/get/1.3.6.1.5.5.7.3.1
[^13]: R28
[^14]: Extended Key Usage
[^15]: the keyAgreement and keyEncipherments are considered mutually exclusive as show in section 5.4.3 of https://www.etsi.org/deliver/etsi_ts/102200_102299/102280/01.01.01_60/ts_102280v010101p.pdf
[^16]: Subject Alternative Name (SAN)
[^17]: Required. Multiple SANs are permitted, e.g., for load balanced environments.
[^18]: DNS host name, or IP address if there is no DNS name assigned. Other name forms may be included, if appropriate.
[^19]: use wildcards in CN
[^20]: R29
[^21]: Authority Information Access
[^22]: Required. Multiple SANs are permitted, e.g., for load balanced environments.
[^23]: field id-ad-caIssuers
[^24]: Required. Multiple SANs are permitted, e.g., for load balanced environments.
[^25]: field id-ad-caIssuers
[^26]: CRL Distribution Points
[^27]: HTTP value in distributionPoint
    field pointing to a full and complete CRL
    
    We don't check if the CRL is full and complete. We only check if the value in the cert is of type IP or URI
[^28]: A CRL is indicated by a DistributionPoint ::= SEQUENCE.
    This SEQUENCE can contain three items:
        distributionPoint: DistributionPointName
        reasons: ReasonFlags
        cRLIssuer: GeneralNames.
    
    The DistributionPointName type is a CHOICE with two options:
        fullName
        nameRelativeToCRLIssuer
    
    A valid distributionPoint must not have the "reasons" and "cRLIssuer" fields and the distributionPoint can not be of type nameRelativeToCRLIssuer
[^29]: Signed Certificate Timestamps List
[^30]: Optional. This extension contains a sequence of Signed Certificate
    Timestamps, which provide 
    evidence that the certificate has been submitted to Certificate Transparency logs.
[^31]: TLS Certificate Status Request
[^32]: Optional. This extension (sometimes referred to as the “must staple” extension) may be present to indicate to clients that the server supports OCSP stapling and will provide a stapled OCSP response when one is requested.
