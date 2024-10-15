# Steganography

## Introduction

Steganography is the art of hiding information in plain sight.

It's a concept which has been around since ancient Greece. In Histories of Herodotus, we see an example where someone wanted to get a message to say that the Persians were going to invade. To do this they took a tablet and removed the wax from that tablet, engraved a message on the wood, and then covered it up with wax. This meant that if a soldier intercepted them and had a look at the tablet, they couldn't see that there was a message hidden there.

Steganography contrasts with cryptography:

* ***Steganography:*** Hiding data within ordinary files to avoid detection
* ***Cryptography:*** Message itself is not hidden, but is only readable with the correct key.

In modern day practice, steganography has obviously moved on. We make use of cover objects. These can include things such as digital images, which have quite a lot of redundant information. You'd be surprised at the amount of information that we can take away from a digital image and not perceive any differences with the naked eye. This makes a great cover object for steganography. There are a number of different algorithms which you can use to achieve this. But fundamentally, they take away that information which is unneeded by the human eye and replace it with the payload. 

So the general process for modern steganography is as follows:

![Steganography process](./images/Steganography_process.png)

* start with a cover object and payload (the information you want to hide)
* take the payload and hide within the cover object
* the resulting output is referred to as the stego object.

The whole idea behind this is that the stego mage should not be noticeably different from the original cover image.

## LSB Algorithm

### Digital representation of images

In this section we will look at a specific steganography algorithm - the least significant bit algorithm. This algorithm makes use of digital images specifically, but can be used with other cover objects.

Consider an uncompressed 24-bit image:

![Digital image](./images/Digital_image.png)

We have three different colour channels, with one byte representing each. That is eight bits representing a value of light related to red, green, and blue. So, an individual pixel is created from that byte of each of those different colour channels.

The least significant bit within a given byte is the right most bit as the change in the right-most bit will cause a minimal change to the naked eye. To see this, lets look at an example, taking a decimal representation of a byte. 

![Original byte](./images/Original_byte.png)

If we change the final bit from a $1$ to a $0$, then it's only going to change the actual value by $1$, because $2$ to the power of $0$ is 1.

![Change to least significant bit](./images/Change_in_least_significant_bit.png)

However, if we were to change the left-most, most significant bit, 

![Change to most significant bit](./images/Change_in_most_significant_bit.png)

it's going to change much more substantially

![Comparison of pixels](./images/Comparison_of_pixels.png)

### The Algorithm

As you might imagine, the LSB algorithm uses the benefit of the very minor adjustment discussed above.

* go the payload bit by bit
* For each bit of the payload, compare it to the least significant bit (LSB) of the current pixel (or byte) in the cover image
    * if the LSB of the cover image matches the current bit of the payload, leave it unchanged
    * if they do not match, flip the LSB (change from $0$ to $1$, or $1$ to $0$) so it matches the payload bit
* Move on to the next pixel/byte in the cover image and repeat the process:
    * Look at the LSB of each byte and compare it to the next bit of the payload.
    * Modify the LSB if it doesn't match the current bit of the payload.
* Continue iterating through the cover image until all bits of the payload have been embedded into the LSBs of the cover image.

Note: you are not always changing the LSB values, only when it doesn't match the payload

There are a few things that can trip people up when tring to implement the algorithm:

* You need to know when to stop extracting the hidden message from the cover image.
* When sending a message using a steganography program, it’s important to determine the point where the message ends and the rest of the cover image data starts.
* If you're hiding digital files (not just strings), you need to be aware of the file extension of the hidden data to handle it correctly after extraction.
* For a robust implementation, you must come up with a consistent way to ensure you can determine the end of the hidden message and any associated file metadata (such as the extension) before completing the program.

There are ways of completing the bit manipulation operations within different programming languages, e.g. in Java:

![Bit manipulation in Java](./images/Bit_manipulation_in_Java.png)

* First line:
    * 0x1 is the hexadecimal representation of the binary number 0000 0001, which is equivalent to 1
    * & is the bitwise AND operator. It compares each bit of two numbers and returns 1 if both bits are 1 and 0 otherwise.
    * When appyling & 0x1, you're effectively masking out all the bits except for the least significant bit of byt, and the result (lsb) will either by 0 or 1. depending on the least significant bit of byt.
* Second line:
    * ~ is the bitwise NOT operator which flips all the bits of a value
    * when ~ is applied to 0x1 (0000 0001) it flips the bits to give 1111 1110
    * &= applies a bitwise AND operation between byt and ~ 0x1, and assigns the result back to byt, changing the LSB of byt to 0, while leaving the other bits unchanged
* Third line:
    * | is the bitwise OR operator. It compares each bit of two values and return 1 if either of the corresponding bits is 1, or 0 if both bits are 0.
    * when | is applied to 0x1 (0000 0001) is affects only the LSB because 0x1 has all bits set to 0 except the LSB.
    * |= performs a bitwise 0R operator between byt and 0x1 and assigns the result back to byt, setting the LSB of byt to 1 regardless of the previous value. All other bits remain unchanged

The final three lines describe other operations which can be useful in implementing the algorithm in Java

### Issues with least significant bit

The straightforward LSB algorithm is very sequential in nature and can only be implemented in a certain number of ways. 

To try and sort this issue we can incorporate some form of randomness. Using random number generators, with some form of seed so it's pseudo-random and can be replicated if we have the seed value, to determine the next position in which to hide information.

TO DO: READ ARTICLE