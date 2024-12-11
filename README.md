# CS50 Cyber Problem Set

Welcome to the CS50 Cyber Problem Set! Designed for Harvard University's CS50, taught by Professor David Malan, this problem set introduces students to fundamental cybersecurity concepts through hands-on exercises and conceptual questions.

---

## Getting Started

To get started, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Misterhoonster/CS50-cyber.git
   ```
   Navigate to the cloned directory:
   ```bash
   cd CS50-cyber
   ```

2. **Explore the Parts**:
   - The problem set is divided into three parts: `part1`, `part2`, and `part3`. 
   - Each part has its own directory and README file with detailed instructions and background information.

   To start working on a specific part:
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