# Further Cryptography

## Public Key Cryptography and Other Applications

### Diffie-Hellman Key Exchange

When looking at symmetric encryption and decryption, we've yet to answer a crucial question: How do both parties share a key in a secure manner? This could be done physically but often this won't be practical. What we need is a key exchange algorithm.

The Diffie-Hellman key exchange algorithm provides a way of generating a shared secret key over an insecure channel, which can then be used to encrypt future communications. The use of mathematics allows two parties to generate a shared secret in such a way that even if an interceptor or attacker observes the information exchanged, they would not be able to derive the shared key.

#### With colours

Lets first look at the algorithm at a high level using colours.

* Alice and Bob each pick a private colour. At no point do either send these private colours over the public communicationj channel (Eve can't see).
* A public colour is agreed upon. Eve can access the public colour at any point, as can Alice and Bob.
* Both Alice and Bob combine the public colour with their own private colours. This results in private colours that can't be seperated into their component colours. Even though Eve has access to the public colour it is computationally infeasible to try an extract what Alice or Bob's private colours were.
* Alice and Bob share the colours consisting of their own private colour and the public colour with each other.
* Each then adds their own private colour to end up with their shared secret key consisting of
    * Alice's colour
    * Bob's colour
    * The public colour
* We need part of a secret to generate that final key but Eve is never going to be able to access either one of those from the information that she has available to her

This process is summarised in the following:

![Diffie-Hellman colours](./images/Diffie_Hellman_colours.webp)

#### With mathematics

We now revisit Diffie-Hellman with numbers:

![Diffie-Hellman numbers](./images/Diffie_Hellman_numbers.png)


* In terms of the publicly agreed information, we have two values:
    * A large prime key $p$. The larger it is the harder it is for an attacker to perform a brute-force attack or solve the discrete logarithm problem.
    * A number $g$, typically chosen such that it generate all the elements of the group $modulo$ $p$ except $0$.
* Alice and Bob define their own private integers, $a$ and $b$, which are less than $p$ and are never communicated across the public channel.
* Alice calculates $A = g^{a} \mod p$ and Bob calculates $B = g^{b}\mod p$ and communicate these over the insecure channel. Knowing $p$ and $g$, it is still computationally infeasible for Eve to be able to figure out be private integers $a$ and $b$.
* Alice and Bob can then calculate the shared key by raising $B$ to the power of $a$ and $A$ to the power of $b$ respectively:

$$B^{a} = (g^{b})^{a} \mod p = (g^{a})^{b} \mod = A^{b}$$

* Even though Eve has access to $A$, $B$, and $g$ she's unable to derive the final secret key and doesn't have access to $a$ or $b$.

### Introducing Public Key Cryptography

Recall the key distribution problem, that is the issue of trying to agree a shared key over an insecure channel. This can be solved by key exchange algorithms such as Diffie-Hellman. Alternatively, we can use public key cryptography, sometimes known as asymmetric cryptography.

In this approach a key pair is generated for each entity (such as an individual):

* a private key, which is kept only by the entity
* a public key, which can be shared without compromising security

This key pair is mathematically linked in such a way that data encrypted with the private key can only be decrypted by its corresponding public key and vice versa. It is also computationally infeasible to derive the private key from the publc key and vice versa.

In order to communicate securely with another entity, Bob say, we would need to encrypt the message using Bob's public key. Only Bob will then be able to decrypt this, as Bob is the only person with access to the corresponding private key.

Public key cryptography can also provide some confidence in authenticity. Fo example, if Bob wants to share information with Alice and provide Alice assurance it comes from Bob then Bob should encrypt the message using his private key. This will not provide confidentiality, but the public key for Bob is the only key which can decrypt this. Thus, if Alice can successfully decrypt using the public key for Bob then there is some assurance the message comes from Bob. In practical use, there are further steps to ensure the integrity of the message which we will come back to. Clearly if Bob's private key was compromised this would be problematic, and the above is more for demonstration.

There are a few things to highlight about public and private key pairs:

* Whilst the natural assumption is that an entity would have only one public and private key pair, the reality is that there mau be multiple key pairs for a single entity. Some of these key pairs may also be ephemeral, that is they are for temporary use e.g. a single communication session over the internet.
* Another point to note is that sometimes keys may be compromised (e.g. if stored on a server which is compromised) or otherwise lost. In such a situation the entity who owns the key pair needs to revoke their public key and generate a new key pair.

### RSA

In this section we'll look at the RSA algorithm, a modern example of public key cryptography. This is used in modern cryptography in tools such as VPNs. The details of the algorithm are below. Note: there have been variations on the RSA algorithm, but we will look at the one originally published.

* Identify two large, distinct primes, $p$ and $q$.
* Calculate the product $n=pq$. As discussed before, it is then very difficult to prise apart the individual values of $p$ and $q$ from the final product as long as $p$ and $q$ are sufficiently large.
* Calculate Euler's function, $\phi (n)$, which is the number of integers $k$ such that:

$$1 \leq k \leq n \textrm{ and } \gcd(k,n) = 1$$

That is, the number of positive integers up to $n$ which are coprime with $n$. Coprime means that the largest common divisor is $1$. For two primes, $p$ and $q$, Euler's function becomes

$$ \phi (n) = (p-1)(q-1)$$

* Next, we select an integer $e$ that satisfies the following:
    * $ 1 < e < \phi (n)$
    * $\gcd (e, \phi(n)) = 1$

$e$ is selected as the public key and it is the combination of $e$ with the value of $n$ which is public.
* We then calculate $d$, the modular inverse of $e$ modulo $\phi (n)$. This means d satisfies:

$$e \times d \mod \phi (n) =1$$

$d$ is then the private key in combination with $n$. 

ADD NOTES ON EXAMPLE

### Crptographic randomness and one-time pads

#### Randomness

Randomness, or more specifically random numbers, are an important aspect of cryptography. To be truly random means that there is no way to predict an event, such as a number series. This means that there are no discernible patterns. To identify a truly random number is to pick a number from a set, where each number is equally probable.

In cryptography, pseudo-random number are used. Pseudo random number generators (PRNG) are algorithms which produce a series of numbers which appear random. To do so, they make use of an initial seed value, a number which starts the generation of subsequent values. This seed should only be shared with those who require the ability to replicate the series, and where used in cryptography the seed is normally truly random. This is helpful in situations where you may be required to provide the sequence at another time. For example, PRNGs are used in simulation of viruses. Where PRNGs are used in cryptography you may see this as being referred to as Cryptographically Secure Pseudo Random Number Generators (CSPRNG). CSPRNGs have additional requirements which we won't discuss here but it is sufficient to note that they shoul be indistinguishable from true randomness.

CSPRNGs can be sufficiently random to prevent attacks, but their deterministic nature means it can be used for encryption or other situation where you may be required to duplicate the values. It is also more efficient than trying to get a suitable list of truly random numbers.

#### One Time Pad

A one-time pad is where a truly random key stream is used to encrypt the message. Each character (e.g. letter or bit or byte) is combined with a character from the key stream. 

As an example, consider a simple shift cipher where letters are shifted along by the key value in the corresponding position, looping back to the start of the alphabet. Assume the key provided below is truly random:

![One-time pad example](./images/One_time_pad.png)

To be classified as a one-time pad (OTP), a key must meet the following requirements:
* it is truly random
* only two copies should exist - one for encryption, one for decryption
* it is one use only, and destroyed after use
* it is at least as long as the plaintext

Provided they are properly implemented, OTPs provide "perfect secrecy". No matter how much computational power you have, you can do no better than guessing randomly what the original message is.

Of course, there are the practical difficulties of efficiently obtaining a sufficiently long random key and sharing the key.

With very short examples like that above, you would be able to guess all the possibilities fairly easily, so there are always limitations.

As an example, lets look at the middle squared method which was developed by Von Neumann. The process is as follows:
* Takes the seed
* square it
* line it up in the middle
* extract the middle part

This gives the next values which can then be used to repeat the process. If the number doesn't have an even number of digits it can be padded. Eventually, the numbers will repeat but it could take a very long time. The point at which numbers begin to repeat in a PRNG is called the PRNG. There are some PRNGs that are so long that they don't have any practical implications

## Digital signitures

Digital signitures give is a digital equivalent to a handwritten signature, but they're better. Whereas a handwritten signiture can easily be forged, a well-designed and implemented digital signature cannot. A digital gives us some assurance in terms of the integrity of the message, as well as some origin authentication.

Lets have a high-level look at how they work:
* We have the following elements:
    * a private key, $s$, that's used for signing.
    * a public key, $v$, used for verification.
    * a message that we would like to send, and prove that it's us that wrote it, and that it hasn't been tampered with
* What we can do is take the message and apply our private key to encrypt it, and send the message and our private key.
* What the recipient can do is apply the public key to the message and compare to the 

## End-To-End Encryption
