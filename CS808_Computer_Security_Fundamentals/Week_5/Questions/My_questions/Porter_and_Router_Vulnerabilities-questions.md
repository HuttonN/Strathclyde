# Porter and Router Vulnerabilities - questions

## Ports

### Introduction

&nbsp;
<details>
<summary>
1. What are ports used for
</summary>

Ports are used by applications to communicate over a network.
</details>

&nbsp;
<details>
<summary>
2. How are they identified
</summary>

A port is identified by a number, and well-known ports are associated with specific services:
* Port 20 and 21: FTP (File Transfer Protocol)
* Port 80: HTTP (Web browsing)
* Port 25: SMTP (Email)
</details>

&nbsp;
<details>
<summary>
3. What does accessing a network do
</summary>

Accessing a network opens a port on the device, enabling communication between applications.
</details>

### Port Scanning

&nbsp;
<details>
<summary>
1. What is port scanning
</summary>

Port scanning is a process which checks a host's ports, normally the common ones, to see which are open. 

</details>

&nbsp;
<details>
<summary>
2. Why can port scanning be useful to attackers
</summary>

The data, which comes back from port scanning can be useful for an attacker to identify vulnerabilities in the system. 
* It may be that ports such as file transfer are left open and an attacker could then send data through that port. That data could be something like a piece of malware. 
* These scans can also help us identify particular applications and application versions or operating system versions that are being used. Often, there are vulnerabilities related with specific versions of software, And again, this provides an opportunity for an attacker to find a way into a system.

</details>

&nbsp;
<details>
<summary>
3. What is a port scanner 
</summary>

A port scanner is a program that sends a request to each of the ports in a list, and notes whether they get a response or not.

</details>

</details>

&nbsp;
<details>
<summary>
3. Describe a legitimate use for port scanners
</summary>

To see particular vulnerabilities such as ports that you might want to close.

</details>

&nbsp;
<details>
<summary>
4. Describe a use for an attacker
</summary>

As an attacker, if you knew which ports were open, and if they are receiving information, then you might be able to do things such as identify utilities which are installed on an operating system, and this could allow you to exploit particular services with known vulnerabilities or send malicious programs and things in on those ports. 

</details>

&nbsp;
<details>
<summary>
5. Describe an example of port scanning software
</summary>

Nmap is a popular open source software which performs port scanning.

![Nmap](./images/Nmap.png)

Here, we can see the result of a scan which shows the port number followed by the protocol, all TCP in this example, then the state of the port, and the service.

</details>

### Types of Port Scanning

&nbsp;
<details>
<summary>
1. What are the types of port scan
</summary>

When performing port scanning, there are two general types of scan which can be performed - vanilla scans and stealth scans.

</details>

#### Vanilla scan

&nbsp;
<details>
<summary>
1. Describe a vanilla scan
</summary>

A Vanilla scan effectively iterates through all the different port numbers and sends a message to determine whether they are open or closed. 

</details>

&nbsp;
<details>
<summary>
2. Why are vanilla scans vulnerable to detection
</summary>

* services running on ports may log connection attempts. 
* This means a port scan might be recorded as an open request without any accompanying data. 
* As a result, such scans can be detected by the target system. 
* Vanilla scans are particularly vulnerable to detection, as they sequentially test each port, making it easier to identify the scanning activity.

</details>

#### Stealth scan

&nbsp;
<details>
<summary>
1. Describe a Stealth scan
</summary>

In contrast to a Vanilla scan, a Stealth (or Strobe) scan, looks for specific services and may limit itself to very specific ports. 

</details>

&nbsp;
<details>
<summary>
2. Why are stealth scans harder to detect
</summary>

A strobe scan is less likely to trigger an event that can be detected by a target system, because it's more particular about what type of services it accesses.

</details>

&nbsp;
<details>
<summary>
3. Describe a particular stealth scan technique
</summary>

One such technique is called fragmented packets. By splitting up the TCP header over several packets, it's harder for packet filters to detect the probe.

</details>

#### Detection and Mitigation

&nbsp;
<details>
<summary>
1. What is important for attackers to consider with regard to detection
</summary>

From an attacker's perspective, it is important to consider the IP address which is being used to perform the scan. If the same IP address is sending a lot of probes to a range of different ports, then it's very possible that the attacker will be identified.

</details>

&nbsp;
<details>
<summary>
2. How can they mitigate this
</summary>

To try and mitigate this, attackers might use things like bot nets or mask IP addresses in a different way. They could also use fragmented packets (see above).

</details>

## Routers

&nbsp;
<details>
<summary>
1. What is war driving
</summary>

If you're close to a router, it's very likely you'll be able to see it if you have a device which has a wireless card. In particular, if there is no password blocking entry onto that network, then someone could get access to it. This is called ***war driving***.

</details>

&nbsp;
<details>
<summary>
2. Describe an example
</summary>

You may have seen this if you, at one point, didn't put a password or some kind of requirement on entry to your network, and noticed perhaps neighbours accessing your network. 

</details>

</details>

&nbsp;
<details>
<summary>
3. How might this cause problems
</summary>

law enforcement might monitor networks for suspicious online behavior. If illegal activity is traced back to your network, it would be difficult to argue that you weren’t responsible.

</details>

&nbsp;
<details>
<summary>
4. How can this be mitigated
</summary>

1. **Set Up Authentication:**

    *  set up an appropriate password or other authentication mechanism on to your router to prevent unauthorised access to your network.
1. **MAC Address Filtering:**
    * restrict access to devices with specific MAC addresses
1. **IP Address Blocking:**
    * block specific IP addresses through your router’s interface.

</details>

&nbsp;
<details>
<summary>
5. Describe a useful service provided by some internet service providers
</summary>

Internet providers like Virgin or BT often provide web interfaces that allow you to configure your router's security settings easily.

</details>

&nbsp;
<details>
<summary>
6. What's important to note about certain attacks
</summary>

It's important to note that for certain attacks, such as packet sniffing, you have to be on the same network. So if you're looking at a building or an organisation that has a local area network, an attacker trying to gain access to that would have to get themselves onto that network before they're able to perform packet sniffing activities.

</details>