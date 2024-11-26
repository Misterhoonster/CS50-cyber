
Here is the updated `README.md` content with the steps outlined:

---

# Part 1 of the problem set (ECB and CTR encryption)

## Subpart 1
In this subpart, students will be asked to implement ECB and CTR encryption modes based on their knowledge learned during a lecture. On our part, we provide an empty python script file, where students will write their code. In order to make the problem more interesting, we would like to ask students to upload their own image and apply two types of encrytpion on it. Then, they should briefly describe the differences between ECB and CTR and their implications on security in the comment section of their code. 

## Subpart 2
In the second subpart, students will carry out frequency distribution analysis. They only need to writte a code to plot a graph of frequency distribution, we will provide an ECB encrypted text. Here are the step-by-step explanation of this subpart:

1. **Launch the Flask server**:
   ```
   python app.py
   ```
2. **Request the ECB encrypted text**:

   Students need to send their Harvard ID to the server, which would uniquely identify them.
   ```
   curl "http://localhost:8080/get_text?id=123"
   ```
   The server will return an ECB encrypted text to a student. They would get something like:
   ```
   {"selected_text":"B QQWBPS WXY WS BYN WWSS XWTSSVD WWVV BSNSQ NBUS FYYK BKNWPSV"}
   ```
3. **After performing the frequency disitrbution analysis and decrypting the text, students would check whether their answer is correct by sending the check request to the server**
   ```
   curl "http://localhost:8080/check?id=123&text=all%20happy%20families%20are%20alike%20each%20unhappy%20family%20is%20unhappy%20in%20its%20own%20way"
   ```
   Here `%20` represents a space, but later we would consider making sending the request much easier for the students.

   If their answer is correct, then the server will send the "Correct!" message; otherwise, "Try Again!" would be received.

**Important point**:
- We are thinking of having a launched server that will handle the backend stuff like storing the encrypted texts for each student's ID and checking the answer. Right now, we are using a smiple .txt file to store the mapping (Student ID - encrypted text); however, we are open to more complex solutions that would make the grading process easier for the CS50 stuff. 
- Also, we are planning to have a pool of plaintexts, from which a randomly selected text would be given to a student. If there were only one text, it would be too trivial for students. So, we hope this would add some complexity to the task and makes it more engaging.

  
# Part 2 of the problem set

# **Password Cracking Pset (Beta Version)**

This beta version hosts a simple Flask web server locally on `localhost:8080`. For the final problem set, we will deploy the server and use the deployed URL instead. The server code is located in the `server` folder, while the student code resides in the `client` folder.

## **Context**
You are at Capital One Cafe with David Malan and spot him in the corner on his laptop. As the conniving CS50 student you are, you decide to inspect network traffic to snoop on Malan's activity. You already have a suspicious `passwords.db` file at your disposal connected to Malan's account, but unfortunately, it's encrypted. Luckily enough, you find that Malan sends an unencrypted HTTP request over the network, and you spot his secret key. You use this key to break the encryption, but bummer, the password is still hashed. Luckily, you have in your arsenal a list of the 25k most common passwords—could Malan be using one of these? You check by hashing each plaintext password against your hashed copy and find that bingo—it is one of them!

This section of the problem set will give students hands-on experience with:

- The dangers of unencrypted HTTP communication.
- Brute-force techniques for common password cracking (and the importance of avoiding weak passwords).
- The SHA-256 hashing algorithm, commonly used for secure applications.

---

## **Steps**

### **Part 1: Capture the Secret Key**
In this task, you will simulate snooping on a public network to capture a secret key sent over an insecure HTTP request.

1. **Run the Flask Web Server**:
   - Navigate to the `server` folder and run:
     ```bash
     python app.py
     ```

2. **Run `tcpdump` to Capture Traffic**:
   - Open a terminal and execute:
     ```bash
     sudo tcpdump -i any port 8080 -A
     ```

3. **Send the HTTP Request**:
   - Use the following code in `traffic.py` to simulate David Malan (as the web server admin) sending a request for a secret key:
     ```python
     import requests

     # Send secret key over network
     url = "http://localhost:8080/fetch"
     payload = {"name": "INSERT NAME HERE"}

     requests.get(url, params=payload)
     ```
   - Run the script:
     ```bash
     python traffic.py
     ```
   - Observe the terminal output from `tcpdump` to find the secret key sent over the network.

---

### **Part 2: Decrypt the Encrypted Database**
Using the captured secret key, decrypt the `passwords.db` file to extract the plaintext username and hashed password.

1. **Fetch `passwords.db`**:
   - Navigate to the web server (e.g., `http://localhost:8080/fetch`) and enter your name to download your custom `passwords.db` file. 
   - Move the downloaded file into the `client` folder.

2. **Run `decrypt.py`**:
   - The following code decrypts the file using the captured secret key:
     ```python
     from Crypto.Cipher import AES
     from Crypto.Util.Padding import unpad

     def decrypt_passwords(file_path, key):
         key = bytes.fromhex(key)

         try:
             with open(file_path, "rb") as encrypted_file:
                 iv = encrypted_file.read(16)
                 encrypted_data = encrypted_file.read()

             cipher = AES.new(key, AES.MODE_CBC, iv)
             decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

             return decrypted_data.decode()
         except Exception as e:
             print("Error decrypting the file:", e)
             return None

     if __name__ == "__main__":
         secret_key = input("Enter the secret key you found from tcpdump: ").strip()
         file_path = "passwords.db"

         decrypted_data = decrypt_passwords(file_path, secret_key)
         if decrypted_data:
             print("\nDecrypted Passwords:")
             print(decrypted_data)
         else:
             print("Failed to decrypt the passwords file.")
     ```
   - Run the script:
     ```bash
     python decrypt.py
     ```

3. **Output**:
   - The script will output the username and hashed password in the format: 
     ```
     username: hashed_password
     ```

---

### **Part 3: Reverse Engineer Hashed Passwords**
Using the `passwords.txt` file (RockYou Top 25k list), brute-force the hashed password to find the plaintext password.

1. **Write `cracker.py`**:
   - The following script hashes each password in `passwords.txt` and compares it to the hashed password:
     ```python
     import hashlib
     import sys

     def crack_password(hashed_password, password_file):
         with open(password_file, "r") as file:
             passwords = file.read().splitlines()

         for password in passwords:
             current_hash = hashlib.sha256(password.encode()).hexdigest()
             if current_hash == hashed_password:
                 print(f"Match found! Password: {password}")
                 return password

         print("No match found.")
         return None

     if __name__ == "__main__":
         if len(sys.argv) != 3:
             print("Usage: python cracker.py <hashed_password> <password_file>")
             sys.exit(1)

         hashed_password = sys.argv[1]
         password_file = sys.argv[2]

         crack_password(hashed_password, password_file)
     ```

2. **Run the Script**:
   - Run the script with the hashed password and the path to `passwords.txt`:
     ```bash
     python cracker.py <hashed_password> passwords.txt
     ```

3. **Output**:
   - The script will output the plaintext password if a match is found.

---

## **Future Improvements**
- Add an endpoint to the web server to verify the student's name and password combination.
- Deploy the web server to a live URL for ease of use.

--- 

This completes the setup and steps for this beta version.
