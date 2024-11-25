# Access control overview

In this section we will look at access control. Typically there are three stages when you try to access a system as an end user:

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

---

Next: [Password Security](Password_Security.md)