# Authorisation

## Introduction

So far in our look at access control, we've looked at identification and authentication, so claiming an identity,verifying that you are that person. But we haven't looked at authorization.

Authorization is the element that basically says, OK, you have access to the system, but are
you permitted to complete this particular task? This could be access to particular files, or it
could be access to a particular function within a system. Access control can be considered as
the way of managing the authorization element of this process.

## Access Control Models

### Lampson model

Let's have a look now at a traditional access control model by Lampson.

![Lampson model](./images/Lampson_model.png)

You'll see on the diagram here we have four entities:
* **Subject:** an end user or even a process requesting access. 
* **Access Request:** which is the request itself to gain access to a particular resource.
* **Object:** resource being accessed (e.g. file or function)
* **Reference Monitor:** the part of the system which verifies if the subject has the correct authorization levels for that particular object.

We could attache the authorization element at the following:
* **Subject Level:** Defines what actions a subject is allowed to perform (e.g. Alice can read but not write)
* **Object Level:** Defines what actions are permitted for an object (e.g. users can read but not alter)

### Unix Access Control

There are, at a basic level, two access modes - observe and alter. However, the
set of access modes are often a lot richer. 

We can have a look at one particular access model if we look at the Linux-based systems. Within
this system, we have the operations:
* Read (`R`) 
* Write (`W`)
* Execute (`X`). 

For any file within the Linux structure, we're going to have the following categories:
* Owner: User who created the particular object
* Group: A defined group of users within the system.
* World: Any user outside the owner or group

For each of these we have permissions. For example:

![UNIX Access Control](./images/UNIX_Access_Control.png)

* Full access for owner (fairly standard): ```R W X```
* Read and write but no execution for group: ```R W -```
* No one else to have any access: ```- - -```

## Principle of Least Privilege

One of the important principles when it comes to authorization is the principle of least privilege. This effectively says that you should permit access at the least amount of privilege possible. For example, to do their job, you should not give someone complete access to everything, but you should only give them access to the minimal amount of information that they need in order to execute their job properly. 

The reasons for using least privilege are:
* if someone were to be given more access than required, that, obviously, increases the chances of information disclosure
* it also increases the risk of an attacker trying to gain access to that particular account in order to increase their access to particular functions or objects. 

The latter is referred to as a privilege escalation attack.

## Privilege Escalation Attacks

There are two different types of privilege escalation attack:
* vertical privilege escalation attack
* horizontal privilege escalation attack

### Vertical Privilege Escalation

A vertical privilege escalation attack is where the attacker tries to move onto an account which has more access
than they have. 

As an example, you could think of this as someone working with a university and trying to gain access to a user account for HR, which is going to have more access to the data relating to employee salaries.

### Horizontal Privilege Escalation

A horizontal privilege escalation attack is where the attacker tries to gain access to users with the same level of functionaility but with different data. 

For example, if you have an account for a bank, and you're trying to get access to someone else's account, clearly, that would violate the information security. But you would still be accessing the same level of functions.

### Delivery Mechanisms

They can be delivered through, for example, password guessing attacks or SQL injection attacks. 