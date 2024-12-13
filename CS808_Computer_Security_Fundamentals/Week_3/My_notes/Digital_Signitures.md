# Digital signitures

Digital signatures give us a digital equivalent to a handwritten signature, but they're better. Whereas a handwritten signature can easily be forged, a well-designed and implemented digital signature cannot. A digital signature gives us some assurance in terms of the integrity of the message, as well as some origin authentication.

Lets have a high-level look at how they work:
* We have the following elements:
    * a private key, $s$, that's used for signing.
    * a public key, $v$, used for verification.
    * a message that we would like to send, and prove that it's us that wrote it, and that it hasn't been tampered with
* What we can do is take the message and apply our private key to encrypt it, and send the encrypted message along with the original message. (Note that this won't achieve confidentiality)
* What the recipient can do is apply the public key to the message and compare to the encrypted message that was sent.
* If they are the same then we can be reassured of the origin.

One thing to note is that if a message is especially small or large it can be difficult:
* If it's too small it could impact the security. For example, if the message was just the number ones, then you're not going to be able to encrypt that in a meaningful way. 
* If it's too large, we're sending a lot of information which could take a while.

What we do is use cryptographic hash functions, which allows us to take any length input and provide a fixed length output. Common lengths are 128-bit to 256-bit and so on.

Hashes have a number of important properties:

* Determinant: The same message will always result in the same output. It shouldn't ever be the case that the same message can go to multiple outputs.
* Collision resistance: For it to be crptographically secure, we need to be sure that we avoid the case where lots of different messages result in the same final output.
* One-way property: It should be really difficult to go backwards. That is, if we have the output or hash value, it must be computationally infeasible to then determine what the origianl input was.

Going back to our example, instead of sending the message as is, which could be problematic for the reasons given above, we can take that message and put it through a cryptographically secure hash function to get our output, which can be referred to as our message digest

---

Next: [End-To-End Encryption](End-To-End_Encryption.md)