# Question 1
## (a) What are the three typical authentication factors?
The three typical authentication factors are:
* Something you know: A piece of information only the user knows.
* Something you have: A physical object or device only the user possesses.
* Something you are: A unique biometric characteristic of the user.
## (b) Provide an example authentication mechanism for each factor:
Something you know: A password or PIN.
Something you have: A smart card, hardware token, or mobile device.
Something you are: A fingerprint scan, iris scan, or facial recognition.
## (c) A friend has said that there is a system they use in which they provide two passwords; they claim this is two-factor authentication. Are they correct?
No, they are not correct. Two passwords are considered two instances of the same factor ("something you know"). Two-factor authentication (2FA) requires that two different authentication factors be used, such as:

A password (something you know) and a fingerprint scan (something you are), or
A password (something you know) and a smart card (something you have).

# Question 2
## (a) Authentication systems do not typically store the password in the clear (i.e. in plain text). Why?
Storing passwords in plain text is highly insecure because:

If the system’s storage is compromised, attackers can directly obtain users' passwords, leading to account takeovers and data breaches.
Plain text storage violates best security practices, as passwords should be protected in case of a data breach.

## (b) Why are secure hashes used to store passwords and how are they used to help verify that a user has provided the correct password?
Secure hashes (e.g., SHA-256, bcrypt) are used to store passwords to ensure that:

Passwords are not stored in plain text.
When a user enters their password, the system hashes the provided password and compares the hash with the stored hash. If they match, the user is authenticated.
Since hashes are one-way functions, even if an attacker gains access to the stored hash, they cannot easily reverse the hash to get the original password.

## (c) Explain how a password salt decreases the likelihood of a successful dictionary attack.
A salt is a random value added to each password before hashing. It makes each password hash unique, even if two users have the same password. This prevents attacks like:

Dictionary attacks: Precomputed tables (rainbow tables) of common password hashes are ineffective because the attacker would have to recompute the tables for every possible salt value.
Without salting, an attacker could use a precomputed list of hash values (rainbow table) to quickly match hashed passwords to common passwords.

## (d) Why is it argued that information entropy is not a good measure of password security?
Information entropy measures the theoretical strength of a password based on its length and character set but doesn’t account for:

Human predictability: Users often choose predictable passwords (e.g., "password123"), which have lower real-world security even if their entropy seems high.
Common password patterns: Entropy assumes random selection, but many users choose non-random passwords (e.g., common words or phrases).

# Question 3
Password Policy Analysis:
The policy:

Minimum of 6 characters: While 6 characters is better than shorter lengths, it's generally considered too short for modern standards.
At least one uppercase letter: This increases the character set slightly but can encourage predictable patterns (e.g., capitalizing the first letter).
At least one number: This adds a bit more complexity but can lead to predictable patterns (e.g., adding "1" at the end).
No minor adjustments: This prevents users from making small changes to old passwords, which improves security.
Enforced monthly changes: Frequent password changes can be detrimental to usability and security because users may choose weaker, more predictable passwords they can remember.
Security:
Positive aspects: The requirements for mixed characters and numbers improve password strength and avoid easily guessable passwords.
Negative aspects: A minimum length of 6 characters and the frequent change policy may encourage users to create weak, easy-to-remember passwords (e.g., "Password1" and slight variations each month), reducing actual security.
Usability:
Negatives: The monthly change requirement places a significant burden on users and can lead to poor password management practices (e.g., reusing passwords across accounts or writing them down).
Positives: The uppercase and number requirements add complexity, but could be easily remembered by users if chosen predictably.
Question 4
Observations from Server Logs:
The logs show repeated failed login attempts from the same IP address (212.1.5.50), followed by a successful login. This behavior is indicative of a brute force attack:

Multiple failed attempts with password mismatches over a short period.
Success after many attempts, indicating that the attacker eventually guessed the correct password after multiple failed tries.
This kind of behavior is common in brute force or credential-stuffing attacks, where the attacker systematically tries different passwords until one works.

Question 5
Biometric Reader Assessment:
Option A:
False Acceptance Rate (FAR): 0.10 (10%)
False Rejection Rate (FRR): 0.30 (30%)
Option B:
False Acceptance Rate (FAR): 0.05 (5%)
False Rejection Rate (FRR): 0.40 (40%)
Analysis:
Option A: Has a higher false acceptance rate (FAR) but a lower false rejection rate (FRR). This means that more impostors will be accepted, but fewer genuine users will be rejected.
Option B: Has a lower FAR but a higher FRR, meaning it is better at rejecting impostors but worse at accepting genuine users.
Security Perspective:
Option B offers better security because it has a lower FAR (fewer impostors will be accepted).
Usability Perspective:
Option A offers better usability because it has a lower FRR, meaning that fewer genuine users will be rejected by the system.
Trade-off: If security is more important, Option B might be better. If usability (reducing false rejections) is prioritized, Option A would be more suitable.