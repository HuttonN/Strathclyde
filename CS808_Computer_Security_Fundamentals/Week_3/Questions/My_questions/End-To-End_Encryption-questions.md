# End-To-End Encryption - questions

## Introduction

&nbsp;
<details>
<summary>
1. State the two approaches for two parties wishing to communicate securely
</summary>

* Server-Mediated Encryption
* End-To-End Encryption
</details>


## Server-Mediated Encryption

&nbsp;
<details>
<summary>
1. What does the server hold in this case
</summary>

The server used to appropriately distribute the communications (e.g. an application server) can have a symmetric key for Alice and Bob.

</details>

### Process

&nbsp;
<details>
<summary>
1. Describe the process for Server-Mediated Encryption
</summary>

1. The server holds symmetric keys for both Alice and Bob.
1. Alice encrypts her message using her symmetric key and sends it to the server.
1. The server decrypts Alice’s message and re-encrypts it using Bob’s symmetric key before forwarding it to Bob.

</details>

### Limitations

&nbsp;
<details>
<summary>
1. What are the limitations of Server-Mediated Encryption
</summary>

In this approach the communication is secured over insecure channels but has limitations: 

* the server is able to decrypt the communication. This is problematic for a number of reasons. Clearly individuals may wish to retain privacy in their communications, even from the service they are using. 
* Additionally, should the server be compromised all communications will also be compromised.

</details>

## End-To-End Encryption

### Process

&nbsp;
<details>
<summary>
1. Describe the process for E2EE
</summary>

1. The server does not hold the decryption key for either Alice or Bob.
1. Alice encrypts her message, and the server passes it to Bob without decrypting it.
1. Bob decrypts the message using his private key.

</details>

### Mechanisms

&nbsp;
<details>
<summary>
1. What mechanisms can be used to achieve E2EE
</summary>

End-To-End encryption can be achieved through different mechanisms:
* Using symmetric keys with a key-sharing algorithm, such as Diffie-Hellman.
* Using public key crptography (asymmetric)
 
</details>

### Applications

&nbsp;
<details>
<summary>
1. Where is E2EE used 
</summary>

E2EE is used in popular messaging apps such as Signal and WhatsApp.
 
</details>

&nbsp;
<details>
<summary>
2. What mechansisms do they make use of
</summary>

* Elliptic Curve Cyrptography (ECC)
* Triple Diffie Hellman
* Public key cryptography 
* Symmetric cryptography.
 
</details>

### Controversy

&nbsp;
<details>
<summary>
1. Describe why E2EE has been controversial at times
</summary>

* E2EE has been controversial, particularly around governments wishing to have access to all communication should they believe there to be an issue of national security. 
* This has led to debates over the balance between privacy and security.
 
</details>

### Advantages 

&nbsp;
<details>
<summary>
1. What advantages does E2EE have over Server-Mediated Encryption
</summary>

* **Privacy:** Communication remains private, even from the service provider.
* **Security:** Even if the server is compromised, communications cannot be decrypted without the user's private keys.
 
</details>