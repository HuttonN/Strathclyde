# VPNs - Questions

## General Overview

&nbsp;
<details>
<summary>
1. What is a VPN?
</summary>

A VPN, or Virtual Private Network, is a tool that provides secure communication over public or untrusted networks by using mechanisms like authentication, tunnelling, and encryption.
</details>

&nbsp;
<details>
<summary>
2. What are the two main uses of VPNs?
</summary>

1. **Remote Access:** Allows a user to appear as if they are working within a specific network while being at a remote site.
2. **Site-to-Site:** Provides a secure communication channel between two different physical locations, such as office sites.
</details>

&nbsp;
<details>
<summary>
3. What are the three types of VPNs?
</summary>

1. **Trusted VPN:** Uses private lines to ensure secure communication. Rarely used today.
2. **Secure VPN:** Relies on protocols for secure communication.
3. **Hybrid VPN:** Combines features of both trusted and secure VPNs.
</details>

## Secure VPNs

&nbsp;
<details>
<summary>
1. What are the three main mechanisms of a secure VPN?
</summary>

1. **Authentication**
2. **Tunnelling**
3. **Encryption**
</details>

### Authentication

&nbsp;
<details>
<summary>
1. How does a secure VPN authenticate a client?
</summary>

A secure VPN authenticates a client using methods such as:
* Username and password combinations.
* Digital certificates.
</details>

&nbsp;
<details>
<summary>
2. What happens after authentication is successful?
</summary>

Once authentication is successful, the VPN sets up a tunnel to securely transmit data.
</details>

### Tunnelling

&nbsp;
<details>
<summary>
1. What is the purpose of tunnelling in a secure VPN?
</summary>

Tunnelling encapsulates data packets within other packets, masking the internal structure and local addressing of the network.
</details>

&nbsp;
<details>
<summary>
2. Describe the envelope analogy for tunnelling.
</summary>

* The outer packet (envelope) contains external addressing, like the building address.
* The inner packet contains local addressing, like the specific room or office within the building.
* This process masks internal network information from external observers.
</details>

&nbsp;
<details>
<summary>
3. Can tunnelling alone secure the data from attackers? Why or why not?
</summary>

No, tunnelling alone cannot secure data because attackers can still sniff the information, even if it is encapsulated. Encryption is needed to ensure data confidentiality.
</details>

### Encryption

&nbsp;
<details>
<summary>
1. What are the two modes of encryption in a secure VPN?
</summary>

1. **Transport Mode:** Encrypts data as it is created.
2. **Tunnel Mode:** Encrypts data as it is transmitted through the tunnel.
</details>

&nbsp;
<details>
<summary>
2. Give an example of an encryption algorithm used in secure VPNs.
</summary>

An example of an encryption algorithm used in secure VPNs is AES (Advanced Encryption Standard).
</details>