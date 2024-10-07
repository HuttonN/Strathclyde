# Cryptography Comprehension Questions

## Question 1
Block ciphers can operate in either ECB mode or CBC mode.

1. Explain the difference between these two modes of operation. What extra information is required for CBC which isn’t required for ECB?

1. Construct a scenario which demonstrates the weakness of ECB mode.

Answer:
1. In ECB the plaintext is divided into fixed-size blocks, and each block is encrypted independently using the same encryption key. In CBC mode, each plaintext block is XORed with the previous ciphertext block before being encrypted. This introduces dependency between blocks, making the encryption of each block reliant on the previous block. CBC requires an initialisation vector.
1. Encrpting a repetitive message could lead to repeated ciphertext and an attacker could notice this.

## Question 2
What are the three properties which make a hash function a cryptographic hash function, and why are they important?

Answer:
1. pre-image resistant: given a random input, it is computationally infeasible to determine the input from the hash value alone. This effectively is a one-way function. This property ensures that even if an attacker knows the hash value (e.g., in the case of a hashed password), they cannot deduce the original input or message. It is important for protecting sensitive information, like passwords, even if their hashes are exposed.
1. second pre-image resistant: Given a hash value h1 it should be computationally infeasible to find a different input message which results in the same hash value h1. If an attacker could find a second pre-image (another input with the same hash), they could substitute a different message with the same hash, potentially forging digital signatures or altering data without detection.
1. collision resistant: It should not be feasible to produce two inputs which have the same hash value as output. Collision resistance is critical to preventing hash-based attacks, such as the birthday attack, where an attacker tries to find two distinct inputs with the same hash. Without collision resistance, attackers could exploit hash functions to generate fraudulent certificates, signatures, or other hashed data.

## Question 3
1. What form of attack can a MAC help mitigate? 
1. How does a MAC mitigate this? 
1. Why can’t we simply append a hash value to the end of the encrypted data to mitigate the attack?

Answer

1. 
1. 
1. 

## Question 4
1. Compare and contrast p-boxes and s-boxes 
1. How does AES use p-boxes and s-boxes?

Answer
1. p-boxes permute or reorder the bits, whereas s-boxes substitute the bits. A p-box could be considered a subclass of a p-box but no the other way round.
1. The AES uses s-boxes in the SubBytes operation and p-boxes in the ShiftRows transformation

## Question 5
In your own words, explain how a digital signature mitigates an attack in which the attacker intercepts the communication from sender to recipient and replaces the document with their own document.

## Question 6
You and a friend have public and private key pairs. 
1. How can you send secret messages to each other? 
1. What could information security property could you achieve if you encrypted a message with your private key and released the cipher text? 
1. How could you combine encryption using different keys to provide confidentiality and authenticity?

# Cryptography Scenario-based Questions

## Question 1
Alain Thénardiers often uses his company’s secure email server. He has lost his private key, but still has the corresponding public key. 
1. Is he still able to send encrypted emails? What about receiving? 
1. Is he still able to sign the email he sends? What about verifying the signatures of emails he received? 
1. What must he do to be capable of carrying out all of the operations above?



## Question 2
A group of n people would like to use a public key encryption system to exchange confidential information pairwise. That is each person should be able to communicate privately with each other person in the group, without anyone else being able to read the message.

1. Bob would like to send Alice encrypted and signed information. They are both members of the group. What keys must Bob use to achieve this?
1. Name a well-known asymmetric encryption system, explain how it works The group has decided to use a hybrid system – using a combination of asymmetric and symmetric encryption.
1. Why might the group have decided to do this?

## Question 3
Demonstrate how RSA generates keys using p=2, q=7.

## Question 4
Your friend Miriam (who lives next door) has decided she’d like to share a file with you, but only with you. She’s decided to encrypt the file before sending it to you.

1. What type of encryption (symmetric or asymmetric) should she use? Given your choice, propose a specific algorithm and explain to her on a high level how it works. 
1. Miriam doesn’t know how Diffie-Hellman relates to public key encryption, explain how they are related.

## Question 5
Design a cipher which uses a Fiestel structure. Note it need not meet the formal requirements of a secure cipher.

