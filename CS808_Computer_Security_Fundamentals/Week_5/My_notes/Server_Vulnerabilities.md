# Server Vulnerabilities

## Introduction

In these notes we will look at a particular type of server vulnerability - denial of service attacks. Effectively, this is where legitimate access is stopped by an attacker. So at a point where a particular system or data should be accessible by the end users, it is no longer the case, because the attacker has managed to stop access. There are a number of different strategies which an attacker can use to achieve this.

One thing that it's important to point out is that there is always a chance of an unintended denial of service. This happens, for example, where the load on a server is deemed to be excessive compared to what was expected. As a result, the server can no longer cope with it and access to that particular resource or website, for example, is no longer happening. We've seen examples of this in recent years:
* When the first new Star Wars film came out, the demand for tickets to the cinema was so large that the ODEON website collapsed under the load
* Similarly, in universities, at registration time, we have on occasion seen that the servers crash.

## Types of DoS

### Service request floods

A service request flood is what we probably see on a more common basis. for example, with a website HTTP or HTTPS requests. Effectively, the server is overloaded with requests and is unable to deal with them and as a result shuts down.

You can compare service request floods to being in a restaurant. Your waiter comes up and tries to serve you. However, that relies on people waiting their turn. They can serve one person and then move on to the next and manage them as they go. However, if everyone comes at the same time and are all asking the waiter simultaneously to give access to your particular favourite foods, then that server is going to be unable to deal with the load.

### Bandwidth flood

A bandwidth flood makes use of a specific size or request that a given server can deal with. The attacker constructs a request, which is larger than the bandwidth which the server accepts, and as a result, this can initiate a denial of service.

You can see that there are similarities in terms of the service flood with the bandwidth flood, but where the service requests flood is about the quantity of requests, the bandwidth is about the size of the request.

### SYN flood

The TCP/IP protocol includes a handshake to establish a connection between a client and a server:

* The client sends a SYN (synchronise) pascket of the server to request a connection
* The server responds by sending a SYN-ACK (Synchronise-Acknowledge) packet has to acknowledge that.
* The client then send an ACK (Acknowledge) packet back to the server

![TCP handshake](./images/TCP_handshake.png)

In a SYN flood the following happens:

* the attacker sends loads of requests, initiating TCP/IP 3-way handshakes 
* the server responds to each SYN packet with a SYN-ACK packet
* The attacker doesn't send ACK packets to close off the handshake leaving the server with partially open connections , consuming system resources and potentially leading to denial of service

![SYN flood](./images/SYN_flood.png)

### Distributed denial of service

In the examples we have discussed, we were likely working under the assumption that there is perhaps one attacker using a single machine to carry out the attack. However, in reality, a distributed denial of service (DDoS) attack is often employed.

![DDoS](./images/DDoS.png)

This means it is not a single client making the requests or trying to overwhelm the bandwidth, but rather multiple clients. One of the ways an attacker can achieve this is by developing a network of what are referred to as zombies. These are computers that have been infected with a bot.

A bot allows an attacker to have remote control over the infected computer. As a result, an individual might unknowingly be contributing to a distributed denial of service attack. A network of these infected computers is called a botnet. This highlights the importance of ensuring that your computers are free from any malware that might be enabling such activities.

---

Next: [Communication Vulnerabilities](Communication_Vulnerabilities.md)