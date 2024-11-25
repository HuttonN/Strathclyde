# Introducing Public-key Cryptography - questions

&nbsp;
<details>
<summary>
1. What problem does public key cryptography solve
</summary>

Public key cryptography (sometimes known as asymmetric cryptography) solves the key distribution problem, that is the issue of trying to agree a shared key over an insecure channel. This can also be solved by key exchange algorithms such as Diffie-Hellman.
 
</details>

&nbsp;

<details>
<summary>
2. Describe the approach, including how individuals communicate 
</summary>

In this approach a key pair is generated for each entity (such as an individual):

* a private key, which is kept only by the entity
* a public key, which can be shared without compromising security

In order to communicate securely with another entity, Bob say, we would need to encrypt the message using Bob's public key. Only Bob will then be able to decrypt this, as Bob is the only person with access to the corresponding private key.
</details>

&nbsp;

<details>
<summary>
3. State the crucial features of the key pair 
</summary>

* The key pair is mathematically linked in such a way that data encrypted with the private key can only be decrypted by its corresponding public key and vice versa. 
* It is also computationally infeasible to derive the private key from the publc key and vice versa.
</details>

&nbsp;

<details>
<summary>
4. As well as security, what else does public key cryptography provide. Describe.
</summary>
Public key cryptography can also provide some confidence in authenticity. For example, if Bob wants to share information with Alice and provide Alice assurance it comes from Bob then Bob should encrypt the message using his private key. This will not provide confidentiality, but the public key for Bob is the only key which can decrypt this. Thus, if Alice can successfully decrypt using the public key for Bob then there is some assurance the message comes from Bob. In practical use, there are further steps to ensure the integrity of the message which we will come back to. Clearly if Bob's private key was compromised this would be problematic, and the above is more for demonstration.
</details>

&nbsp;

<details>
<summary>
5. State two more features of public and private key pairs.
</summary>

* Whilst the natural assumption is that an entity would have only one public and private key pair, the reality is that there may be multiple key pairs for a single entity. Some of these key pairs may also be ephemeral, that is they are for temporary use e.g. a single communication session over the internet.
* Another point to note is that sometimes keys may be compromised (e.g. if stored on a server which is compromised) or otherwise lost. In such a situation the entity who owns the key pair needs to revoke their public key and generate a new key pair.
</details>