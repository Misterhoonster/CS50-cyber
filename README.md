# CS50 Cyber Problem Set

Welcome to the CS50 Cyber Problem Set! Designed for Harvard University's CS50, taught by Professor David Malan, this problem set introduces students to fundamental cybersecurity concepts through hands-on exercises and conceptual questions.

---

## Getting Started

To get started, follow these steps:

### 1. **Clone the Repository**
Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/Misterhoonster/CS50-cyber.git
cd CS50-cyber
```

### 2. **Set Up the `.env` File**
This file is essential for generating unique ciphertext for Part 1 and unique passwords for Malan in Part 2. Follow these steps carefully:

#### a. **Create the `.env` File**  
If it doesn’t already exist, create a file named `.env` in the root directory.

#### b. **Copy Contents from `.env.sample`**  
Copy everything from the provided `.env.sample` file into your `.env` file.

#### c. **Update the `STUDENT_ID` Variable**  
Replace the placeholder in the `.env` file with your Harvard ID:
```env
STUDENT_ID=YourHarvardIDHere
```

Save the file to ensure proper configuration.

### 3. **Explore the Parts**
The problem set is divided into three parts: `part1`, `part2`, and `part3`. Each part has its own directory with detailed instructions in its respective README file.

To start working on a specific part, navigate to its directory:
```bash
cd part1
```
Replace `part1` with `part2` or `part3` as needed.

---

## Problem Set Structure

### Part 1: ECB and CTR Encryption
- **Subpart 1**: Implement ECB and CTR encryption methods in `encryption.py` and apply them to an uploaded image. Compare results and observe patterns created by ECB mode.
- **Subpart 2**: Decrypt an ECB-encrypted text using frequency analysis, leveraging knowledge of English letter frequencies to crack the code.

### Part 2: HTTP and Password Cracking
- Simulate a network traffic sniffing scenario where sensitive data is transmitted via unencrypted HTTP. Extract a secret key and decrypt Malan's database to retrieve a hashed password. Finally, use brute-force techniques to crack the hashed password.

### Part 3: Signing and Authentication
- Explore the use of digital signatures to ensure message integrity and authenticity. Analyze flaws in naive signing mechanisms, refine them, and propose improved solutions to counteract potential vulnerabilities.

---

## Support
For additional assistance, refer to the detailed READMEs within each part or consult the CS50 course materials.

Happy hacking, and enjoy exploring the fascinating world of cybersecurity!