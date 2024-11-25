# TLS (Transport Layer Security) Notes

## Introduction

- **TLS** is a protocol that enables:
  - Secure communication between a client and a server.
  - Agreement on a symmetric key for encryption.
  - Authentication of the server to the client.
- Commonly used in **HTTPS** to deliver secure web pages.
- TLS builds on an earlier protocol called **SSL**. While the term "SSL" is still used colloquially, TLS is more secure and preferred:
  - The most recent version, **TLS 1.3**, was finalized in 2018.

## Objectives of TLS

1. **Agreeing on a Symmetric Key:**
   - Enables encryption for secure communication.
2. **Server Authentication:**
   - Provides confidence that the server is authentic.

## Key Features of TLS 1.3

### Handshake Process

The handshake is a series of messages exchanged between the client and the server to:
- Agree on a symmetric key for encryption.
- Authenticate the server.

#### Steps of the Handshake

1. **Client Hello:**
   - The client sends:
     - **Supported Cipher Suites:** Cryptographic algorithms the client supports (e.g., Diffie-Hellman, RSA-PSS).
     - **Key Shares:** Pre-shared values used for key agreement (e.g., Diffie-Hellman parameters).
   - Purpose:
     - To inform the server of the client's cryptographic capabilities.

2. **Server Hello:**
   - The server responds with:
     - **Chosen Cipher Suite:** Based on compatibility with the client.
     - **Key Share:** The server’s contribution to the key agreement process.
     - **Digital Certificate:** Authenticates the server’s identity.
     - **Finished Message:** Encrypted using the agreed key.

3. **Client Verification:**
   - The client:
     - Uses the key exchange algorithm and key share to generate the symmetric key.
     - Decrypts and verifies the digital certificate.
   - If checks are successful, the client sends a "finished" message and begins encrypted communication.

4. **Secure Communication:**
   - Both client and server communicate using the agreed symmetric key for encryption.

## Security Properties of TLS 1.3

1. **Forward Secrecy:**
   - Protects past communications even if a secret key is compromised.
   - Achieved using **ephemeral keys** in the Diffie-Hellman key exchange.
   - Prevents retrospective decryption of communications.

2. **Improved Cipher Suite Security:**
   - TLS 1.3 limits the use of insecure cryptographic protocols and parameters (e.g., some used in TLS 1.2).
   - Ensures stronger confidentiality and resilience against attacks.

## Key Differences Between TLS 1.2 and TLS 1.3

| **Feature**            | **TLS 1.2**                         | **TLS 1.3**                     |
|-------------------------|-------------------------------------|----------------------------------|
| **Handshake Speed**     | Slower, requires more messages.    | Faster, fewer message exchanges.|
| **Key Sharing**         | Includes RSA.                     | Only ephemeral key exchanges.   |
| **Cipher Suite Options**| Broader, includes less secure options.| Limited to secure protocols only.|
| **Forward Secrecy**     | Not guaranteed.                   | Guaranteed via ephemeral keys.  |

## Applications of TLS

- **Web Browsing:** Secure communication in HTTPS.
- **Email:** Encrypts messages during transit.
- **VPNs:** Secure tunneling for remote access.