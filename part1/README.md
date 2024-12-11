# Part 1 of the problem set (ECB and CTR encryption)

## Setup
Before diving in, make sure to put your student ID in the `.env` file. This ID is used to generate unique ciphertext for Part 1 and unique passwords for Malan in Part 2. Don't skip this step unless you enjoy unnecessary confusion later!

---

# Background on ECB and CTR Encryption Modes

Encryption is a critical concept in cybersecurity, and understanding how data is protected is an essential skill. Two widely used encryption modes are **Electronic Codebook (ECB)** and **Counter (CTR)**. Here’s a brief overview to help you get started:

### **Electronic Codebook (ECB)**
ECB is the simplest encryption mode. Here’s how it works:
- The input data (e.g., an image or text) is divided into fixed-size blocks.
- Each block is encrypted independently using the same encryption key.

**Advantages**:
- Easy to implement.
- Fast and efficient for small amounts of data.

**Disadvantages**:
- Identical blocks of plaintext produce identical blocks of ciphertext.

Think of ECB like a simple substitution cipher for blocks: easy to understand but not always secure.

### **Counter (CTR)**
CTR takes a more sophisticated approach:
- Instead of encrypting the data blocks directly, CTR generates a unique "keystream" using a combination of a counter and the encryption key.
- Each data block is XORed with the corresponding part of the keystream to produce the ciphertext.

**Advantages**:
- Doesn’t reveal patterns in the data (e.g., the same plaintext blocks will produce different ciphertext blocks).
- Supports parallel processing, making it faster for larger datasets.
- Can also be used for decryption by reversing the XOR operation.

**Disadvantages**:
- Requires careful management of the counter value to avoid reusing keystreams, which could compromise security.

Think of CTR as turning encryption into a math problem: it’s more secure and versatile than ECB but a bit more complex.

### Why Are These Modes Important?
- ECB shows why simple encryption isn't enough in many cases. It's easy to implement but often leaks information.
- CTR demonstrates how encryption can be made more secure and flexible by introducing randomness and counter-based techniques.

By working through this problem set, you’ll implement and analyze these modes, gaining hands-on experience in cryptography. Ready to get started? 🚀

---

## Subpart 1: Encrypt Your Own Image
In this subpart, you'll implement **ECB** and **CTR** encryption modes in `encryption.py` and run them on your own uploaded image. This isn't just coding—it's a chance to play with pixels and patterns!

### Steps:

1. Implement the encryption methods in `encryption.py`.
2. Upload your own image and apply both ECB and CTR encryption.
3. After running the encryption, observe the results and note the differences between the encrypted images in `questions.txt`.

**Hint:** ECB mode tends to create recognizable patterns in the encrypted image. Think of it as leaving a digital breadcrumb trail.

---

## Subpart 2: Decrypt the ECB-Encrypted Text
Now, it's time to test your sleuthing skills. You'll decrypt an ECB-encrypted text using frequency analysis and crack the code like a true cipher detective!

### Steps:

1. Run the `frequency_analysis.py` script to analyze the frequency distribution of letters in the encrypted text.
   ```bash
   python frequency_analysis.py
   ```
2. Design your own frequency analysis approach to crack the ciphertext.
3. Once you've decrypted the text, answer the questions in `questions.txt`. 
4. Verify your solution by placing the decrypted text in `sol.txt` and running:
   ```bash
   python check.pyc
   ```

**Pro Tip:** This isn't just about the math—it's about creativity. Use your knowledge of English letter frequencies (hint: 'E' is popular) and your inner Sherlock to crack the code.

---

Good luck! Remember, every encrypted image and cracked ciphertext brings you closer to mastering the art of cryptography.