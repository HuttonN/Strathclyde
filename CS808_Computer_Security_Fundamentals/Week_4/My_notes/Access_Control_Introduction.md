# Access control Introduction

## Access control overview

In this section we will look at access control. Typically there zre three stages when you try to access a system as an end user:

* ***Identification:*** where you claim an identity
* ***Authentication:*** where you try to confirm an identity
* ***Authorisation:*** making sure you have the appropriate permissions and authority to access specific data or functions 

When we look at authentication, specifically user authentication, there are typically three different factors which we could use to authenticate the user. We have 
* ***Knowledge:*** something you know. Typically a text-based password, but there are alternatives
* ***Biometrics:*** something you have. Aspects such as fingerprints, iris, retina, or even voice recognition.
* ***Tokens:*** something you are. Although these tend to be used less often, these can be, for example, access cards which only you should have access to.

Multifactor authentification (MFA) can be used, and has benefits:
* additional security
* if one factor is comprimisedf, MFA gives extra assurance that it is the end user attempting access

To be MFA, they must come from two seperate factor categories. So you could have a form of biometrics as well as a password or a token as well as a password or a token and biometrics and so forth. Two passwords by technicalities doesn't really count as multifactor authentication.

The drawback with MFA is usability. It's down to the end user to decide are they more interested in the security and willing to give up the ease of having only a single factor there?

### Password Security

When considering the security of passwords we need to address:
* how passwords are generated
* how passwords are stored
* how passwords are attacked

Note: when we discuss passwords we are referring to alphanumeric tex based passwords

#### Password Generation

Password generation can be challenging. Too simple makes it easy to recall, but also easy to attack (low entropy). Too random and it makes it difficult to attack, but also difficult to recall (high entropy).

In generating passwords you can be shown password strength meters. When considering what a strong or secure password is people will often suggest a mix of upper and lower case letters,special characters and numbers as a “strong” password. Generally, these work on the basis of calculating the entropy of the password 

##### Entropy

Entropy was created with application to information compression, and is a measure of how few bits can be used to represent the data. The more random the data is, the more bits required to represent it. This concept was extrapolated to determine the redundancy in a given language, and then to determine the redundancy in a password. The idea being that a more random password has higher entropy and takes more processing power to crack.

Entropy is measured in bits, where each bit represents a binary decision. For example, consider a password of length $k$ bits. There are $2^k$ possible passwords so the entropy is $k$ bits as $k$ binary decisions are needed to define the password.

If we were only working in binary then the length of the password would be the entropy. However, say we're working with the lowercase letters. Each character in a password has an entropy of $\log_{2} 26 \approx 4.7$. We can think of this as applying a binary search on the 26 lowercase letters, e.g.:
* is it in a to m? No, then it's in n to z
* is it in n to s? Yes
* is it in n to p? No, then it's in q to s
* is it in q to r? Yes
* is it q? No, then it's r

Using the above it takes on average 4.7 questions to determine the correct letter. Then the entropy of a password of length $k$ is $k \log_{2} 26$.

The problem with the above is that it assumes that a password has been randomly selected from the the password space (set of all possible passwords), but we as users don't pick random passwords, and can be quite predictible (password $123456$ is very common). This is a limitation of using entropy in this way as it can skew the apparent security of a password. For example, $password123$ isn't a good password as it could be easily guessed, but it has entropy of approximately 41 bits which suggests reasonable strength.

Shannon did further work, performing an experiment looking at a 27 letter alphabet (lower case letters plus a space character). People were asked to guess the next letter given the previous letter. It was observed that it is difficult to guess the first letter of a string but it gets progressively easier the more letters you have. In fact the result was that the first character contributed about 4.7 bits, the second 2.8 bits, the third 2.3 bits then each subsequent character contributed about 1.5 bits, with the sum providing an estimate of the entropy of the user chosen password. This method gives us a more realistic estimate of user chosen entropy but has the flaw that it wasn't designed specifically for passwords.

These two approaches, whilst flawed, are generally the best we have. Indeed, the initial calculation tends to be the basis of strength meters on the internet.

In generating passwords guidance is beginning to change to recognise the human aspect of using passwords. In particular, recommendations such as forcing frequent password changes, adding requirements such as minimum length, plus a mix of lower and upper, plus special characters and numbers place undue burden on users and as we have discussed this can result in poor password management. 

Instead, guidance from the National Cyber Security Centre recommends three random words. This is more memorable, and emphasises length over randomness.

#### One-time passwords

One final option for passwords which is worth mentioning is the use of a one-time password. A one-time password (OTP) is a random password valid for a single session only, ordinarily with a time limit by which you must use it. You may have come across this through use of bank security OTP devices:

![OTP device](./images/OTP_device.png)

#### Storing Passwords

##### Introduction

When a user registers for a service, they often are required to provide a username and password. In order to authenticate the user in future, this password needs to be stored by the service for future reference. Clearly we should not store this password ‘in the clear’ that is in a plaintext format where if the database were compromised any attacker could simply read the passwords without further effort.

Instead we look at the process of using password hashes and salts.

##### Hashes

Password hashes are effectively cryptographic hashes, but often have mechanisms inbuilt to slow the process of generating a hash. As you will see when we come to the types of attacks on passwords, slowing the computation of the hash makes it more challenging for an attacker. One example of such a hashing function is bcrypt which is based on the blowfish cipher.

Hashing the password for storage ensures the plaintext password is never stored on the server or in the database. It also means, so long as an appropriate hashing function is used, that it is a one way function making it difficult to determine the original password from the hash value alone. You will see as we discuss the different aspects that there are a range of mechanisms which improve the security of the password in storage.

##### Salts

Another way of ensuring a password is robust to cracking when stored in a database is to make use of a salt. A salt is a long pseudo-random string (generated using a cryptographically secure pseudorandom generator) which is prepended or appended to a password before it is hashed. This means that if two or more users have the same password, they will have a different password hash due to the inclusion of a salt. This again makes it more challenging for an attacker to crack a password as we will see below. To ensure a password hash is correct at the time of authentication, the server needs to store the salt in the database with the password. Note that the salt does not need to be kept secret, it is providing a randomisation of the password which results in specific attacks becoming ineffective. Passwords within a database should use different salts since having two identical passwords with the same salt would mean the same hash value, which is contrary to the purpose of the salt. A salt should also be sufficiently long so as to avoid an attacker being able to calculate all possible salts. For example, an 8 bit salt would be much too small. You may wish to use a salt of the same length as the size of your hash function output, e.g. SHA256 would use salts of length 256 bits.

##### Three Strikes and You Are Out

Often to mitigate an attacker attempting many passwords in an effort to gain access to the system, a system will implement a maximum number of attempts before the user is locked out of their account. The number of unsuccessful attempts can vary, but often it is three or five. The limitation here is that users forget their passwords legitimately and it can be cumbersome to reset the password.

##### Checking the Password for Authentication Process

Making use of hash functions and salts means when a user authenticates the following general process is followed:

* the provided password is combined with salt and hashed
* the hash value is compared with the stored hash value
* if they match, the user is successfully authenticated.

#### Attacking Passwords

There are a range of different attacks which can be used to "crack" a password.

##### Brute Force

In a brute force attack the attacker attempts all possible passwords, which is generated from the password space. This can be completed online, where a tool or attacker provides direct entry in real time. Alternatively, this can be completed offline. In this situation the attacker has access to a set of credentials, e.g. from a compromised database of passwords. It is possible to buy such data sets, and older data sets of compromised passwords are readily available on the web. These are often gathered through attacking systems using attacks such as SQLi. You may even have received a communication from a company asking you to reset your password due to a suspected or known compromise. 

Clearly brute force could be time consuming, and is not the most effective approach.

##### Password guessing

It should be noted that if an individual is known to the attacker, or there is information available to the attacker about a target individual then guessing the password can become easier. A common example is often portrayed in film and TV where in an effort to break into a laptop they try combinations of relatives’ birthdays and favourite pets. All this is simply to say be careful in how you generate passwords and share personal information.

Another area for password guessing is where default username and passwords (such as admin and password123) which should be changed on purchase of a device or installation of software are left as is. This means an attacker with knowledge of the default configuration for a given device or system may be able to exploit it.

##### Dictionary Attack

A dictionary attack is more sophisticated than a brute force attack. It makes use of a pre-populated list of possible passwords. This can be generated from common password lists, compromised password lists, and words from a dictionary as we typically think of it. It can make use of lists of pop culture references such as movies, and need not be in English alone. Using such a list is much more likely to be successful since we are reducing the potential password space to more probable passwords. Dictionary attacks can be completed online as detailed above, or offline with a compromised database of usernames and passwords (or password hashes).

Note that if passwords are hashed and the attacker is attempting to determine the plaintext value, then the attacker must compute hash values of the plaintext dictionary values. Multiple hash functions can be used to calculate hash values for a single potential password. This allows the attacker to compare the computed hash with the hash in the compromised dataset to determine the original input. This is where salts can help mitigate attacks - by randomising the hash values an attacker needs to know the salt for that password in order to compute the hash value. Note also that assuming each user has a different salt, the same password will have different hash values due to the different salt.

##### Pre-computed Hash Tables

As one might imagine, an attacker can precompute different hash values using a range of common hash functions and a dictionary of passwords. This means when it comes to trying to crack passwords, they are able to use a lookup table to determine if they have the original password. If they find a hash value in the compromised passwords which matches a pre-computed hash then they can locate the password used to generate that value. As above, this assumes there is no salt, or a very poorly implemented salt.

There is a more sophisticated version of pre-computed hash tables called rainbow tables, but this is beyond the scope for our purpose.

##### Software

There is also software available to crack passwords. One real world example is John the Ripper.

### Biometrics overview

A biometric  is a sufficiently distinct trait which can be measured, quantified, and stored in such a way as to allow authentication to happen for the end user.

We can split it into two different categories:
* ***physical biometrics:*** facial identification, fingerprint recognition, and so forth
* ***behavioural biometrics:*** things like how you type

There are two stages when we look at biometric authentication - enrolment then operations:

* ***enrolment:*** When we look at enrolment, what we're trying to establish is what's referred to as a template. A template is basically the computer representation of that distinctive trait. So for example, a fingerprint could be broken down into aspects, such as the swirls and loops within your fingerprint. Having this template stored means that when you go to authenticate, you provide your biometric, and it can take that, perform the similar calculation, and determine whether it's sufficiently close to the template. This then takes us to different modes of operation.
* ***operations:*** Within biometrics, we can either use it in identification mode or verification mode.
    * ***Verification:*** this mode is very likely what you use most of the time. This is where there's a template stored, you've already claimed your identity, and you're just trying to check that the biometric you provide matches the identity template that they have on the database.
    * ***Identification:*** In contrast, identification mode is more like what we would think of as a watch list for the FBI, where you're presented with a biometric and you need try and find the corresponding identity from the database. That's a much more challenging problem and not one that we are particularly interested in for this module. So, we'll focus on verification mode.

When looking at different biometric systems, one helpful tool is to be able to determine whether one is better than the other. In order to do this, we need to define a few metrics, which are going to be helpful. We have 
* ***true positive (TP):*** where someone is the genuine user and is accepted as they should be. 
* ***true negative (TN):*** where someone isn't a user and they are correctly rejected. 
* ***false positive (FP):*** where someone shouldn't be allowed access, but is allowed access. 
* ***false negative (FN):*** where someone should be accepted, but they have been rejected

The following are also needed:
* ***true acceptance rate:*** proportion of genuine users that are appropriately authenticated. Given by $\frac{TP}{TP+FN}$ 
* ***true rejection rate:*** proportion of unauthorised users that are appropriately rejected. Given by $\frac{TN}{TN+FP}$ 
* ***false acceptance rate:*** proportion of unauthorised users that a incorrectly authenticated. Given by $\frac{FP}{FP+TN}$
* ***false rejection rate:*** proportion of genuine users that are incorrectly rejected. Given by $\frac{FN}{FN+TP}$

Clearly, in any biometric system, we want to maximise the true positives and minimise the false negatives. One way of modelling this information is to use an ROC curve. This stands for Receiver Operating Characteristic. Effectively, what this does is it maps our true acceptance rate (proportion of people who were accepted and should have been accepted) versus the false acceptance rate (proportion of people who were accepted, but shouldn't have been).

We can map the value for a given biometric classifier on this graph shown here.

![ROC curve](./images/ROC_curve.png)

On the $x$-axis, we have the false acceptance rate. And on the $y$-axis, we have the true acceptance rate. At the corner, we have the value $0$, and our maximum is going to be $1$ on both of these as we are working with a proportion of the whole.

When we look at our classifier effectively, what you're going to end up with is a score. You're going to look at the biometric that's provided. You're going to perform whatever transformations and calculations you need to complete, and then you need to make a judgement as to whether you accept that it matches the template or doesn't match the template. Now, this is normally done on a sliding scale. So on this sliding scale, we need to decide, at which point we'll say, OK, this is where we're going to accept that these two are similar enough in order to provide a positive result. Now clearly, this threshold can be moved around. You can say move this closer to zero. In which case, you're going to get more true positives because you're catching more people and saying that they're positive, but you are also going to increase your false positives because you're lowering that threshold for acceptance.

In contrast, if you were to move this higher up, then you would get certainly lower false positives, because you have a higher standard to meet. However, you would also get lower true positives. You'll start to reject people who should be accepted. So it is a bit of a balance trying to find out where on that scale we want to place our threshold.

On our ROC curve, if we were to take a particular biometric classifier or biometric system and plot the true accept rate and the false accept rate for all the different thresholds that we wish to look at, then we can make our ROC curve. Now, if we were to do something and it was basically random guessing, what we would end up with is a diagonal line up here. Then for our curve, if we start off at 0, then we'll end up with something which looks a little bit like this, where that's going to end up as $(1,1)$. This means that we can start to compare different systems because we can have curves with different shapes (see graph). If you consider the three curves, which is the better system?. Well, the better system is the one that gives us a better true accept rate and a lower false accept rate. In this particular instance, the curve at the top is performing better. We're getting a higher true acceptance rate for not much of an increase along our false accept rate.Whereas, this bottom curve, there's not terribly much movement there. It started to become closer to guesswork. 

Now clearly, there's a lot more that can be said about our ROC curves, but for our purpose, this is sufficient.

#### Further Biometrics

In this section we're going to take a slightly more in-depth look at some common physical biometrics as well as a high-level overview of behavioural biometrics. Biometrics offer the benefit of less cognitive load on the end user. You don't need to remember a range of passwords or other knowledge-based authentication. Instead, it's something which comes inherently with them, such as a fingerprint or an iris or retina scan. We'll take a little bit of a deeper look into fingerprints and iris and retina scans. 

Note, biometrics is obviously a field in its own right. As a result, you can go very in-depth into these areas. So what we'll focus on today is a high-level level overview of how these different methodologies function, starting off with facial recognition.


##### Facial recognition

***TO TIDY UP AFTER:***

Whilst technology is certainly improving in this area, it's still by no means perfect. 

Recall that we have two possible uses or modes of operations with biometrics:
* identification: where you have a range of possible images and you're trying to identify an individual person within that. 
* verification, which is what we are focusing on, where there's a stored biometric, perhaps in a device, such as a mobile phone or tablet and you're just trying to verify that the identity claimed matches the one stored. 

With facial recognition, we're commonly looking at aspects such as features on the face like the distance between your eyes, the length of your nose, distance between the mouth and eyes, a variety of different focus points on the face. This can then be translated into a template when you are registering. Then, when you go to authenticate, it tries to extract this information again from the visual that it has and sees whether it closely matches the template stored in your database. There are a range of different options in terms of the algorithm used to implement this. One such algorithm as to use Eigenfaces. However, there are a variety of different algorithms out there. The NIST does regular testing of a range of different mechanisms, looking at aspects such as how effective the false accept rates and false reject rates are, and so forth. So there's a lot of data in that kind of field. One interesting area of facial recognition is around the diversity of the faces used to train such systems and algorithms. There has been a lot of research done at MIT which demonstrated that facial recognition was inherently biased, particularly towards white males. So it's clearly a field which has a lot of different facets and it's good to see that we've been moving forward in this area. There is, obviously, the privacy issues and we'll come back to speak a little bit about those later in the video. Real-world world use of facial recognition can be a little bit patchy. In particular, you've probably seen a number of news reports related to the use of facial recognition in crime settings and how individuals can be falsely registered as criminals. So clearly, there's a few things to consider there. It's also quite possible that in using facial recognition, you get a lot of false rejects. So as we improve, it's important to keep a balanced view on the benefits and the drawbacks of using such a system.

***TO TIDY UP BEFORE:***

##### Iris recognition

##### Retina recognition

##### Fingerprint recognition

### Authorisation