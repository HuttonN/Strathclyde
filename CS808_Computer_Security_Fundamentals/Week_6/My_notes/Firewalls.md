# Firewalls

## Introduction

Firewalls are a key part of our perimeter defense in organisations. 

If you consider a company which has a large number of computers, it's incredibly likely that these computers are going to be connected in an internal local area network. But equally it's very likely that they are going to be connected to the internet. So much of modern practice involves making use of cloud-based software and software as a service. As a result, a connection to the internet is a key component of modern working. However, in doing so this introduces the possibility of a number of attacks through that network connection. So it's important to look at the different mechanisms we have which allow us to protect our networks. 

Firewalls effectively are a security concept, they can be implemented either as software or as hardware. There's two general approaches to firewalls:
* packet filtering approach 
* proxy-based approach. 

In these notes we will break down each of those, looking at how they work.

## Aim of a Firewall

The aim of a firewall is to protect your network and the devices connected to it. It's a combination of security mechanisms such as monitoring and filtering of traffic packets, which are either entering or leaving a network. The aim is to provide a private network some protection from an unsecured external network, like the internet. 

![Firewall](./images/Firewall.png)

It typically uses a combination of packet filters and/or proxies. We'll take a look at each of these in turn. 

## Approaches to firewalls

### Packet Filtering

A firewall can put conditions on inbound and outward bound traffic. These are referred to as a firewall rule. In packet filtering, rules are created which evaluate a packet to determine whether it should be allowed to pass through the firewall or not, whether that's outbound or inbound. This can involve looking at things such as 

* ***Source address*** i.e. where it comes from, e.g. packets from the internet with internal IP
* ***Destination address*** i.e. where it's intending to go to, e.g. only allows packets to bastion host
* ***Protocol host*** e.g. Telnet, SSH etc

The rules can also be customised based on whether the packets are incoming or outgoing. For example, it may be that a company is less concerned about outgoing packets and more concerned about incoming packets, which might contain things such as malware. 

Depending on these values a packet is either:
* ***Accepted:*** allowed to pass through the firewall. 
* ***Denied:*** sent back to the sender. Due to the cost of bandwidth, this isn't often done.
* ***Dropped:*** the packet is simply removed from existence, or deleted.

To implement this, the security administrator, or other colleagues who are responsible for the firewall, first have to decide what the policies are, e.g.
* deny all traffic coming in using FTP. 
* allow traffic to a specific web server, but deny all other incoming traffic. 

These policies are then translated into technical statements called rule sets. This typically comprises a name, a protocol such as FTP or TCP, a source IP and the port destination, and whether it should be allowed or denied. 

Here is an example GUI construction of a firewall interface:

![Firewall interface](./images/Firewall_interface.png)

As already mentioned, the rule has things like a name or a description, a protocol, a source IP, the destination port, and the destination IP. This policy then looks to allow or deny based on specific requirements. Recall that client applications can use random, uncommon port numbers, but typically port 80 is HTTP. 

Why is the good rule good, and why is the bad rule bad? 

* The bad one only looks at requests for port 80 to port 80. But we could feasibly have HTTP requests from any port between 1,024 to 65,535. So traffic could still feasibly be let through.
* The good one is better because it examines all possible source ports. 

Other things to watch out for when creating such rules includes trying to avoid conflating policies. For example, if one rule says to allow something and another one says to deny it for the same configuration, then this would clearly be contradictory and cause issues. The same port numbers, IP addresses, and so forth, are the kind of configurations you might want to consider. You may also wish to consider having a default rule, that is, what do you do if none of the other rules are broken or applied, and ensure that it's reflective of what you truly want to happen. 

Two approaches to policies can be to deny all within a particular range, or to allow all within a given range. For example, certain IP addresses might be preapproved, or specific IP addresses may be
blocked.

### Proxy-based approach

A proxy server acts as a gateway, or intermediary, from one network to another, e.g. from the internet into an internal local area network. 

![Firewall](./images/Proxy_server.png)

It works as follows:
* A request is made to the proxy to gain access to a given service. 
* The proxy server checks this and passes it on, assuming it is satisfied. 

It acts like a server to the client, and like a client to the server, hence the name proxy. It allows you to implement policies based on user IDs, and hide information about the structure of an internal network. This means that the proxy server is the only entity seen by the outside world. Note that for every service that you provide, there needs to be a proxy server to deal with that service.

The kind of things that the proxy server is going to ask the client who is making the access request is:
* what is it they are looking to access, 
* who are they, 
* and it's going to require some form of authentication for that. 

If it is happy with the information provided, then it can pass on the request to an internal router, which can then route that request to the server.

If we look at outbound packets when using proxy servers, if the proxy server sends out the packets from the internal network it has the potential to be sniffed, and the original IP address of the internal server could be revealed. In order to stop that, a modern proxy firewall can employ several strategies:
 
* ***Host IP address hiding:*** add its own IP header to the packets, and then the sniffer would only see the IP address of the proxy, hence hiding internal hosts.
* ***Header destruction:*** Another way to stop sniffing of the IP header is to employ header destruction. In this approach the firewall proxy destroys the packet header completely, and replaces it with its own IP header. 
* ***Protocal enforcement:*** A possible limitation of a firewall which is using a packet filtering approach is that port numbers could potentially be spoofed. This means that when looking at the filtering rules, if they are looking for specific port numbers, then this could potentially be exploited. However, with a proxy firewall this isn't so easy to do, since it enforces particular protocols. For example, it ensures that port 80 is in fact HTTP, and deals with only one application per server. 

---

Next: [Demilitarized Zones and Intrusion Detection Systems](Demilitarized_Zones_and_Intrusion_Detection_Systems)