# Digital Certificates - Questions

## Introduction

&nbsp;
<details>
<summary>
1. Why are digital certificates important in TLS?
</summary>

Digital certificates are crucial in TLS as they authenticate servers to clients, ensuring the server is who it claims to be and preventing man-in-the-middle attacks.
</details>

&nbsp;
<details>
<summary>
2. What type of attack do digital certificates help prevent?
</summary>

Digital certificates help prevent **man-in-the-middle attacks**, such as when an attacker intercepts and replaces a server's key during a key exchange.
</details>

## What is a Digital Certificate?

&nbsp;
<details>
<summary>
1. Define a digital certificate.
</summary>

A digital certificate is a collection of data that associates a **public key** with a server and is digitally signed by a trusted certificate authority (CA).
</details>

&nbsp;
<details>
<summary>
2. What is the role of a certificate authority (CA)?
</summary>

A certificate authority (CA) is a trusted third party that:
* Verifies a server belongs to the claiming entity.
* Associates the entity's public key with the server.
* Digitally signs the public key and other certificate information to establish trust.
</details>

## Certificate Signing Request (CSR)

&nbsp;
<details>
<summary>
1. What is a Certificate Signing Request (CSR)?
</summary>

A CSR is a block of encoded text generated on the server where the certificate will be installed. It includes the server's public key and organisational details.
</details>

&nbsp;
<details>
<summary>
2. List the components of a CSR.
</summary>

A CSR includes:
* Public key.
* Common name (FQDN of the server).
* Organisation name.
* Department responsible for the server.
* City, state, country, or region.
* Email address of the responsible person.
</details>

## Verifying a Certificate Request

&nbsp;
<details>
<summary>
1. How does a certificate authority (CA) validate a CSR?
</summary>

A CA validates a CSR through:
1. **Domain Validation:** Sending an authentication token or link to the domain's administrative email.
2. **Research and Validation:** Ensuring the server and public key belong to the requesting entity.
</details>

&nbsp;
<details>
<summary>
2. What happens after a CA validates a CSR?
</summary>

The CA issues a certificate by:
1. Associating the public key from the CSR with the requesting entity.
2. Digitally signing the certificate using the CA's signing key.
</details>

## Components of a Digital Certificate

&nbsp;
<details>
<summary>
1. What are the key components of a digital certificate?
</summary>

Key components of a digital certificate include:
* Name (identifying the server or entity).
* Validity period.
* Issuer (certificate authority).
* Owner's public key.
* Digital signature (created by the CA's signing key).
</details>

## Verifying a Digital Certificate

&nbsp;
<details>
<summary>
1. How do clients verify a certificate's authenticity?
</summary>

Clients verify a certificate's authenticity by:
1. Checking the digital signature using the CA's public key.
2. Ensuring the certificate's integrity.
3. Verifying the certificate is not outdated.
</details>

&nbsp;
<details>
<summary>
2. Why do browsers sometimes display warnings about digital certificates?
</summary>

Browsers display warnings when:
* The certificate is **not trusted**.
* The certificate is **self-signed** or invalid.
</details>