# CS808 Induction Workshop

Look into some useful background for the CS808 course

## Binary, bits and bytes

Binary is a base 2 numbering system, e.g. 1 or 0, on or off, etc. It is the way data is represented in computing. 

A binary number is a collection of bits (individual 0 or 1). A byte is a collection of 8 bits, e.g. 00101010. 

Starting from the right the nth digit represents 2^n. So 00101010 equates to 2^5 + 2^3 + 2^1 = 42. 

# Numbers

Some reminders:

A factor is a number which divides another completely, e.g. 5 is a factor of 15.

Integers are whole numbers, positve, negative or 0.

Modular arithmetic is a system of integer arithmetic which cycles to 1 after reaching the base.

How is this used in cryptography? The Caeser cipher takes each letter and shifts by a particular number, and then cycles. If using a key of 3 A goes to D, B to E etc. But then X goes back to A

Prime number - whole number greater than 1 which is divsisble only by itelf and 1.

# Networks

The simplest network consists of two computers. Any more than two requires some form of addressing, e.g. IP address 192.168.0.1

There are two basic types of network:

Wide area networks (WAN) - spans a large geographical network, e.g. the internet
Local area network (LAN) - defined over a small defined network, e.g. workplace, home

Computers send data over a network in "packets". Protocols define how its is transmitted (e.g. TCP/IP is the protocol used for internet communication), and ports provide start and end points for communication.

Ports are virtual start and end points for communication on networks, managed by opeationg systems. Each port has and assigned number (standardised) 

Hardware is also required to send data over a network:

Network Interface Card: Harware circuit which allows connection to a network, turns data into electric signal
Media Access Control address: hard wired ID specific to the network interdace of the machine
Hub or Switch: Hub broadcasts all packets to all computers (not normally used). Switch send packets to intended destination.
Routers: provides connection to the internet and manage data transmit and recieve data from the internet