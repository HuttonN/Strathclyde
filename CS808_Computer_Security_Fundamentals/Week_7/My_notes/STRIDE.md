# STRIDE Framework

## Introduction

- Security is often overlooked during system development.
- STRIDE was developed to help developers identify common types of threats.
- The acronym STRIDE represents:
  - **S:** Spoofing
  - **T:** Tampering
  - **R:** Repudiation
  - **I:** Information Disclosure
  - **D:** Denial of Service
  - **E:** Escalation of Privilege

## Overview of STRIDE

STRIDE is structured to help developers consider common security threats to systems. Each element relates to a specific security property, has a definition, and is illustrated with an example.

### Spoofing
- **Property:** Authentication
- **Definition:** Masquerading as someone or something else.
- **Example:** Phishing emails and websites.

### Tampering
- **Property:** Data Integrity
- **Definition:** Unauthorized modification of data.
- **Example:** Changing a salary record in an HR database.

### Repudiation
- **Property:** Non-repudiation
- **Definition:** Rejection of responsibility for an action.
- **Example:** Denying sending an email or accessing inappropriate websites.

### Information Disclosure
- **Property:** Confidentiality
- **Definition:** Unauthorized access to confidential information.
- **Example:** Password leaks.

### Denial of Service
- **Property:** Availability
- **Definition:** Preventing legitimate users from accessing services.
- **Example:** Service request floods (e.g., HTTPS attacks).

### Escalation of Privilege
- **Property:** Authorization
- **Definition:** Gaining higher access privileges without proper authorization.
- **Example:** A read-only user gaining write access to a document.

## Application of STRIDE

- **Purpose:** Helps developers proactively identify potential threats to systems.
- **Process:**
  1. Consider each STRIDE element for the system component or application.
  2. Document threats and assumptions.
  3. Identify mitigation strategies for each threat.

### Example Application
- Threat: Spoofing a web application by trying common username/password combinations.
- Mitigation: Implement a password policy and provide training to staff.

## Mitigation Approaches

- **Spoofing:** Use proper authentication mechanisms.
- **Tampering:** Ensure data protection and integrity measures.
- **Repudiation:** Implement non-repudiation mechanisms like digital signatures.
- **Information Disclosure:** Use encryption, cryptographic hashes, or air-gapped machines.
- **Denial of Service:** Use firewalls, intrusion detection/prevention systems.
- **Privilege Escalation:** Employ robust authorization mechanisms.

## Limitations

- STRIDE is a **proactive framework** for identifying threats but is not comprehensive.
- It may miss novel or day-to-day vulnerabilities during reactive analysis.