# Digital signitures - questions

&nbsp;
<details>
<summary>
1. What do digital signatures provide
</summary>

Digital signatures give us a digital equivalent to a handwritten signature
 
</details>

&nbsp;
<details>
<summary>
2. How are digital signatures better
</summary>

Whereas a handwritten signature can easily be forged, a well-designed and implemented digital signature cannot. A digital signature gives us some assurance in terms of the integrity of the message, as well as some origin authentication.
 
</details>

&nbsp;
<details>
<summary>
3. Give a high-level description of how they work
</summary>

* We have the following elements:
    * a private key, $s$, that's used for signing.
    * a public key, $v$, used for verification.
    * a message that we would like to send, and prove that it's us that wrote it, and that it hasn't been tampered with
* What we can do is take the message and apply our private key to encrypt it, and send the encrypted message along with the original message. (Note that this won't achieve confidentiality)
* What the recipient can do is apply the public key to the message and compare to the encrypted message that was sent.
* If they are the same then we can be reassured of the origin.
 
</details>

&nbsp;
<details>
<summary>
4. What difficulties do especially small or large messages cause
</summary>

* If it's too small it could impact the security. For example, if the message was just the number ones, then you're not going to be able to encrypt that in a meaningful way. 
* If it's too large, we're sending a lot of information which could take a while.
 
</details>

&nbsp;
<details>
<summary>
5. How do we get around the difficulties with especially large or small messages
</summary>

We use cryptographic hash functions, which allows us to take any length input and provide a fixed length output. Common lengths are 128-bit to 256-bit and so on.
 
</details>

&nbsp;
<details>
<summary>
6. What important properties do hashes have
</summary>

* Determinant: The same message will always result in the same output. It shouldn't ever be the case that the same message can go to multiple outputs.
* Collision resistance: For it to be crptographically secure, we need to be sure that we avoid the case where lots of different messages result in the same final output.
* One-way property: It should be really difficult to go backwards. That is, if we have the output or hash value, it must be computationally infeasible to then determine what the origianl input was.
 
</details>

&nbsp;
<details>
<summary>
7. What is a message digest
</summary>

It is the output of a message put through a cryptographically secure hash function
 
</details>