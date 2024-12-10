# **Part 2 of the problem set (HTTP and password cracking)**

## **Context**
You are at Capital One Cafe with David Malan and spot him in the corner on his laptop. As the conniving CS50 student you are, you decide to inspect network traffic to snoop on Malan's activity. You already have a suspicious `passwords.db` file at your disposal connected to Malan's account, but unfortunately, it's encrypted. Luckily enough, you find that Malan sends an unencrypted HTTP request over the network, and you spot his secret key. You use this key to break the encryption, but bummer, the password is still hashed. Luckily, you have in your arsenal a list of the 25k most common passwords—could Malan be using one of these? You check by hashing each plaintext password against your hashed copy and find that bingo—it is one of them!

This section of the problem set will give students hands-on experience with:

- The dangers of unencrypted HTTP communication.
- Brute-force techniques for common password cracking (and the importance of avoiding weak passwords).
- The SHA-256 hashing algorithm, commonly used for secure applications.

---

## **Steps**

### **Step 1: Download Malan's Database**
Before you can even begin to unravel the mystery of Malan's account, you need his encrypted `passwords.db` file. Lucky for you, there's a script for that!

1. Run the following command to download Malan's database locally:
   ```bash
   python download_db.py
   ```

   This will fetch the suspicious `passwords.db` file connected to Malan's account and save it locally for decryption later.

---

### **Step 2: Sniff the Traffic**
Now comes the sneaky part. Malan, in all his wisdom, decides to send a secret key over an unencrypted HTTP request. It's your job to intercept it—ethically, of course, in this controlled environment.

1. Start sniffing for traffic at Capital One by running:
   ```bash
   sudo tcpdump -i any port 80 -A
   ```

2. While `tcpdump` is running, simulate Malan's unsafe HTTP request by executing:
   ```bash
   python malan_request.pyc
   ```

3. Observe the terminal output from `tcpdump`. Look closely—you’ll find the secret key hidden in the network traffic. 

   **Hint:** Keep an eye out for something resembling `key=...`. That’s the golden ticket!

4. After finding the secret key, answer the first question in `questions.txt` about the security implications of sending sensitive data over unencrypted HTTP.

---

### **Step 3: Decrypt the Encrypted Database**
With the secret key in hand, you’re now ready to unlock Malan’s encrypted database and reveal its secrets.

1. Run the following script, replacing `<your_key>` with the secret key you found in Step 2:
   ```bash
   python decrypt.py
   ```

2. The script will output the username and hashed password from the `passwords.db` file. 

   Example output:
   ```
   username: hashed_password
   ```

   Congrats! You’re halfway there.

---

### **Step 4: Crack the Hashed Password**
Now comes the fun part—brute-forcing Malan’s hashed password. Using the `passwords.txt` file (a list of the 25k most common passwords), you’ll find the plaintext password.

1. Implement the `crack_password` function in `cracker.py`:

2. Run the script with the hashed password from Step 3 and the path to `passwords.txt`:
   ```bash
   python cracker.py <hashed_password> passwords.txt
   ```

3. The script will output the plaintext password if a match is found.

   **Hint:** Malan probably didn’t pick a very strong password.

4. Once you’ve cracked the password, answer the second question in `questions.txt` about the implications of using common passwords.

---

### **Step 5: Check Your Work**
Finally, make sure you got everything right. Use the `check.pyc` script to verify your cracked password.

1. Run the following command:
   ```bash
   python check.pyc
   ```

2. Enter the username and plaintext password when prompted. If you’ve done everything correctly, you’ll get a congratulatory message. If not, it’s back to the drawing board!

---

Good luck, and remember—use your powers for good (and to ace this problem set)!
