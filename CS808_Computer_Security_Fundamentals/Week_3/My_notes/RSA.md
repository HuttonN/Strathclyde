# RSA

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