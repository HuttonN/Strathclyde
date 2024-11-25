# Communication Vulnerabilities

## Packet Sniffing

### What is Packet Sniffing

Packet sniffing is where an attacker can view information that is sent through a network. A packet sniffer is a program which monitors and logs all network traffic over the network they're on, not just the packets for their nodes. Once the packet data has been captured, it needs to be analysed by the software and presented in a user-readable format. 

### Vulnerability

If you think about the web and the kind of information which is sent, such as e-commerce, passwords, financial information, and so forth, if this information is unencrypted, then the attacker can potentially access all of that information.

### Hubs and Switches

Both hubs and switches can be exploited using packet sniffing

* ***Hubs:***
    * Hubs are inherently vulnerable to packet sniffing because a hub operates by broadcasting all network traffic to all devices connected to it, regardless of the intended recipient.
    * Since every device on the network receives all the packets, a device running a packet sniffer can easily capture all the network traffic. This makes packet sniffing very simple in hub-based networks, as all communication passes through all devices.
* ***Switches:***
    * Switches are designed to be more secure because they only send packets to the device that is the intended recipient. Each device on the network receives only the data that is meant for it, reducing the ability to sniff traffic.
    * However, certain attacks can overload switches, forcing them into "promiscuous mode" and acting like hubs. This is because a hub sends all the packets to all the hosts on a network. Switches send packets to the correct nodes. However, some switches can reduce themselves to hubs, and hence, become susceptible to sniffing. 
    
One important thing to note is that what we commonly call a router these days is actually a combination of multiple things, such as the router, modem, a switch, and a wireless access point. 

### Example tools

A network traffic analyser which is freely available is called Wireshark. 

As with port scanning, there are legitimate uses of this kind of software, e.g.:
* to identify a denial of service, 
* to troubleshoot firewall problems, such as looking at communication from a node which isn't passed to another node when you would expect it to be. 

You can examine the details of traffic at a variety of levels using the software, ranging from connection-level information to the actual bits comprising a single packet.

![Wireshark](./images/Wireshark.png)

Here is a screenshot from Wireshark, and you can see that the destination, IP address, username, and password are all sent in clear text, or in the clear. And this means that this information could potentially be used for an attack. 

### Passive attacks

Packet sniffing is what we call a passive attack. It allows the attacker to read information which wouldn't normally pass through their computer, without altering it.

## Man in the Middle attacks

### What is a Man-in-the-Middle Attack?

A **Man-in-the-Middle (MITM) attack** occurs when an attacker intercepts communication between two parties by tricking the victim's computer into connecting with the attacker’s device instead of the legitimate destination.

The attacker acts as a relay, passing information between the victim and the legitimate recipient. This can allow the attacker to:
- View sensitive data (e.g., credentials, personal information).
- Modify the information in transit.

### Example Scenario

1. Victim connects to the attacker’s device, believing it is the legitimate server.
2. The attacker establishes a connection with the real server.
3. All communication between the victim and the server is passed through the attacker.

### Methods Used in MITM Attacks

MITM attacks are often achieved through **spoofing**, such as:
- **ARP Spoofing** (on Local Area Networks).
- **DNS Spoofing** (on the internet).

## Spoofing

### ARP Spoofing

**Address Resolution Protocol (ARP) spoofing** manipulates the mapping of IP addresses to MAC addresses on a Local Area Network (LAN).

#### Process:
1. The attacker’s MAC address is falsely associated with a legitimate IP address of another node on the network.
2. Hosts on the LAN cache this spoofed ARP packet, causing data meant for the legitimate IP to be sent to the attacker instead.

#### Tools Used:
- Examples of ARP spoofing tools include:
  - ARP Spoof
  - Cain and Abel
  - Ettercap

### DNS Spoofing

**Domain Name System (DNS) spoofing** manipulates DNS responses, causing traffic to be redirected to the attacker’s IP address.

#### Process:
1. A victim sends a DNS request to resolve a domain (e.g., `example.com`).
2. The attacker intercepts the request and sends a false DNS response with their IP address as the answer.
3. The victim connects to the attacker’s server instead of the legitimate one.

## Replay attacks

### What is a Replay Attack?

In a **replay attack**, an attacker intercepts communication and replays the intercepted packets to the server or client at a later time.

### Example Scenario:

1. The attacker captures a communication stream, such as a username and password being sent to a server.
2. At a later time, the attacker replays the same stream, potentially gaining unauthorized access.

Even if the data is encrypted or hashed, the packets remain the same and can be replayed unless additional protections (e.g., timestamps or nonces) are used.

![Replay Attack](./images/Replay_attack.png)

#### Real-World Example:
Alice attempts to sign into `myrecipes.com` with her username and password:
- Alice sends her credentials.
- The MITM attacker intercepts this communication.
- Later, the attacker replays these packets to `myrecipes.com`, bypassing authentication checks.