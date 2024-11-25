# Demilitarized Zones and Intrusion Detection Systems - Questions

## Introduction

&nbsp;
<details>
<summary>1. What are two approaches for protecting internal networks from external untrusted networks?</summary>

1. **Demilitarized Zones (DMZ)**  
2. **Intrusion Detection and Prevention Systems (IDPS)**

</details>

&nbsp;
<details>
<summary>2. Why are these approaches necessary?</summary>

They provide additional layers of security and segregation, protecting internal networks from attacks originating from external untrusted networks like the internet.

</details>

## Demilitarized Zones

&nbsp;
<details>
<summary>1. What is a demilitarized zone (DMZ)?</summary>

A DMZ is a part of a network, or a complete network, placed between the internal network and the external untrusted network (e.g., the internet). It provides an additional layer of security by segregating internal resources from external access.

</details>

&nbsp;
<details>
<summary>2. How does a DMZ enhance security?</summary>

* Provides an extra layer of segregation between internal and external networks.  
* Requires attackers to breach multiple firewalls.  
* Restricts routes between private networks and the internet.  
* Ensures only external-facing resources like web servers are accessible to untrusted networks.

</details>

&nbsp;
<details>
<summary>3. Describe the two-firewall architecture for a DMZ.</summary>

1. **Perimeter Firewall:**  
    * Controls traffic between the external untrusted network and the DMZ.  
    * Allows external access to resources within the DMZ.  

2. **Internal Firewall:**  
    * Controls traffic between the internal network and the DMZ.  
    * Prevents external network traffic from accessing the internal network.  

In effect, internal and external networks can communicate with the DMZ but not directly with each other.

</details>

## Intrusion Detection and Prevention Systems

### Intrusion Detection System (IDS)

&nbsp;
<details>
<summary>1. What is an intrusion detection system (IDS)?</summary>

An IDS monitors a network for unusual behavior or suspected incidents, such as violations of security policies, denial of service attacks, malware, or unauthorized access.

</details>

&nbsp;
<details>
<summary>2. What is the purpose of an IDS?</summary>

To identify potential security incidents and log them for analysis, without necessarily taking action to stop the incidents.

</details>

### Intrusion Prevention System (IPS)

&nbsp;
<details>
<summary>1. What is an intrusion prevention system (IPS)?</summary>

An IPS is software that includes all the capabilities of an IDS but also attempts to stop potential incidents, such as blocking access to a resource or IP.

</details>

&nbsp;
<details>
<summary>2. How does an IPS differ from an IDS?</summary>

* **IDS:** Detects and logs incidents without taking action.  
* **IPS:** Detects and actively prevents incidents by blocking access or taking other measures.

</details>

### IDPS

&nbsp;
<details>
<summary>1. What does IDPS stand for, and what does it combine?</summary>

IDPS stands for **Intrusion Detection and Prevention Systems**. It combines the capabilities of both IDS and IPS technologies.

</details>

&nbsp;
<details>
<summary>2. What tasks are typically performed by an IDPS?</summary>

1. **Event Logging:**  
    * Records observed events, which can be logged locally or sent to other systems.  

2. **Alert Notifications:**  
    * Notifies security administrators about critical events via email or user interface messages.  

3. **Report Generation:**  
    * Summarizes monitored events or provides detailed reports for management or policy refinement.  

</details>

&nbsp;
<details>
<summary>3. What are some limitations of an IDPS?</summary>

* Cannot prevent administrator misconfigurations.  
* Does not address insider threats.  
* Cannot mitigate social engineering attacks.

</details>
