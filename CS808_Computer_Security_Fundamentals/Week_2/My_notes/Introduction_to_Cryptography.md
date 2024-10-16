# Introduction to Cryptography



## Cryptography Fundamentals

### Cryptography Overview

A cipher is effectively an algorithm which allows us to send a message across an insecure network in a secure fashion. It means that if anyone were to intercept that message, they would be unable to read the contents of that message.

#### Cryptography components

![Cryptography components](./images/Cryptography_components.png)

There are three components:

* **Plain text:** The unencrypted message. This is a message that if anyone were to intercept that, they would be able to read it irrespective of whether they have access to the key or not
* **Key:** The key itself is the thing that allows us to apply the encryption. It's the
secret information that allows us to encrypt and potentially decrypt that information as well.
* **Ciphertext:** The bottom line here shows the ciphertext. Ciphertext is the result of applying encryption to the plain text using the key.

The intention here is that if someone was to send a message over an insecure network, anyone intercepting that would not be able to read that message without the key.

#### Sending messages

Three of the key names that you might hear in relation to cryptography
include Alice, Bob, and Eve. 

![Sending messages](./images/Alice_Bob_Eve.png)

These are just traditional labels used to represent intended recipients, and the sender, as
well as someone trying to intercept that message. So Alice is sending a message, Bob is
receiving it or vice versa, and Eve is trying to intercept that message.

#### Cryptography Process

The overall process when it comes to ciphers is that we take our plaintext and we can apply our encryption algorithm using the key and that results in our ciphertext. And then we can perform the reverse, the decryption. We apply the decryption key to the ciphertext to get the plain text out.

The example that we have here, the key is basically a substitution where we're taking every letter in English alphabet and translating that into a little diagram or figure if you like. 

![Cryptography process](./images/Cryptography_process.png)

When we're looking at ciphers, there's two general classifications that you might come across:

* **Symmetric cryptography:** Within symmetric cryptography, we've got the same key for encryption as we do for decryption
* **Asymmetric cryptography:** Within asymmetric cryptography, we have a different key

### Cryptographic Hash Functions

#### Cryptographic Primitives

Before we consider what a cryptographic hash is, it is helpful to note that a cryptographic hash function can be referred to as a cryptographic primitive. A cryptographic primitive can be considered a generic building block of cryptography. Cryptographic primitives are a low level constructs which are used together to build larger cryptographic protocols.

#### Cryptographic Hash Definition

A cryptographic hash function takes data of an arbitrary length, and produces a fixed length string of alphanumeric characters which represents that data. The output can be called a hash value or a digest. I primarily refer to this as a hash value, but you may come across other sources which use the term digest.

There are a number of hash function standards such as SHA-256 and MD5. Note that MD5 is considered insecure for modern practical use, but is commonly used as an example. SHA-256 is commonly used in modern practice.

If calculating the SHA-256 hash of the following string “this is an arbitrary length string” then you should get the hash value:

018D17D6672278F09D99C87B882A4D0AC00CB7322A471BFAA49C6E32C71937E0

#### Secure Properties of Cryptographic Hashes

A cryptographic hash function has a number of properties, most notably the following:

* ***Deterministic:*** The same input using the same hash function always provides the same hash value. This is true for all hash functions, but the following properties are for cryptographic hashes only.
* ***Pre-image resistant:*** This means that given a random output, it is computationally infeasible to determine the input from the hash value alone. For any given code $h$, it is computationally infeasible to find $x$ such that $H(x)=h$. This effectively is a one-way function.

![Pre-image resistant](./images/Pre-image_resistant.png)
* ***Second pre-image resistant:*** Given a hash value $h_{1}$ it should be computationally infeasible to find a different input message which results in the same hash value $h_{1}$
![Second pre-image resistant](./images/Second_pre-image_resistant.png)
* ***Collision resistant:*** It should not be feasible to produce two inputs which have the same hash value as output. It should be computationally infeasible to find any pair $(x, y)$ such that $H(x) =H(y)$.
![Collision resistant](./images/Collision_resistant.png)

Note the distinction between second pre-image resistance and collision resistance is that in second pre-image resistance you have a given input which it is impossible to find another value which hashes to the same output. For collision resistance, you have no such input and are simply trying to determine two inputs which produce the same hash value.

#### Purpose of Cryptographic Hash Functions

You may be wondering the purpose of cryptographic hash functions. Consider an example as follows, you locate software you wish to download and install from a trusted secure website. On the website you are provided with a link to download the software and a hash value, as well as the specific hash function used to calculate that value. If you then independently calculate the hash value of the file downloaded using that function, and this matches the hash value provided on the website then you have confidence in the integrity of the file. If it were changed, e.g. by an attacker, then the hash value would not match and you would not install the software.

#### Limitations

There are some limitations of cryptographic hash functions:
1. Very small messages or predictable messages cannot be meaningfully hashed. For example, a single bit cannot be meaningfully hashed as any attacker could easily compute the input to result in the hash value.
1. You must trust origin of hash function in order for it to provide integrity, e.g. on a website providing software you would need to be confident of a
secure channel which provides the hash value

### Substitution Ciphers

In this section we'll look at substituions and permutations through the lens of traditional cryptography.

#### Caeser cipher

Very simple cipher where each letter is shifted along the alphabet. An example using a key of 3 is shown below:

![Caeser cipher](./images/Caeser_cipher.png)

A is shifted to D, B to E, and so on until we reach X which is then sent back to A.

So as you can see, substitution is simply a case of taking a letter or component within your plain text and substituting it with a different value. In this instance, we're mapping letters to letters. But it could also relate to ones and zeros or bytes or even a longer set of bits. But we don't need to use just the one cipher alphabet. We can actually expand that and use a range of different possible cipher alphabets. 

#### Vigenere Cipher

The Vigenere cipher makes use of the Caesar cipher except with the whole range of possible
shifted values. So it starts off with a shift of 0, shift of 1, and goes further down until you get to the maximum shift of 25. Traditionally, this is done using a Vigenre cipher grid, as you can see here. 

![Vigenere grid](./images/Vigenere_grid.png)

Within the Vigenre cipher, we pick a key which doesn't have any repeated letters. And we then place that key above every letter within our plaintext. Repeat that key as needed over the plaintext. And we then use that to evaluate which alphabet we should be using in order to encrypt. 

For example, say we use a keyword of ALICE and we want to encrypt the plaintext HELLO. Placing ALICE above HELLO we take the keyword value above each letter and look up our grid to get the correct ciphertext. Above H is A so we look up where row A intersect column H and we get H. Above E is L so we look up where the row L intersect the column E to obtain P. Repeating this process we finally obtain the ciphertext HPTNS.

Another way of looking at the Vigenre cipher is to translate every letter and into a position number. 

![Vigenere cipher](./images/Vigenere_cipher.png)

So A would be 0 through to 25. We can then translate any letter, whether that's in our plain text or whether that's in the key. And then, perform the addition for those. And the resulting value, obviously, it needs to be calculated mod 25. But the resulting output can then be translated back from a number into the corresponding letter. 

This is slightly easier if you ever want to implement this in code, for example. But often, that visual representation of the Vigenre square can be helpful in wrapping your head around what's happening. 

### Permutations

Permutations, as the name suggests, is basically moving components around.

One such example is the Rail-fence cipher. In this cipher we take every second letter and move it down to the line beneath that one. So if we look at hello world, on the top line, we end up with H, L, O, O, L. And then, the second line we've got E, L, W, R, D. 

![Raile-fence cipher](./images/Rail_fence_cipher.png)

The idea then is that you put the second line after the first line. So effectively, you end up with an anagram at the bottom there.

## Modern Cryptography Structures

### Stream Ciphers

A stream cipher effectively works with a stream of data. This could be a stream of bits or a stream of bytes. 

The most simple example that I give is to work with the bitwise operations. So for example, an exclusive OR (XOR) operation. In this example, we would take each bit of the plaintext, in turn, and perform an XOR operation with the corresponding key bit. An example is as follows:

![Stream cipher](./images/Stream_cipher.png)

For decryption in this particular example, we would repeat the same process. Effectively, we need to XOR the ciphertext with the key which is repeated once more, and the resulting output would be the plaintext.

### Block Ciphers

In a block cipher, we take a block of data and encrypt that or decrypt that before moving on to the next block. This is in contrast to a stream cipher, where we take each bit per bit or each byte per byte. In terms of block size, typically, we're looking at 128 to 156 and so on and so forth. So we're taking a set of bits, working on that before moving on. 

There are a number of different operations which can be completed within a block cipher. A very basic example is shown below.

![Basic block cipher](./images/Basic_block_cipher.png)

For each block of data we:
1. Split in two
1. Switch halves 
1. Do XOR with key

#### Padding

In the previous the length of the message happened to be a multiple of the key length. That's very unlikely to be the case in real world applications. To get around this we look at a primitive (fundamental operation defined withing cryptography) called padding. Padding is the process of expanding the length of a message to ensure that it's a multiple of the key. There are a range of different standards which can be used to achieve this.

A simple example standard based on the cryptographic message syntax is shown here. 

![Padding](./images/Padding.png)

In this example, what we're doing is we're figuring out effectively what the remainder is upon division by the key size. So if we have, for example, a key size of 12 and a message of length 8, then we've got 4 bytes left over. So we need to pad that up by another 4 bytes. So what we do there is we replicate that number in bytes for four different bytes. This isn't necessarily the best example in terms of real-world use. So if you are applying this in modern use, you'd want to make sure what the context is within your workplace to identify an appropriate padding algorithm. In saying that, it is a nice, easy example to give you a flavour for what that could be.

Caveat: The above form of padding with a short message can potentially lead to a Bleichenbacher attack (LOOK UP!)

### Feistal Ciphers

The below is referred to as a Feistal structure:

![Feistal structure](./images/Feistal_structure.png)

We start off with a plaintext block and split into two halves. We will assume that the two halves are even but there are Feistal structures that work with uneven halves.

TO FINISH!!!

### Components of modern block ciphers

In this section we will look at three of the key components of a modern block symmetric cipher:
* substitution boxes
* permutation boxes
* key schedules

#### Substitution boxes

Substitution or s-boxes effectively allows us to take a block of data and replace it with a different block of data. This can be implemented in a number of different ways. One of the common ways of doing this is through a lookup table where we are given a particular position and take the value at that position to replace the original value.

Lets look at an example. This example has been taken from the Data Encryption Standard. This was defined in the '70s by the National Institute of Standards and Technology. However, it is not suitable for modern use, but does provide a practical example that's easy for us to see how it can work.

![S Box Example](./images/S_Box_Example.png)

* We take an input consisting of 6 bits: $101001$
* We take the middle $4$ bits, $0100$, to determine the column
* We take the $2$ outer bits, $11$, to determine the row
* We then find the intersection of our row and column to determine our output: $0100$.

#### Permutation boxes

In a permutation or P-box, bits can be rearranged, repeated, and possibly discarded, but not changed. It could be said that this is a subclass of an S-box, but this doesn't go the other way around. That is, an S-box cannot be a P-box but a P-box could be classified as an S-box.

##### Types of P-box

There are three types of P-box:
* ***Straight P-box:*** just transposes the digits, the $1$'s and $0$'s.
![Straight P Box Example](./images/Straight_P_Box.png)
In this example, we take the first bit and the last bit, and reposition those so that they are swapping. So we'll take bit $1$, swap it with bit $6$, and vise versa. We'll take bit $2$, $3$, $4$, and $5$, and keep those static. This then provides the output at the bottom of our permutation box, where we can see that these have been reordered appropriately. Bits $1$ and $6$ swap places, and $2$, $3$, $4$, and $5$ remained static.
* ***Compression P-box:*** discards some of the bits
![Compression P Box Example](./images/Compression_P_Box.png)
* ***Expansion P-box:*** basically takes particular elements within a block and repeats the values
![Expansion P Box Example](./images/Expansion_P_Box.png)

##### Diffusion and confusion

S-boxes and P-boxes provide two important properties of a secure cipher: confusion and diffusion. Modern cryptography attempts to achieve both of these for a secure cipher. 

* confusion: each bit of the ciphertext is dependent on multiple parts of the key. Effectively, we are obscuring the relationship between the key and the cipher. A substitution box helps us to achieve this property.
* diffusion: Diffusion, in contrast, means that if one bit of the plain text is changed, then that should impact many parts, in fact, at least half of the ciphertext bits. This is where the permutation block comes in.

It's the combination of these two aspects which help us define a secure cipher.

#### Key schedules

In modern symmetric block ciphers, we often repeat a series of steps multiple times. These are referred to as rounds. Within each round a subkey is used. This can also be referred to a round key. Sub keys, or round keys, are keys which are derived from the original key, adding further complexity to the cipher. In order to determine what the round keys are, we have to define an algorithm called a ***key schedule***. This algorithm allows us to take a key which is normally at least 128 bits in length and use it to generate these round keys.

![Key schedule](./images/Key_schedule.png)

Doing this achieves a similar goal to the Vigenere cipher, which had multiple cipher alphabets. In this instance, we're generating multiple keys from the original, so as to help hide the relationship between the plaintext and the ciphertext even further. 

In the past, key schedules have been based primarily on relatively straightforward permutations and substitutions. However, in more recent cryptography, we're looking at more complex ways of generating a key schedule. However, we won't go into that in particular depth here. It's just important to recognise that a single key can be used to generate round keys.

### AES, Blowfish and modes of operation

In this section we will be looking at two modern block ciphers:
* Blowfish
* Advanced Encryption Standard

We will also look at how block ciphers actually operate on a set of data, which can be referred to as its mode of operation.

#### AES and Blowfish (to do!)

#### Modes of Operation

Thus far, we have primarily been working on the basis of encrypting one block at a time and then move on. However, this can impact the security because you can start to recognise patterns in the data. There are a number of different types of modes of operation but we'll look at two:

##### Electronic Code Book (ECB)

![Electronic code book](./images/Electronic_code_book.png)

In ECB the process is as follows:
* the plain text is divided into fixed size blocks, say $b$ bits a piece
* each block is encrypted in isolation using the same key.
* if the message is longer than the block size, padding is applied to the last block as necessary

Note that if the length of the plain text is not a multiple of the block size, padding is added to the last block to make it a complete block.

There are some advantages and disadvatages to ECB.

***Advantages:***
* Easy to implement and conceptualise, making it attractive where ease of implementation and efficiency are desirable.
* It's resilient to the loss or corruption of individual blocks during transmission. Each ciphertext block is generated independently of other blocks, which mean that loss or corruption of one block does not leak into neighboring blocks.

***Disadvantages:***
* If the same $b$-bit block of plain text appears more than once in the message, it always produces the same ciphertext. Because of this, for lengthy messages, the ECB may not be secure. 
* If the message is highly structured it may be possible for a cryptanalyst to exploit these regularities. For example, if it is known that the message always starts out with certain predefined fields, then the cryptanalyst may have a number of known plaintext-ciphertext pairs to work with. 
* If the message has repetitive elements, with a period of repetition a multiple of $b$-bits, then these elements can be identified by the analyst.

##### Cipher Block Chaining (CBC)

![Cipher block chaining](./images/Cipher_block_chain.png)

In CBC the process is as follows:
* the plain text is divided into fixed size blocks, say $b$ bits a piece
* the first block of plain text is XORed with an initialisation vector (a pseudo-random number generated value)
* this is then input to the encryption function to produce the first cipher text block
* the next plain text block is XORed with the previous ciphertext block and input to the encryption function to produce the next cipher text block.
* This process is then repeated for each subsequent plain text block.