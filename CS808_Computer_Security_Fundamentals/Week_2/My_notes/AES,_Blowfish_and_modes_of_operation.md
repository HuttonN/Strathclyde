# AES, Blowfish and modes of operation

In this section we will be looking at two modern block ciphers:
* Blowfish
* Advanced Encryption Standard

We will also look at how block ciphers actually operate on a set of data, which can be referred to as its mode of operation.

## AES and Blowfish (to do!)

## Modes of Operation

Thus far, we have primarily been working on the basis of encrypting one block at a time and then move on. However, this can impact the security because you can start to recognise patterns in the data. There are a number of different types of modes of operation but we'll look at two:

### Electronic Code Book (ECB)

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

### Cipher Block Chaining (CBC)

![Cipher block chaining](./images/Cipher_block_chain.png)

In CBC the process is as follows:
* the plain text is divided into fixed size blocks, say $b$ bits a piece
* the first block of plain text is XORed with an initialisation vector (a pseudo-random number generated value)
* this is then input to the encryption function to produce the first cipher text block
* the next plain text block is XORed with the previous ciphertext block and input to the encryption function to produce the next cipher text block.
* This process is then repeated for each subsequent plain text block.