# Phishing Overview

## Introduction

Phishing is a type of **social engineering** where attackers attempt to:

- Obtain sensitive information (e.g., login credentials, bank details).
- Trick users into downloading malware.

The typical attack flow involves:
1. The attacker sends an email with a link or attachment.
2. The user clicks the link or downloads the attachment.
3. The attacker:
   - Collects sensitive information (e.g., credentials) from a fake website.
   - Installs malware on the user's device (e.g., via a drive-by download).

## Examples of Phishing

### Genuine Email Example

![Genuine email example](./images/Genuine_email_example.png)

- Features:
  - Contains multiple links and lacks identifying information, except a partial bank account number.
  - The **Received From domain matches the From domain** in the email overview.
- Conclusion: **Not phishing.**

### Phishing Email Example 1

![Phishing example 1](./images/phishing_example_1.png)

![Phishing example 1 metadata](./images/phishing_example_1_metadata.png)

- Features:
  - Sent in an unfamiliar language.
  - Strange formatting and phrasing (e.g., links labeled "Wife," "Man," etc.).
  - **From domain mismatch**: Email claims to be from "Bon Prix," but actual sender domain is "lemustdesdeals.com."
- Explanation:
  - Attackers can spoof the **From field** using an SMTP server and mailing software.
  - SMTP (Simple Mail Transfer Protocol) allows any computer to send emails claiming to be from a specific source domain.
- Mitigation: **Sender Policy Framework (SPF)** checks if the IP sending the email is authorized by the domain's SPF record.

### Phishing Email Example 2

![Phishing example 2](./images/phishing_example_2.png)

![Phishing example 2 metadata](./images/phishing_example_2_metadata.png)

- Features:
  - Lacks identifying information.
  - Urgency (e.g., "login as soon as possible").
  - Hovering over the provided link reveals it does not direct to the claimed domain.
  - **Domain mismatch** between the Received From field and the From field.
- Conclusion: **Phishing email.**

### Spear Phishing

![Spear Phishing example](./images/spear_fishing_example.png)

- Characteristics:
  - Targets specific individuals using personalized information.
  - Example: Job application email with an obfuscated URL (e.g., tinyURL).
- Explanation:
  - Spear phishing emails are harder to detect due to personalization.
- Mitigation: **Vigilance and awareness.**

## Common Techniques in Phishing

Phishing emails often use social engineering techniques, including:

- **Authority**: Impersonating a trusted entity (e.g., a bank, employer).
- **Impersonation**: Posing as a legitimate organization or individual.
- **Pressure and Solution**: Creating urgency (e.g., "Your account will be suspended unless...").
- **Pretext**: Providing a convincing scenario to justify the request (e.g., account verification).

## Mitigating Phishing Attacks

1. **Raising Awareness**:
   - Employee training to recognize phishing attempts.
   - Penetration testers can simulate phishing attacks and provide follow-up training.

2. **Technical Solutions**:
   - Use of **SPF** to verify email sender authenticity.
   - Employ tools to filter and block phishing emails.

3. **Best Practices for Individuals**:
   - **Verify links**: Hover over links to check the destination URL.
   - Avoid downloading attachments from unknown sources.
   - Report suspected phishing emails.

## Risks of Clicking Phishing Links

- **Malware Installation**:
  - Drive-by downloads can install malware without the user's awareness.
- **Credential Theft**:
  - Phishing websites mimic legitimate ones to collect login credentials.

## Key Takeaways

- Phishing relies on human error, making user training critical.
- Technical measures (e.g., SPF) can help mitigate phishing risks.
- Vigilance is essential, as even legitimate emails can sometimes appear suspicious or be mistaken for phishing.

---

Next: [Advanced Persistent Threat](Advanced_Persistent_Threat)