# Advanced Persistent Threat - Questions

## Introduction

&nbsp;
<details>
<summary>
1. What does APT stand for?
</summary>

APT stands for Advanced Persistent Threat.
</details>

&nbsp;
<details>
<summary>
2. What are the four components covered in APT notes?
</summary>

1. What is it?
2. Why is it so concerning?
3. How does it happen?
4. What can we do about it?
</details>

---

## What is it

&nbsp;
<details>
<summary>
1. How is an Advanced Persistent Threat defined?
</summary>

An APT is a well-funded, long-term attack or campaign targeting an organisation, often involving state actors, aiming to maintain access to systems over an extended period.
</details>

&nbsp;
<details>
<summary>
2. What are the three key characteristics of APTs?
</summary>

1. **Long-term**: Campaigns can last for several years.
2. **Well-funded**: Often backed by state actors or large organisations.
3. **Well-organised and researched**: Significant investment in time and resources.
</details>

---

## Why is it so concerning

&nbsp;
<details>
<summary>
1. Why are APTs difficult to detect?
</summary>

APTs are stealthy and disguise malicious traffic to appear legitimate, making it hard for traditional tools like firewalls and intrusion detection systems to identify them.
</details>

&nbsp;
<details>
<summary>
2. What is the typical consequence of an APT being identified late?
</summary>

Damage is likely to have already occurred due to the long-term nature of the attack.
</details>

---

## How does it happen

### Reconnaissance

&nbsp;
<details>
<summary>
1. What activities might attackers perform during reconnaissance?
</summary>

1. Exploring publicly available websites.
2. Identifying staff vulnerable to social engineering.
3. Gathering other relevant information about the system.
</details>

### Initial Compromise

&nbsp;
<details>
<summary>
1. How might attackers gain a foothold during the initial compromise stage?
</summary>

1. **Phishing emails**: Tricking users into providing access.
2. **Malware**: Exploiting software vulnerabilities.
3. **Poor password management**: Leveraging weak credentials.
</details>

&nbsp;
<details>
<summary>
2. What is the goal of outbound communication during the initial compromise?
</summary>

To set up channels for exfiltrating data or assets from the compromised network.
</details>

### Lateral Movement

&nbsp;
<details>
<summary>
1. What might attackers attempt during lateral movement?
</summary>

1. Compromising other hosts.
2. Accessing related networks.
3. Locating data for extraction.
</details>

### Data Exfiltration

&nbsp;
<details>
<summary>
1. What happens during the data exfiltration stage?
</summary>

Attackers send extracted data back to their devices using outbound communication channels set up earlier.
</details>

### Maintenance and Concealment

&nbsp;
<details>
<summary>
1. What are the key activities during the maintenance and concealment stage?
</summary>

1. Covering tracks (e.g., altering logs).
2. Maintaining access to compromised systems.
3. Concealing evidence of the attack.
</details>

---

## What can we do about it

&nbsp;
<details>
<summary>
1. How does shifting the security focus help mitigate APTs?
</summary>

It involves monitoring both inbound and outbound traffic, instead of focusing solely on perimeter security.
</details>

&nbsp;
<details>
<summary>
2. List some mitigation techniques for defending against APTs.
</summary>

1. **Principle of least privilege**: Restrict access to only what is necessary.
2. **Patch management**: Regularly updating software and operating systems.
3. **Behaviour monitoring**: Detecting unusual or malicious activity within the network.
4. **End-user training**: Raising awareness about secure practices and social engineering threats.
</details>

&nbsp;
<details>
<summary>
3. Why is end-user behaviour critical in mitigating APTs?
</summary>

End users are often the primary entry point for attackers through social engineering techniques. Educating them helps reduce this vulnerability.
</details>

&nbsp;
<details>
<summary>
4. Can APTs be entirely prevented? Why or why not?
</summary>

No, APTs cannot be entirely prevented. Security relies on building multiple layers of defense to reduce the likelihood and impact of such attacks.
</details>