# Block Ciphers questions

## Introduction

&nbsp;
<details>
<summary>
1. Describe the process when working with a block cipher
</summary>

In a block cipher, we take a block of data and encrypt that or decrypt that before moving on to the next block.
 
</details>

&nbsp;

<details>
<summary>
2. How does this contrast with stream ciphers
</summary>
In a stream cipher, we take each bit per bit or each byte per byte, instead of looking at blocks
</details>

&nbsp;

<details>
<summary>
3. What is a typical block size
</summary>
In terms of block size, typically, we're looking at 128 to 256 bit
</details>

&nbsp;

<details>
<summary>
4. Describe a basic example illustrating the operations which can be completed in a block cipher
</summary>

![Basic block cipher](./images/Basic_block_cipher.png)

For each block of data we:
1. Split in two
1. Switch halves 
1. Do XOR with key
</details>

## Padding

&nbsp;
<details>
<summary>
1. What about the previous example is unlikely to occur in practice
</summary>
The length of the message happened to be a multiple of the key length. That's very unlikely to be the case in real world applications.
</details>

&nbsp;

<details>
<summary>
2. How do we get round this?
</summary>
To get around this we look at a primitive (fundamental operation defined within cryptography) called padding. Padding is the process of expanding the length of a message to ensure that it's a multiple of the key. There are a range of different standards which can be used to achieve this.
</details>

&nbsp;

<details>
<summary>
3. Descibe an example standard
</summary>

A simple example standard based on the cryptographic message syntax is shown here. 

![Padding](./images/Padding.png)

In this example, what we're doing is we're figuring out effectively what the remainder is upon division by the key size. So if we have, for example, a key size of 12 and a message of length 8, then we've got 4 bytes left over. So we need to pad that up by another 4 bytes. So what we do there is we replicate that number in bytes for four different bytes.

</details>

&nbsp;

<details>
<summary>
4. What kind of attack is the above form of padding vulnerable to?
</summary>

The above form of padding with a short message can potentially lead to a Bleichenbacher attack

</details>