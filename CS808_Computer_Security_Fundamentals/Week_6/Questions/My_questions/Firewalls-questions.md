# Firewalls - Questions

## Introduction

&nbsp;
<details>
<summary>1. What is the purpose of a firewall?</summary>

Firewalls protect networks and devices by monitoring and filtering traffic packets entering or leaving a network, providing a layer of security against attacks through network connections.

</details>

&nbsp;
<details>
<summary>2. What are the two general approaches to firewalls?</summary>

1. **Packet filtering approach**  
2. **Proxy-based approach**

</details>

&nbsp;
<details>
<summary>3. Why is an internet connection both essential and a potential security risk for organizations?</summary>

An internet connection is essential for modern operations like cloud-based software and SaaS, but it exposes the network to potential attacks.

</details>

## Aim of a Firewall

&nbsp;
<details>
<summary>1. How does a firewall provide protection for a private network?</summary>

A firewall provides protection by using a combination of security mechanisms such as monitoring and filtering inbound and outbound traffic packets.

</details>

&nbsp;
<details>
<summary>2. What is the primary goal of a firewall?</summary>

To safeguard the private network from unsecured external networks like the internet by filtering and monitoring network traffic.

</details>

## Approaches to Firewalls

### Packet Filtering

&nbsp;
<details>
<summary>1. What is a firewall rule?</summary>

A firewall rule is a condition applied to traffic to determine whether a packet should be allowed to pass through the firewall.

</details>

&nbsp;
<details>
<summary>2. What are three key attributes a packet filter examines?</summary>

1. **Source address**: Where the packet comes from.  
2. **Destination address**: Where the packet is going.  
3. **Protocol host**: Protocols like Telnet or SSH.

</details>

&nbsp;
<details>
<summary>3. What are the possible actions for a packet in packet filtering?</summary>

1. **Accepted**: Allowed to pass through the firewall.  
2. **Denied**: Sent back to the sender.  
3. **Dropped**: Deleted without notification.

</details>

&nbsp;
<details>
<summary>4. What should be avoided when creating firewall rules?</summary>

* Avoid conflating or contradictory policies.  
* Ensure there is a default rule for unaddressed traffic.  

</details>

&nbsp;
<details>
<summary>5. How can port number ranges influence firewall rules?</summary>

Rules should account for all possible source ports, especially for protocols like HTTP, which can use ports between 1,024 and 65,535 for requests.

</details>

&nbsp;
<details>
<summary>6. What is a default rule in a firewall, and why is it important?</summary>

A default rule defines the action for packets that do not match any specific rules, ensuring unaddressed traffic is handled appropriately.

</details>

### Proxy-based Approach

&nbsp;
<details>
<summary>1. What is a proxy server?</summary>

A proxy server acts as a gateway between networks, such as the internet and an internal LAN, to manage requests and enforce security policies.

</details>

&nbsp;
<details>
<summary>2. How does a proxy server enhance security?</summary>

* It hides information about the internal network.  
* It enforces specific protocols.  
* It authenticates requests before forwarding them.  

</details>

&nbsp;
<details>
<summary>3. What are the three key questions a proxy server asks before granting access?</summary>

1. What is being accessed?  
2. Who is making the request?  
3. Is the requester authenticated?

</details>

&nbsp;
<details>
<summary>4. Describe two methods used by a proxy server to protect internal network information.</summary>

1. **Host IP Address Hiding**: Adds its own IP header to packets, hiding internal host IPs
