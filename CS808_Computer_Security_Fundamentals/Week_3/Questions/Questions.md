# Cryptography Comprehension Questions

## Question 5

In your own words, explain how a digital signature mitigates an attack in which the attacker intercepts the communication from sender to recipient and replaces the document with their own document.

### Solution



## Question 6

You and a friend have public and private key pairs
1. How can you send secret messages to each other
1. What information security property could you achieve if you encrypted a message with your private key and released the cipher text?
1. How could you combine encryption using different keys to provide confidentiality and authenticity?

### Solution

1. Encrypt messages using the other's public key. Since they are the only ones with the private key only they can decrypt it
1. Authenticity
1. Sign the message using your private key to ensure authenticity and encrypt using the friend's public key.

# Cryptography Scenario-based Questions