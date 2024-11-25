# TLS Questions

## Introduction

&nbsp;
<details>
<summary>
1. What does TLS enable in communication between a client and a server?
</summary>

TLS enables secure communication by:
- Agreeing on a symmetric key for encryption.
- Authenticating the server to the client.
</details>

&nbsp;
<details>
<summary>
2. How is TLS related to SSL?
</summary>

TLS builds on the SSL protocol. While SSL terminology is still used, TLS is more secure and is preferred over SSL.
</details>

&nbsp;
<details>
<summary>
3. What is the most recent version of TLS, and when was it finalized?
</summary>

The most recent version is TLS 1.3, finalized in 2018.
</details>

## Objectives of TLS

&nbsp;
<details>
<summary>
1. What are the two primary objectives of TLS?
</summary>

1. Agreeing on a symmetric key for encryption.
2. Authenticating the server.
</details>

## Key Features of TLS 1.3

### Handshake Process

&nbsp;
<details>
<summary>
1. What is the purpose of the handshake in TLS?
</summary>

The handshake enables:
- Agreement on a symmetric key for encryption.
- Authentication of the server.
</details>

&nbsp;
<details>
<summary>
2. What information is included in the Client Hello message?
</summary>

The Client Hello message includes:
- Supported cipher suites.
- Key shares for key agreement.
</details>

&nbsp;
<details>
<summary>
3. What does the Server Hello message contain?
</summary>

The Server Hello message contains:
- The chosen cipher suite.
- A key share.
- The server's digital certificate.
- A finished message (encrypted using the agreed key).
</details>

&nbsp;
<details>
<summary>
4. What steps does the client perform after receiving the Server Hello?
</summary>

The client:
- Uses the key exchange algorithm and key share to generate the symmetric key.
- Decrypts and verifies the digital certificate.
</details>

&nbsp;
<details>
<summary>
5. What happens after the handshake is complete?
</summary>

The client and server communicate securely using the agreed symmetric key for encryption.
</details>

## Security Properties of TLS 1.3

&nbsp;
<details>
<summary>
1. What is forward secrecy, and how does TLS 1.3 achieve it?
</summary>

Forward secrecy ensures that past communications remain secure even if a secret key is compromised. It is achieved through ephemeral keys used in the Diffie-Hellman key exchange.
</details>

&nbsp;
<details>
<summary>
2. How does TLS 1.3 improve cipher suite security compared to TLS 1.2?
</summary>

TLS 1.3 limits the use of insecure cryptographic protocols and parameters, ensuring stronger confidentiality and resilience against attacks.
</details>

## Key Differences Between TLS 1.2 and TLS 1.3

&nbsp;
<details>
<summary>
1. How does the handshake process differ between TLS 1.2 and TLS 1.3?
</summary>

TLS 1.3 has a faster handshake process with fewer message exchanges compared to TLS 1.2.
</details>

&nbsp;
<details>
<summary>
2. How does key sharing differ between TLS 1.2 and TLS 1.3?
</summary>

TLS 1.2 includes RSA for key sharing, whereas TLS 1.3 only uses ephemeral key exchanges.
</details>

&nbsp;
<details>
<summary>
3. How does TLS 1.3 ensure forward secrecy compared to TLS 1.2?
</summary>

TLS 1.3 ensures forward secrecy by using ephemeral keys, while TLS 1.2 does not guarantee this.
</details>

## Applications of TLS

&nbsp;
<details>
<summary>
1. Name three common applications of TLS.
</summary>

1. **Web Browsing:** Secure communication in HTTPS.
2. **Email:** Encrypting messages during transit.
3. **VPNs:** Secure tunneling for remote access.
</details>
