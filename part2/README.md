# Problem Set: Analyzing HTTP(S) Traffic and Breaking Encrypted Passwords

## Overview

This problem set combines network analysis and cryptographic concepts. Students will:
1. Capture and analyze HTTP traffic to retrieve a secret key.
2. Use the key to decrypt an encrypted `passwords.db` file.
3. Reverse engineer hashed passwords using a list of common passwords.

---

## Part 1: Capture the Secret Key

### Objective
Capture a secret key sent over HTTP using `tcpdump`.

### Instructions
1. Write a Python script to send an HTTP request and retrieve the secret key.
2. Use `tcpdump` to capture HTTP traffic.

### Boilerplate Code
```python
import requests

# Fetch secret key from a simulated server
response = requests.get("http://httpbin.org/anything")
print("Secret Key:", response.text)
```

### Simulated Response
The server responds with a JSON payload containing a secret key, e.g., `{ "secret": "mySecretKey123" }`.

### Capture Command
```bash
sudo tcpdump -A port 80
```

---

## Part 2: Decrypt the Encrypted Database

### Objective
Use the captured secret key to decrypt the `passwords.db` file, which contains usernames and hashed passwords.

### Provided File
- `passwords.db` (encrypted file in the same directory)

### Boilerplate Code
```python
from cryptography.fernet import Fernet

# Replace with the captured key
secret_key = b'mySecretKey123'
cipher = Fernet(secret_key)

# Decrypt the file
with open("passwords.db", "rb") as encrypted_file:
    encrypted_data = encrypted_file.read()

decrypted_data = cipher.decrypt(encrypted_data)

# Save the decrypted data
with open("decrypted_passwords.txt", "wb") as decrypted_file:
    decrypted_file.write(decrypted_data)

print("Decryption complete! Decrypted data saved in decrypted_passwords.txt.")
```

### Decrypted File Format (Example)
```
username1:5f4dcc3b5aa765d61d8327deb882cf99
username2:098f6bcd4621d373cade4e832627b4f6
```

---

## Part 3: Reverse Engineer Hashed Passwords

### Objective
Write a function to match hashed passwords against a list of common passwords.

### Provided Files
- `decrypted_passwords.txt` (from Part 2)
- `common_passwords.txt` (list of common passwords)

### Hashing Algorithm
MD5

### Boilerplate Code
```python
import hashlib

def crack_passwords(hash_file, password_list_file):
    # Load the hashes
    with open(hash_file, "r") as f:
        hashed_passwords = [line.strip().split(":") for line in f]

    # Load the list of common passwords
    with open(password_list_file, "r") as f:
        common_passwords = [line.strip() for line in f]

    cracked_passwords = {}

    # Attempt to crack each hash
    for username, hashed in hashed_passwords:
        for password in common_passwords:
            hashed_attempt = hashlib.md5(password.encode()).hexdigest()
            if hashed_attempt == hashed:
                cracked_passwords[username] = password
                break

    return cracked_passwords

# Example usage
cracked = crack_passwords("decrypted_passwords.txt", "common_passwords.txt")
print("Cracked Passwords:")
for user, password in cracked.items():
    print(f"{user}: {password}")
```

---

## Final Deliverables

1. `traffic.py`: Script to capture and extract the secret key.
2. `decrypt_db.py`: Script to decrypt the `passwords.db` file.
3. `crack_passwords.py`: Script to reverse engineer hashed passwords.

---

## Bonus Challenge

- Enhance the password cracking function to handle SHA-256 hashes and compare runtimes.

---

## Walkthrough

### Step-by-step Guide
1. **Capture the key**:
   - Run `tcpdump` to extract the secret key from HTTP traffic.
   - Use the key in the decryption script.
   
2. **Decrypt the database**:
   - Use the secret key to decrypt `passwords.db`.
   - Verify that the decrypted file contains usernames and hashed passwords.

3. **Reverse engineer passwords**:
   - Write a function to compare MD5 hashes with common passwords.
   - Test the function and document cracked passwords.

---

## Runtime Complexity

- **Decryption**: \( O(n) \), where \( n \) is the size of the database file.
- **Password Cracking**: \( O(m \cdot p) \), where \( m \) is the number of hashes and \( p \) is the number of common passwords.