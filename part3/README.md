# **Part 3 of the problem set (Signing and Authentication)**

## **Context**
David Malan has a sneaking suspicion that someone is intercepting his messages and might be impersonating him. He is worried about a man-in-the-middle attack and wants to send a message to Mr. Duck to alert him securely. You've turned over a new leaf, and after seeing all that is wrong with the world, you decide to do some good—you will help them facilitate their message exchange privately using a secure signing and authentication mechanism.

This section of the problem set will give students hands-on experience with:

- How signatures ensure the integrity and authenticity of messages.
- Exploring the shortcomings of signing mechanisms.
- Understanding attacks on signed messages and how to mitigate them.

In this phase, assume David is trying to communicate securely with his friend (you) while an attacker intercepts their communication. You will take on the role of David’s friend, analyzing and improving his signing mechanism.

---

## **Steps**

### **Part 1: David's Naive Signing Mechanism**
David did well in his CS security course at the College. He decides to append a signature to his plaintext messages. Specifically, David encrypts his public key using his private key to create the signature. However, this naive approach has its flaws.

1. **Scenario**:
   - David uses the same signature for all his messages.
   - The attacker can see the communication channel.

2. **Analyze the Flaw**:
   (a) Why is using the same signature for every message problematic? What could an attacker possibly do with this repeated signature?

   (b) Suppose the attacker appends their own random number (of the same length) as the signature to the intercepted messages. When you receive two identical messages with different signatures, how would you identify which one belongs to David?

3. **Write your answers in `answers.txt`.**

---

### **Part 2: David’s Improved Mechanism**
After learning about the flaws in his first approach, you inform David of the potential vulnerabilities. David decides to act smarter this time. Instead of encrypting his public key, he chooses to encrypt the cleartext message itself with his private key and use it as the signature.

This means that:
- Each message gets a unique signature.
- An attacker cannot modify the content of a message without invalidating the signature.

David is confident that:
- Message integrity is preserved.
- Authenticity is ensured because only he has the private key.

1. **Analyze David’s Claims**:
   (a) Which one of David’s assumptions about his new approach is wrong? Why?

2. **Write your analysis in `answers.txt`.**

---

### **Part 3: Refining the Signature Mechanism**
Based on the analysis in Part 2, you identify where David’s new approach falls short. To address these issues and ensure that an attacker cannot perform malicious attacks, propose a refined signature mechanism.

1. **Propose a Solution**:
   - What should David modify in his signing mechanism to fully address the vulnerabilities from Part 2?

2. **Write your solution in `answers.txt`.**

---

## **What You Will Submit**
Ensure you complete the following:
- Answer all questions in `answers.txt`.
- Provide clear and concise explanations for each part of the problem.

Good luck, and remember: security is about being one step ahead of the attackers!