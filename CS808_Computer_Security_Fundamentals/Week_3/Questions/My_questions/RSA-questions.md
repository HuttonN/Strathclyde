# RSA questions

## Introduction

&nbsp;
<details>
<summary>
1. What is RSA used for
</summary>

This is used in modern cryptography in tools such as VPNs.
</details>

## Key generation

### The Algorithm

&nbsp;
<details>
<summary>
1. Describe the algorithm for key generation
</summary>

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
    
$d$ is then the private key in combination with $n$. It is computationally infeasible to compute $d$ from $e$ and $n$ alone.

</details>

### Example

&nbsp;
<details>
<summary>
1. Work through a key generation example
</summary>

1. Select two distinct primes:
    * $p=5$, $q=11$.
1. Calculate $n$:
    * $n=p×q=5×11=55$.
    * $n=55$ will be part of both the public and private keys.
1. Calculate Euler’s function $\phi(n)$:
    * $\phi(n) = (p−1)×(q−1)=(5−1)×(11−1)=4×10=40$.
1. Choose $e$:
    * $e$ must satistfy $ 1 < e < \phi (n)$ and $\gcd (e, \phi(n)) = 1$
    * Let $e=7$ (which satisfies the conditions)
1. Calculate $d$:
    * $d$ is the modular inverse of $e$ modulo $\phi (n)$
    * $d$ satisfies $e \times d \equiv 1 \mod \phi (n)$
    * Solve $7 \times d \equiv 1 \mod 40$
    * $d=23$ (as $7\times 23 = 161$, and $161 \mod 40 =1$)
1. We then have the following key pair:
    * **Public Key:** $(e,n) = (7,55)$.
    * **Private Key:** $(d,n) = (23,55)$.
</details>

## Encryption and Decryption

### Encryption

&nbsp;
<details>
<summary>
1. Describe how a message is encrypted
</summary>

1. Split the message into blocks:
    * For simplicity, let’s encrypt a single letter: $B$.
    * Assign $B=2$ (its position in the alphabet).
1. Apply the encryption formula:
    * $C = M^{e}\mod n$, where $M$ is the plaintext block
    * $C = 2^{7}\mod 55$
    * Calculate: $2^{7} = 128$, and $128 \mod 55 =18$
1. Ciphertext:
    * $C=18$.
</details>

### Decryption

&nbsp;
<details>
<summary>
1. Describe how a message is decrypted
</summary>

1. Apply the decryption formula:
    * $M = C^{d}\mod n$, where $C$ is the ciphertext block
    * $M = 18^{23}\mod 55$
    * Simplify using modular arithmetic:
        * $18^{23}\mod 55 \equiv 2$ (restoring the original plaintext $M=2$).
1. Plaintext:
    * Decrypting $C=18$ yields $M=2$, which corresponds to $B$.
</details>