# Digital Certificates Overview

## Introduction

In order to understand the TLS protocol we need to understand a digital certificate. So far, we have worked on the basis that we can trust the key provided by a server, but what if they are not who they claim to be?

## Why Digital Certificates?

Digital certificates serve the following purposes:

- They ensure the **authenticity** of a server during communication.
- They prevent man-in-the-middle attacks (e.g., **Eve intercepting key exchange** and replacing the server's key).
- **Digital certificates** are used to authenticate servers to clients.

## What is a Digital Certificate?

A digital certificate is a **collection of data** that associates a **public key** with a server.

They are managed by certificate authorities. A certificate authority is a trusted third party who verify a server belongs to the entity claiming it, and associates the entity’s public key with that server. The certificate authority digitally signs the public key and other information (i.e. the digital certificate) using their signing key to demonstrate its trust in the server’s identity.

## How Certificates are Requested

### Certificate Signing Request (CSR)

- A **CSR** is generated on the server where the certificate will be installed.
- It is a block of text, typically encoded in **ASN.1** (Abstract Syntax Notation).
- Contains the following:
  - **Public Key**
  - **Common Name**: Fully Qualified Domain Name (FQDN) of the server.
  - **Organisational Details**:
    - Organisation name.
    - Department responsible for the server (e.g., IT).
    - City, state, country, region.
    - Email address of the server's responsible person.
  
The following is an example of a CSR generated using OpenSSL. It appears as encoded symbols and letters.

![CSR](./images/CSR.png)

## How the Certificate Authority Verifies the Request

1. **Domain Validation**:
   - The CA sends an email to an administrative address associated with the domain.
   - Includes an **authentication token** or link.  
   - Using the token or link proves access to the domain.

2. **Research and Validation**:
   - The CA ensures the server and public key belong to the requesting entity.

3. **Certificate Issuance**:
   - Once verified, the CA associates the **public key** from the CSR with the requesting entity.
   - Signs the certificate using their **signing key**.

## Components of a Digital Certificate

- **Name**: Identifies the server or entity.
- **Time Frame**: Validity period of the certificate.
- **Issuer**: The certificate authority.
- **Owner's Public Key**: The public key associated with the server.
- **Digital Signature**: Created by the CA's signing key, vouching for the entity.

## Verifying a Digital Certificate

1. **Pre-installed Certificates**:
   - Many trusted certificates (e.g., VeriSign) are pre-installed on operating systems.
   - These include the CA’s **public key**, enabling signature verification.

2. **Verification Process**:
   - The client downloads the certificate from the web server.
   - The client verifies:
     - The **digital signature** using the CA's public key.
     - The **integrity** of the certificate.
     - That the certificate is not **outdated**.

3. **Browser Warnings**:
   - Web browsers alert users when:
     - The certificate is **not trusted**.
     - The certificate is **self-signed** or otherwise invalid.

---

**Note**: Digital certificates are a cornerstone of secure communications and provide trust in public key cryptography systems like TLS.

---

Next: [Transport Layer Security](Transport_Layer_Security)