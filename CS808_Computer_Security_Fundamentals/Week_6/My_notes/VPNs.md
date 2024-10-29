# VPNs

In these notes, we're going to look at VPNs, virtual private networks.

We can generally think of VPNs as having two possible uses:
* ***Remote access:*** This is effectively where you are on a remote site and you wish to appear as if you are within a specific network. For example, if I'm working at home and I want to appear as though I'm working in the University environment, then I can use the university's VPN to achieve this.
![Remote Access VPN](./images/Remote_Access_VPN.png)
* ***Site-to-site:*** With site-to-site VPN, what we're trying to achieve is that someone who is perhaps at the Glasgow office wants to work with information that's available at the Edinburgh office. So it provides a secure communication channel from one site to another. 
![Site-to-Site VPN](./images/Site_to_Site_VPN.png)

There are generally three types of VPN.
* ***Trusted VPN:*** Effectively, these were where companies would have access to their own private lines, which would give them that degree of certainty that that communication was secure, as no one else was able to use those particular lines. We don't tend to see them these days.
* ***Secure VPN:*** In contrast, a secure VPN uses protocols to ensure secure communication.
* ***Hybrid VPN:*** A hybrid VPN is a combination of both.

## Secure VPNs

With a secure VPN, it's effectively a combination of three separate mechanisms:
* authentication, 
* tunnelling,
* encryption. 

We'll address each of these in turn. 

### Authentication
When the client makes a request to the VPN to set up a secure connection, it's asked to authenticate itself. This depends on the protocols which the secured VPN is using. But this could, perhaps, be through a username and password combination or even digital certificates. Once the VPN is happy that the client has authenticated, it can then move on to set-up, what is referred to as a tunnel. 

### Tunnelling

Tunnels can effectively be thought of as packing up your information packets into other packets, obscuring the information that's within. You can think of this as working with an envelope. Your envelope can have the address of the building on it. So for example, we could send a letter to the 11th floor office of Livingstone Tower. However, within that packet, what we want to do is have some local addressing. So it could then go to my office on the 14th floor. So it would use internal addressing. It has to get to the building first, using the external facing addressing. And then, from there, it can use the internal addressing. So this masks the local addressing that we might have. It's this process of encapsulating packets within other packets which helps us to mask the structure of the internal network. But of course, an attacker can still sniff this information, even if we have it layered up in different packets. So our next step is encryption. 

### Encryption

Packets are encrypted in one of two modes:
* ***Transport mode:*** In transport mode, data is encrypted as it's created.
* ***Tunnel mode:*** In tunnel mode, it's encrypted as it is transmitted through the tunnel.

The encryption used obviously varies depending on the secure VPN implementation. So it may be making use of encryption, such as AES. 
