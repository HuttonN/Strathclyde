# Networks Introduction- questions

## Introduction

&nbsp;
<details>
<summary>
1. What is a computer network
</summary>

A computer network is a collection of computers sometimes referred to as nodes, or computer devices such as PCs, mobiles, tablets, which can communicate with each other, that is send and receive data, using a predefined set of rules called protocols. 

![Network diagram](./images/Network_diagram.png)

</details>

&nbsp;
<details>
<summary>
2. What makes communication between computers possible
</summary>

It is a combination of hardware and software which makes this communication between computers possible.
</details>

&nbsp;
<details>
<summary>
3. Describe an example
</summary>

The most common network that you'll be aware of is the internet, which primarily uses the internet protocol, or IP, to communicate between nodes.
</details>

## Types of Network Connections

&nbsp;
<details>
<summary>
1. What is the simplest form of network
</summary>

The simplest form of network that we can have is where two computing devices are connected to each other.

![Simplest network](./images/Simplest_network.png)

We can connect these using a physical or wired connection, but we can also connect these using a wireless connection.

</details>

&nbsp;
<details>
<summary>
2. What happens when more computers are added
</summary>

When you add on more computers it becomes more complex. How does one computer know whether the information is for them or whether it's for another computer on the same network? 
</details>

&nbsp;
<details>
<summary>
3. What is the solution
</summary>

addressing 
</details>

## Network Addressing

&nbsp;
<details>
<summary>
1. What does network addressing allow
</summary>

In the same way addressing a letter allows us to know where to send information to, addressing for networks allows us to know which computer should be receiving the data. 
</details>

&nbsp;
<details>
<summary>
2. Give an example of addressing
</summary>

* One form of addressing is an IP address. 
* This is the internet protocol. 
* IP addresses are commonly used in computers which are connected to the internet as you would imagine, given the protocol name. 
</details>

## Types of Networks

&nbsp;
<details>
<summary>
1. How are networks described
</summary>

Networks are also described in one of two ways according to the geographical area that they span. 
* **W**ide **A**rea **N**etwork (WAN): spans a large geographical area. The most common example of this being internet.
* **L**ocal **A**rea **N**etwork (LAN): in contrast, a local area network is over a much more defined and smaller geographical area, such as a workplace or a home network. 
</details>

&nbsp;
<details>
<summary>
2. Can WANs and LANs interact
</summary>

![LAN connected to WAN](./images/WAN_LAN.png)

As you can see from the diagram here, local area networks can reach out to wide area networks. Most commonly, this is the internet.

</details>

## Data Transmission over Networks

&nbsp;
<details>
<summary>
1. What components are required for data transmission over networks
</summary>

Well, it's down to a combination of 
* **hardware:** that's physical devices that you can touch and see.
* **software:** things that we run on computers in order to achieve any tasks that we have.
</details>

&nbsp;
<details>
<summary>
2. How is data sent over networks
</summary>

* Data is transmitted over a network in packets. 
* These are small defined chunks of data with a particular structure. 
* Often, the data that we're trying to send, such as an MP3 file, an image file, or an email can be larger than the size of a data packet. 
* And so, we have to split it across multiple packets. 
* Those packets then transmit over the network and at the other end are reformed into the original format. 
</details>

&nbsp;
<details>
<summary>
3. What are protocols
</summary>

* Computers use standard rules to transmit this information. 
* This agreed set of rules is called a protocol. 
</details>

&nbsp;
<details>
<summary>
4. What protocol is used for internet communication
</summary>

the TCP/IP protocol is used for internet communication
</details>

## Network Ports and Communication

&nbsp;
<details>
<summary>
1. What are ports
</summary>

* Another key piece of software in network communication is that of ports. 
* These provide a virtual start point and endpoint for network communication. 
* A port is a virtual location where network connections begin and end. 
</details>

&nbsp;
<details>
<summary>
2. What properties do they have
</summary>

* They're managed by computer operating systems, and so are software-based. 
* They're standardised. Each port has an assigned number, such that specific ports are assigned specific protocols to distinguish different forms of traffic. For example, HTTP uses port 80. But there are many more ports than this.
</details>

## Network Hardware and Devices

&nbsp;
<details>
<summary>
1. What are the key hardware elements in making network communication work. Describe them
</summary>

* **Network Interface Card (NIC):**
    * This is a hardware digital circuit which allows communication to a network and turns data into an electrical signal for communication. 
    * These cards are within all of your computer devices and can provide us with either wired connections through ethernet cables or wireless connection.
* **Media Access Control (MAC) address:**
    * This is a hard wired identification, specific to an individual device. It's like a physical address and is unique globally to that device. 
    * This is particularly helpful for local area network communication. 
    * This isn't something that you would normally look at. They're embedded within the device itself.
* **Hub or Switch:**
    * This is a little box that has connections like the one shown in the image on the right hand side. 
    * Both serve the function of connecting multiple computer devices to a network. 
    * It's most likely you have a switch. Hubs are more of an old fashioned piece or kit, and they would communicate all messages to all computers on a network. 
    * A switch instead, sends packets only to the intended destination, and that destination is defined by the MAC address, and that's how it gets to the right place.
* **Routers:**
    * These in particular manage a connection to the internet and manage data transmission and receiving data from the internet as well. 
</details>

## Key Components of the Internet

&nbsp;
<details>
<summary>
1. Describe key components of the internet
</summary>

* **HTTP**: 
    * Hyper Text Transfer Protocol (HTTP), is the set of rules that govern how information is communicated over the internet
    * in particular it allows the retrieval of resources such as HTML documents.
* **HTML:** Hyper Text Markup Language (HTML) is the language that's used to define the stucture of a web page.
* **IP Addresses:** 
    * any device which is connected to the internet is going to have an IP address. 
    * This value can change, So it's worth recognising that it's not necessarily consistent for a given device. 
    * This is why addresses, such as MAC addresses, can be more helpful in certain situations. 
    * The IP address is going to be something like the format shown here: 146.242.113.65. However, there is a very slightly different format in a newer version of IP addresses.
* **URL:**
    * Uniform Resource Locator (URL) is a readable way of accessing an IP address for an internet resource. 
    * As a user, trying to remember an IP address in order to access a website is not a very practical way of working. 
    * So we have URLs to do this for us.
* **DNS:** The domain name server (DNS), translates those URLs into the appropriate IP addresses.
* **ARP:** 
    * The Address Resolution Protocol (ARP) translates IP addresses into MAC addresses. 
    * So again, information coming from the internet is going to have an IP address to try and get to your machine. But it's going to want locally a MAC address to go to that specific device.
</details>