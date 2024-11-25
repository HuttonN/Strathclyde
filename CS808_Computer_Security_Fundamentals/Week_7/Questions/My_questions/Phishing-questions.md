# Phishing - Questions

## Introduction

&nbsp;
<details>
<summary>
1. What is phishing?
</summary>

Phishing is a type of social engineering where attackers attempt to obtain sensitive information (e.g., login credentials, bank details) or trick users into downloading malware.
</details>

&nbsp;
<details>
<summary>
2. Describe the typical phishing attack flow.
</summary>

1. The attacker sends an email with a link or attachment.
2. The user clicks the link or downloads the attachment.
3. The attacker:
   - Collects sensitive information (e.g., credentials) from a fake website.
   - Installs malware on the user's device (e.g., via a drive-by download).
</details>

## Examples of Phishing

### Genuine Email Example

&nbsp;
<details>
<summary>
1. What characteristics made the genuine email appear suspicious?
</summary>

- Multiple links to click on.
- Lack of identifying information, except for a partial bank account number.
</details>

&nbsp;
<details>
<summary>
2. How was it determined that the email was genuine?
</summary>

The **Received From domain** matched the **From domain** in the email overview.
</details>

### Phishing Email Example 1

&nbsp;
<details>
<summary>
1. What characteristics identified this email as phishing?
</summary>

- Sent in an unfamiliar language.
- Strange formatting and phrasing (e.g., links labeled "Wife," "Man," etc.).
- Mismatched **From domain** ("lemustdesdeals.com" vs. "Bon Prix").
</details>

&nbsp;
<details>
<summary>
2. How can attackers spoof the From field in emails?
</summary>

Attackers can use an SMTP (Simple Mail Transfer Protocol) server and mailing software to spoof the From field.
</details>

&nbsp;
<details>
<summary>
3. What is SPF, and how does it help mitigate phishing?
</summary>

The **Sender Policy Framework (SPF)** verifies that the IP sending the email is authorized by the domain's SPF record. If the IP does not match, the email can be flagged as spam.
</details>

### Phishing Email Example 2

&nbsp;
<details>
<summary>
1. What characteristics identified this email as phishing?
</summary>

- Lacked identifying information.
- Created urgency (e.g., "login as soon as possible").
- Hovering over the link revealed it directed to a domain not associated with the claimed sender.
- Mismatched domains in the **Received From** and **From fields**.
</details>

### Spear Phishing

&nbsp;
<details>
<summary>
1. How does spear phishing differ from generic phishing?
</summary>

Spear phishing targets specific individuals using personalized information, unlike generic phishing, which sends the same email to many addresses.
</details>

&nbsp;
<details>
<summary>
2. Why is spear phishing harder to detect?
</summary>

Spear phishing emails are personalized, making them appear more legitimate and convincing.
</details>

## Common Techniques in Phishing

&nbsp;
<details>
<summary>
1. List four social engineering techniques commonly used in phishing emails.
</summary>

1. **Authority**: Impersonating a trusted entity (e.g., a bank, employer).
2. **Impersonation**: Posing as a legitimate organization or individual.
3. **Pressure and Solution**: Creating urgency (e.g., "Your account will be suspended unless...").
4. **Pretext**: Providing a convincing scenario to justify the request (e.g., account verification).
</details>

## Mitigating Phishing Attacks

&nbsp;
<details>
<summary>
1. How can organizations raise awareness about phishing?
</summary>

- Employee training to recognize phishing attempts.
- Using penetration testers to simulate phishing attacks and provide follow-up training.
</details>

&nbsp;
<details>
<summary>
2. What technical solutions can help mitigate phishing risks?
</summary>

- Using **SPF** to verify email sender authenticity.
- Employing tools to filter and block phishing emails.
</details>

&nbsp;
<details>
<summary>
3. What are some best practices for individuals to avoid falling victim to phishing?
</summary>

- Verify links by hovering over them to check the destination URL.
- Avoid downloading attachments from unknown sources.
- Report suspected phishing emails.
</details>

## Risks of Clicking Phishing Links

&nbsp;
<details>
<summary>
1. What are two main risks of clicking phishing links?
</summary>

1. **Malware Installation**: Drive-by downloads can install malware without the user's awareness.
2. **Credential Theft**: Phishing websites mimic legitimate ones to collect login credentials.
</details>

## Key Takeaways

&nbsp;
<details>
<summary>
1. Why is vigilance important in detecting phishing emails?
</summary>

Phishing relies on human error, and some legitimate emails can appear suspicious or be mistaken for phishing, requiring careful scrutiny.
</details>
