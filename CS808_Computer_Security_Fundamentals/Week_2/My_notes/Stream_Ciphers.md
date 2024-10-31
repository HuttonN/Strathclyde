# Stream Ciphers

A stream cipher effectively works with a stream of data. This could be a stream of bits or a stream of bytes. 

The most simple example that I give is to work with the bitwise operations. So for example, an exclusive OR (XOR) operation. In this example, we would take each bit of the plaintext, in turn, and perform an XOR operation with the corresponding key bit. An example is as follows:

![Stream cipher](./images/Stream_cipher.png)

For decryption in this particular example, we would repeat the same process. Effectively, we need to XOR the ciphertext with the key which is repeated once more, and the resulting output would be the plaintext.

---

Next: [Block Ciphers](Week_2/My_notes/Block_Ciphers.md)