# Porter and Router Vulnerabilities

## Ports

### Introduction

Ports are used by applications to communicate over a network.

A port is identified by a number, and well-known ports are associated with specific services:
* Port 20 and 21: FTP (File Transfer Protocol)
* Port 80: HTTP (Web browsing)
* Port 25: SMTP (Email)

Accessing a network opens a port on the device, enabling communication between applications.

### Port Scanning

Port scanning is a process which checks a host's ports, normally the common ones, to see which are open. The data, which comes back from this can be useful for an attacker to identify vulnerabilities in the system. It may be that ports such as file transfer are left open and an attacker could then send data through that port. That data could be something like a piece of malware. These scans can also help us identify particular applications and application versions or operating system versions that are being used. Often, there are vulnerabilities related with specific versions of software, And again, this provides an opportunity for an attacker to find a way into a system.

There is software that can be used for port scanning. A port scanner is a program that sends a request to each of the ports in a list, and notes whether they get a response or not. There are legitimate uses of this, for example, to see particular vulnerabilities such as ports that you might want to close. As an attacker, if you knew which ports were open, and if they are receiving information, then you might be able to do things such as identify utilities which are installed on an operating system, and this could allow you to exploit particular services with known vulnerabilities or send malicious programs and things in on those ports. 

Nmap is a popular open source software which performs port scanning.

![Nmap](./images/Nmap.png)

Here, we can see the result of a scan which shows the port number followed by the protocol, all TCP in this example, then the state of the port, and the service.

### Types of Port Scanning

When performing port scanning, there are two general types of scan which can be performed - vanilla scans and stealth scans.

#### Vanilla scan

A Vanilla scan effectively iterates through all the different port numbers and sends a message to determine whether they are open or closed. 

It's important to note that services running on ports may log connection attempts. This means a port scan might be recorded as an open request without any accompanying data. As a result, such scans can be detected by the target system. Vanilla scans are particularly vulnerable to detection, as they sequentially test each port, making it easier to identify the scanning activity.

#### Stealth scan

In contrast to a Vanilla scan, a Stealth (or Strobe) scan, looks for specific services and may limit itself to very specific ports. 

A strobe scan is less likely to trigger an event that can be detected by a target system, because it's more particular about what type of services it accesses. One such technique is called
fragmented packets. By splitting up the TCP header over several packets, it's harder for packet filters to detect the probe.

#### Detection and Mitigation

From an attacker's perspective, it is important to consider the IP address which is being used to perform the scan. If the same IP address is sending a lot of probes to a range of different ports, then it's very possible that the attacker will be identified. 

To try and mitigate this, attackers might use things like bot nets or mask IP addresses in a different way. They could also use fragmented packets (see above).

## Routers

If you're close to a router, it's very likely you'll be able to see it if you have a device which has a wireless card. In particular, if there is no password blocking entry onto that network, then someone could get access to it. This is called ***war driving*** and you may have seen this if you, at one point, didn't put a password or some kind of requirement on entry to your network, and noticed perhaps neighbours accessing your network. 

Clearly, this can cause problems, especially because law enforcement might monitor networks for suspicious online behavior. If illegal activity is traced back to your network, it would be difficult to argue that you weren’t responsible. Therefore, it's important to be aware of this risk.

There are several ways of mitigating this:
1. **Set Up Authentication:**
    *  set up an appropriate password or other authentication mechanism on to your router to prevent unauthorised access to your network.
1. **MAC Address Filtering:**
    * restrict access to devices with specific MAC addresses
1. **IP Address Blocking:**
    * block specific IP addresses through your router’s interface.

Internet providers like Virgin or BT often provide web interfaces that allow you to configure your router's security settings easily.

It's important to note that for certain attacks, such as packet sniffing, you have to be on the same network. So if you're looking at a building or an organisation that has a local area network, an attacker trying to gain access to that would have to get themselves onto that network before they're able to perform packet sniffing activities.

---

Next: [Server Vulnerabilities](Server_Vulnerabilities.md)