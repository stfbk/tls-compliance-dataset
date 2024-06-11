 | HashAlgorithm | IANA | TLS version | ('NIST', '')        [^1] | ('BSI', '')       | ('ANSSI', '')    [^2] | ('MOZILLA (+AgID)', 'Modern') | ('MOZILLA (+AgID)', 'Intermediate') | ('MOZILLA (+AgID)', 'Old') |
 | :------------ | ---: | ----------: | :----------------------- | :---------------- | :-------------------- | :---------------------------- | :---------------------------------- | :------------------------- |
 | none          |    0 |         1.2 | must not                 | \<Not mentioned\> | must not              | \<Not mentioned\>             | \<Not mentioned\>                   | \<Not mentioned\>          |
 | md5           |    1 |         1.2 | must not                 | \<Not mentioned\> | must not              | \<Not mentioned\>             | \<Not mentioned\>                   | \<Not mentioned\>          |
 | sha1          |    2 |         1.2 | must not                 | \<Not mentioned\> | must not              | \<Not mentioned\>             | \<Not mentioned\>                   | \<Not mentioned\>          |
 | sha224        |    3 |         1.2 | must not                 | \<Not mentioned\> | must not              | \<Not mentioned\>             | \<Not mentioned\>                   | \<Not mentioned\>          |
 | sha256        |    4 |         1.2 | recommended              | recommended       | must                  | \<Not mentioned\>             | \<Not mentioned\>                   | \<Not mentioned\>          |
 | sha384        |    5 |         1.2 | recommended              | recommended       | must                  | \<Not mentioned\>             | \<Not mentioned\>                   | \<Not mentioned\>          |
 | sha512        |    6 |         1.2 | recommended              | recommended       | must                  | \<Not mentioned\>             | \<Not mentioned\>                   | \<Not mentioned\>          |

[^1]: Partly deduced from
    3.2.1 Server Certificate Profile
    together with supported groups
    first row, table at page 11, SP800-52
[^2]: ANSSI only allows the usage of SHA-2 family hash algorithms.
    SHA-2 family is defined as (SHA-256, SHA-384, SHA-512)
