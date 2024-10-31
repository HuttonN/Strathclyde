# Cryptography Overview questions

## Cryptographic Primitives

&nbsp;
<details>
<summary>
1. What is meant by a cryptographic primitive
</summary>

* A cryptographic primitive can be considered a generic building block of cryptography. 
* Cryptographic primitives are a low level constructs which are used together to build larger cryptographic protocols.
* A cryptographic hash function can be referred to as a cryptographic primitive.
 
</details>

## Cryptography Hash Definition

&nbsp;
<details>
<summary>
1. What does a cryptographic hash function do
</summary>
A cryptographic hash function takes data of an arbitrary length, and produces a fixed length string of alphanumeric characters which represents that data. 
</details>

&nbsp;

<details>
<summary>
2. What is the output referred to
</summary>
The output can be called a hash value or a digest
</details>

&nbsp;

<details>
<summary>
3. State two hash function standards
</summary>

* MD5: considered insecure for modern practical use
* SHA-256: commonly used in modern practice

</details>

## Secure Properties of Cryptographic Hashes

&nbsp;

<details>
<summary>
1. State the properties of cryptographic hash functions
</summary>

* ***Deterministic:*** The same input using the same hash function always provides the same hash value. This is true for all hash functions, but the following properties are for cryptographic hashes only.
* ***Pre-image resistant:*** This means that given a random output, it is computationally infeasible to determine the input from the hash value alone. For any given code $h$, it is computationally infeasible to find $x$ such that $H(x)=h$. This effectively is a one-way function.

![Pre-image resistant](./images/Pre-image_resistant.png)
* ***Second pre-image resistant:*** Given a hash value $h_{1}$ it should be computationally infeasible to find a different input message which results in the same hash value $h_{1}$
![Second pre-image resistant](./images/Second_pre-image_resistant.png)
* ***Collision resistant:*** It should not be feasible to produce two inputs which have the same hash value as output. It should be computationally infeasible to find any pair $(x, y)$ such that $H(x) =H(y)$.
![Collision resistant](./images/Collision_resistant.png)

</details>

<details>
<summary>
2. Explain the distinction between second pre-image resistance and collision resistance
</summary>

* In second pre-image resistance you have a given input which it is impossible to find another value which hashes to the same output. 
* For collision resistance, you have no such input and are simply trying to determine two inputs which produce the same hash value.

</details>

## Purpose of Cryptographic Hash Functions

&nbsp;
<details>
<summary>
1. Using an example, describe the purpose of cryptograpic hash functions
</summary>

You locate software you wish to download and install from a trusted secure website. On the website you are provided with a link to download the software and a hash value, as well as the specific hash function used to calculate that value. If you then independently calculate the hash value of the file downloaded using that function, and this matches the hash value provided on the website then you have confidence in the integrity of the file. If it were changed, e.g. by an attacker, then the hash value would not match and you would not install the software.

</details>

## Limitations

&nbsp;
<details>
<summary>
1. Describe limitations of cryptographic hash functions
</summary>

1. Very small messages or predictable messages cannot be meaningfully hashed. For example, a single bit cannot be meaningfully hashed as any attacker could easily compute the input to result in the hash value.
1. You must trust origin of hash function in order for it to provide integrity, e.g. on a website providing software you would need to be confident of a secure channel which provides the hash value

</details>