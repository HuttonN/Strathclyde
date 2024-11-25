# End-To-End Encryption

## Introduction

When two parties wish to communicate securely, e.g. using a messaging system, they can do this in two general approaches. 

## Server-Mediated Encryption

The server they use to appropriately distribute the communications (e.g. an application server) can have a symmetric key for Alice and Bob. This is illustrated below:

![Server-Mediated Encryption](./images/Server-Mediated_Encryption.png)

Note this is a somewhat simplified version, there are likely multiple intermediaries, but the principle remains the same. 

### Process

1. The server holds symmetric keys for both Alice and Bob.
1. Alice encrypts her message using her symmetric key and sends it to the server.
1. The server decrypts Alice’s message and re-encrypts it using Bob’s symmetric key before forwarding it to Bob.

### Limitations

In this approach the communication is secured over insecure channels but has limitations: 

* the server is able to decrypt the communication. This is problematic for a number of reasons. Clearly individuals may wish to retain privacy in their communications, even from the service they are using. 
* Additionally, should the server be compromised all communications will also be compromised.

Neither of these are ideal. Instead, we can deploy end to end encryption.

## End-To-End Encryption

![End-To-End Encryption](./images/End-To-End_Encryption.png)

This can be achieved using different mechanisms, but it is fundamentally structured as follows.

### Process

1. The server does not hold the decryption key for either Alice or Bob.
1. Alice encrypts her message, and the server passes it to Bob without decrypting it.
1. Bob decrypts the message using his private key.

### Mechanisms

End-To-End encryption can be achieved through different mechanisms:
* Using symmetric keys with a key-sharing algorithm, such as Diffie-Hellman.
* Using public key crptography (asymmetric)

### Applications

E2EE is used in popular messaging apps such as Signal and WhatsApp. They make use of mechanisms we have seen elsewhere, albeit variations on them. In particular, they makes use of 
* Elliptic Curve Cyrptography (ECC)
* Triple Diffie Hellman
* Public key cryptography 
* Symmetric cryptography.

### Controversy

E2EE has been controversial, particularly around governments wishing to have access to all communication should they believe there to be an issue of national security. This has led to debates over the balance between privacy and security.

### Advantages

E2EE does have the following advantages over the form described at the top:
* **Privacy:** Communication remains private, even from the service provider.
* **Security:** Even if the server is compromised, communications cannot be decrypted without the user's private keys.