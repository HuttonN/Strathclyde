# Substitution Ciphers

In this section we'll look at substituions and permutations through the lens of traditional cryptography.

## Caeser cipher

Very simple cipher where each letter is shifted along the alphabet. An example using a key of 3 is shown below:

![Caeser cipher](./images/Caeser_cipher.png)

A is shifted to D, B to E, and so on until we reach X which is then sent back to A.

So as you can see, substitution is simply a case of taking a letter or component within your plain text and substituting it with a different value. In this instance, we're mapping letters to letters. But it could also relate to ones and zeros or bytes or even a longer set of bits. But we don't need to use just the one cipher alphabet. We can actually expand that and use a range of different possible cipher alphabets. 

## Vigenere Cipher

The Vigenere cipher makes use of the Caesar cipher except with the whole range of possible shifted values. So it starts off with a shift of 0, shift of 1, and goes further down until you get to the maximum shift of 25. Traditionally, this is done using a Vigenre cipher grid, as you can see here. 

![Vigenere grid](./images/Vigenere_grid.png)

Within the Vigenre cipher, we pick a key which doesn't have any repeated letters. And we then place that key above every letter within our plaintext. Repeat that key as needed over the plaintext. And we then use that to evaluate which alphabet we should be using in order to encrypt. 

For example, say we use a keyword of ALICE and we want to encrypt the plaintext HELLO. Placing ALICE above HELLO we take the keyword value above each letter and look up our grid to get the correct ciphertext. Above H is A so we look up where row A intersect column H and we get H. Above E is L so we look up where the row L intersect the column E to obtain P. Repeating this process we finally obtain the ciphertext HPTNS.

Another way of looking at the Vigenre cipher is to translate every letter into a position number. 

![Vigenere cipher](./images/Vigenere_cipher.png)

So A would be 0 through to 25. We can then translate any letter, whether that's in our plain text or whether that's in the key. And then, perform the addition for those. And the resulting value, obviously, it needs to be calculated mod 25. But the resulting output can then be translated back from a number into the corresponding letter. 

This is slightly easier if you ever want to implement this in code, for example. But often, that visual representation of the Vigenre square can be helpful in wrapping your head around what's happening. 

## Permutations

Permutations, as the name suggests, is basically moving components around.

One such example is the Rail-fence cipher. In this cipher we take every second letter and move it down to the line beneath that one. So if we look at hello world, on the top line, we end up with H, L, O, O, L. And then, the second line we've got E, L, W, R, D. 

![Raile-fence cipher](./images/Rail_fence_cipher.png)

The idea then is that you put the second line after the first line. So effectively, you end up with an anagram at the bottom there.

---

Next: [Stream Ciphers](Stream_Ciphers.md)