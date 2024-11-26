Here is the updated `README.md` content with the steps outlined:

---

# **Sending secure messages with asymmetric encryption (Beta Version)**

This beta version hosts a simple Flask web server locally on `localhost:8080`. For the final problem set, we will deploy the server and use the deployed URL instead. The server code is located in the `server` folder, while the student code resides in the `client` folder.

## **Context**
David Malan has a sneaking suspicion that someone is spying him, and wants to send a message to Mr. Duck to alert him. However, he wants to avoid tipping off his spy. You've turned over a new leaf, and after seeing all that is wrong with the world, you decide to do some good – you will help them facilitate their message exchange privately, using the PGP encryption system.

This section of the problem set will give students hands-on experience with:

- the mechanics of encryption, signing, and key management.
- how encryption integrates into systems.


## **Background on Email Encryption**
[Insert brief overview of email encryption]
- Asymmetric encryption (public/private key pairs).
- How PGP ensures confidentiality, integrity, and authenticity.
- Common challenges in secure email communication.

## **Steps**

### **Part 1: Generate Key Pairs**
In this task, you will generate your own PGP key pair using a Python library like `gnupg`.

```python
import gnupg
gpg = gnupg.GPG()
input_data = gpg.gen_key_input(name_email="student@example.com", passphrase="securepass")
key = gpg.gen_key(input_data)
print("Key generated:", key)
```

---

### **Part 2: Exchange Public Keys**
Here, you will share your public keys `publickey.asc` with a partner, and import your partner's public key.

1. **Export public key:**
```bash
gpg --export --armor your_email@example.com > publickey.asc
```

2. **Import a partner’s public key:**
```bash
gpg --import partner_publickey.asc
```

---

### **Part 3: Encrypt and Sign an Email**
1. **Encrypt**

- Here, you will digitally sign a plaintext email/message, and then encrypt it using your partner's public key. Afterwards, send it using either an email client/code.
  ```python
  encrypted_data = gpg.encrypt("This is a secret email.", recipients="partner@example.com")
  with open("email.gpg", "wb") as f:
      f.write(str(encrypted_data))
  ```

2. **Sign**
- After encrypting your email, you can digitally sign it using the following code:
  ```python
  signed_data = gpg.sign("This is a signed email.", passphrase="securepass")
  with open("signed_email.txt", "wb") as f:
      f.write(str(signed_data))
  ```


### **Part 4: Decrypt and verify Email**

1. **Decrypt**
Once you've received an encrypted email, decrypt it using your private key, and verify the signature.

```python
with open("email.gpg", "rb") as f:
    encrypted_message = f.read()
decrypted_data = gpg.decrypt(encrypted_message, passphrase="securepass")
print("Decrypted message:", decrypted_data)
```

2. **Verify**
```python
verified = gpg.verify(decrypted_data)
print("Signature valid:", verified.valid)
```

---

## **Future Improvements**
- 

--- 
