# Block Ciphers

In a block cipher, we take a block of data and encrypt that or decrypt that before moving on to the next block. This is in contrast to a stream cipher, where we take each bit per bit or each byte per byte. In terms of block size, typically, we're looking at 128 to 156 and so on and so forth. So we're taking a set of bits, working on that before moving on. 

There are a number of different operations which can be completed within a block cipher. A very basic example is shown below.

![Basic block cipher](./images/Basic_block_cipher.png)

For each block of data we:
1. Split in two
1. Switch halves 
1. Do XOR with key

## Padding

In the previous the length of the message happened to be a multiple of the key length. That's very unlikely to be the case in real world applications. To get around this we look at a primitive (fundamental operation defined withing cryptography) called padding. Padding is the process of expanding the length of a message to ensure that it's a multiple of the key. There are a range of different standards which can be used to achieve this.

A simple example standard based on the cryptographic message syntax is shown here. 

![Padding](./images/Padding.png)

In this example, what we're doing is we're figuring out effectively what the remainder is upon division by the key size. So if we have, for example, a key size of 12 and a message of length 8, then we've got 4 bytes left over. So we need to pad that up by another 4 bytes. So what we do there is we replicate that number in bytes for four different bytes. This isn't necessarily the best example in terms of real-world use. So if you are applying this in modern use, you'd want to make sure what the context is within your workplace to identify an appropriate padding algorithm. In saying that, it is a nice, easy example to give you a flavour for what that could be.

Caveat: The above form of padding with a short message can potentially lead to a Bleichenbacher attack (LOOK UP!)

---

Next: [Feistel Structures](Feistel_Structures.md)