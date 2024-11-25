# STRIDE Framework Questions

## Introduction

&nbsp;
<details>
<summary>
1. What is the purpose of STRIDE?
</summary>

To help developers systematically identify common security threats in a system during development.
</details>

&nbsp;
<details>
<summary>
2. What does STRIDE stand for?
</summary>

- **S:** Spoofing  
- **T:** Tampering  
- **R:** Repudiation  
- **I:** Information Disclosure  
- **D:** Denial of Service  
- **E:** Escalation of Privilege
</details>

---

## STRIDE Threats

### Spoofing

&nbsp;
<details>
<summary>
1. What security property does spoofing relate to?
</summary>

Authentication.
</details>

&nbsp;
<details>
<summary>
2. Provide an example of spoofing.
</summary>

Phishing emails and websites.
</details>

---

### Tampering

&nbsp;
<details>
<summary>
1. What is tampering?
</summary>

Unauthorized modification of data.
</details>

&nbsp;
<details>
<summary>
2. What security property does tampering affect?
</summary>

Data integrity.
</details>

&nbsp;
<details>
<summary>
3. Provide an example of tampering.
</summary>

Modifying a salary record in an HR database.
</details>

---

### Repudiation

&nbsp;
<details>
<summary>
1. What does repudiation mean in computer security?
</summary>

The rejection of responsibility for an action.
</details>

&nbsp;
<details>
<summary>
2. Provide an example of repudiation.
</summary>

Denying sending an email or accessing an inappropriate website.
</details>

---

### Information Disclosure

&nbsp;
<details>
<summary>
1. What does information disclosure relate to?
</summary>

Confidentiality.
</details>

&nbsp;
<details>
<summary>
2. Provide an example of information disclosure.
</summary>

Password leaks.
</details>

---

### Denial of Service

&nbsp;
<details>
<summary>
1. What security property is impacted by denial of service?
</summary>

Availability.
</details>

&nbsp;
<details>
<summary>
2. What is an example of denial of service?
</summary>

Service request floods (e.g., HTTPS attacks).
</details>

---

### Escalation of Privilege

&nbsp;
<details>
<summary>
1. What does escalation of privilege mean?
</summary>

Gaining higher access privileges without proper authorization.
</details>

&nbsp;
<details>
<summary>
2. Provide an example of escalation of privilege.
</summary>

A read-only user gaining write access to a document.
</details>

---

## Application of STRIDE

&nbsp;
<details>
<summary>
1. How can STRIDE help in system development?
</summary>

By identifying potential threats, documenting assumptions, and suggesting mitigation strategies.
</details>

&nbsp;
<details>
<summary>
2. What is an example of mitigation for spoofing?
</summary>

Implementing a password policy and providing training to staff.
</details>

---

## Mitigation Approaches

&nbsp;
<details>
<summary>
1. What mitigation strategies are suggested for tampering?
</summary>

Ensure data protection and integrity measures.
</details>

&nbsp;
<details>
<summary>
2. How can information disclosure be mitigated?
</summary>

Use encryption, cryptographic hashes, or air-gapped machines.
</details>

&nbsp;
<details>
<summary>
3. How can denial of service attacks be mitigated?
</summary>

Use firewalls, intrusion detection/prevention systems.
</details>