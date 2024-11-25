# Communication Vulnerabilities - Questions

## Packet Sniffing

&nbsp;
<details>
<summary>
1. What is packet sniffing?
</summary>

Packet sniffing is where an attacker views information sent through a network. A packet sniffer monitors and logs all network traffic on the network it is connected to.
</details>

&nbsp;
<details>
<summary>
2. What is a packet sniffer
</summary>

A packet sniffer is a program which monitors and logs all network traffic over the network they're on, not just the packets for their nodes. Once the packet data has been captured, it needs to be analysed by the software and presented in a user-readable format. 
</details>

## Vulnerability

&nbsp;
<details>
<summary>
1. Why is unencrypted data vulnerable to packet sniffing?
</summary>

If sensitive information (e.g., passwords, financial data) is sent unencrypted, an attacker can potentially intercept and read it.
</details>

## Hubs and Switches

&nbsp;
<details>
<summary>
1. Describe how hubs can be exploited using packet sniffing
</summary>

* Hubs are inherently vulnerable to packet sniffing because a hub operates by broadcasting all network traffic to all devices connected to it, regardless of the intended recipient.
* Since every device on the network receives all the packets, a device running a packet sniffer can easily capture all the network traffic. This makes packet sniffing very simple in hub-based networks, as all communication passes through all devices.
</details>

&nbsp;
<details>
<summary>
2. Describe how switches can be exploited using packet sniffing
</summary>

* Switches are designed to be more secure because they only send packets to the device that is the intended recipient. Each device on the network receives only the data that is meant for it, reducing the ability to sniff traffic.
* However, certain attacks can overload switches, forcing them into "promiscuous mode" and acting like hubs. This is because a hub sends all the packets to all the hosts on a network. Switches send packets to the correct nodes. However, some switches can reduce themselves to hubs, and hence, become susceptible to sniffing. 
</details>

&nbsp;
<details>
<summary>
3. What is a router
</summary>

One important thing to note is that what we commonly call a router these days is actually a combination of multiple things, such as the router, modem, a switch, and a wireless access point. 
</details>

### Example tools

&nbsp;
<details>
<summary>
1. Give an example of a network traffic analyser
</summary>

Wireshark is a network traffic analyser
</details>

&nbsp;
<details>
<summary>
2. Give examples of legitimate uses of this type of software
</summary>

* to identify a denial of service, 
* to troubleshoot firewall problems, such as looking at communication from a node which isn't passed to another node when you would expect it to be. 
</details>

### Passive attacks

&nbsp;
<details>
<summary>
1. Why is packet sniffing considered a passive attack?
</summary>

It allows the attacker to read information which wouldn't normally pass through their computer, without altering it.
</details>

## Man-in-the-Middle Attacks

### What is a Man-in-the-Middle Attack?

&nbsp;
<details>
<summary>
1. What is a Man-in-the-Middle (MITM) attack?
</summary>

A **Man-in-the-Middle (MITM) attack** occurs when an attacker intercepts communication between two parties by tricking the victim's computer into connecting with the attacker’s device instead of the legitimate destination.

The attacker acts as a relay, passing information between the victim and the legitimate recipient.
</details>

&nbsp;
<details>
<summary>
2. What can an attacker achieve in a MITM attack?
</summary>

* View sensitive data.
* Modify data being transmitted.
* Impersonate one of the communicating parties.
</details>

### Example Scenario

&nbsp;
<details>
<summary>
1. Describe an example scenario
</summary>

1. Victim connects to the attacker’s device, believing it is the legitimate server.
2. The attacker establishes a connection with the real server.
3. All communication between the victim and the server is passed through the attacker.
</details>

### Methods Used in MITM Attacks

&nbsp;
<details>
<summary>
1. How are MITM attacks often achieved
</summary>

MITM attacks are often achieved through **spoofing**, where the attacker tricks the victim's device into connecting with their node instead of the intended destination, intercepting and relaying traffic.

Two spoofing techniques are:
- **ARP Spoofing** (on Local Area Networks).
- **DNS Spoofing** (on the internet).

</details>

## Spoofing

### ARP Spoofing

&nbsp;
<details>
<summary>
1. What is ARP spoofing, and how does it work?
</summary>

Address Resolution Protocol (ARP) spoofing spoofing manipulates the mapping of IP addresses to MAC addresses, causing traffic meant for a legitimate IP to be sent to the attacker.
</details>

#### Process

&nbsp;
<details>
<summary>
1. Describe the process
</summary>

1. The attacker’s MAC address is falsely associated with a legitimate IP address of another node on the network.
1. Hosts on the LAN cache this spoofed ARP packet, causing data meant for the legitimate IP to be sent to the attacker instead.
</details>

#### Tools Used

&nbsp;
<details>
<summary>
1. State example of tools used
</summary>

- Examples of ARP spoofing tools include:
  - ARP Spoof
  - Cain and Abel
  - Ettercap
</details>

### DNS Spoofing

&nbsp;
<details>
<summary>
1. What is DNS spoofing, and how does it work?
</summary>

Domain Name System (DNS) spoofing manipulates DNS responses, redirecting traffic to the attacker’s server by sending a false IP address in response to a DNS query.
</details>

#### Process

&nbsp;
<details>
<summary>
1. Describe the process
</summary>

1. A victim sends a DNS request to resolve a domain (e.g., `example.com`).
1. The attacker intercepts the request and sends a false DNS response with their IP address as the answer.
1. The victim connects to the attacker’s server instead of the legitimate one.
</details>

## Replay Attacks

### What is a Replay Attack?

&nbsp;
<details>
<summary>
1. What is a replay attack?
</summary>

A replay attack involves capturing and retransmitting intercepted communication to one of the parties (server or client) at a later time.
</details>

### Example Scenario:

&nbsp;
<details>
<summary>
1. Describe an example scenario
</summary>

1. The attacker captures a communication stream, such as a username and password being sent to a server.
2. At a later time, the attacker replays the same stream, potentially gaining unauthorized access.
</details>

&nbsp;
<details>
<summary>
2. Why does encryption or hashing not prevent replay attacks?
</summary>

Even if encrypted or hashed, the packets remain identical and can be replayed without alteration.
</details>

&nbsp;
<details>
<summary>
3. Describe a replay attack scenario.
</summary>

Alice attempts to sign into `myrecipes.com` with her username and password:
- Alice sends her credentials.
- The MITM attacker intercepts this communication.
- Later, the attacker replays these packets to `myrecipes.com`, bypassing authentication checks.
</details>
