import os
import hashlib
from flask import Flask, request, jsonify, send_file
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import random

app = Flask(__name__)

# Encryption configuration
AES_BLOCK_SIZE = 16

def hash_name(name):
    """Hash the name using SHA-256 and return the first 16 bytes (AES-128 key)."""
    hashed = hashlib.sha256(name.encode()).digest()
    return hashed[:AES_BLOCK_SIZE]

@app.route('/')
def home():
    """Homepage with a form to download the encrypted passwords file."""
    return '''
    <form action="/download" method="post">
        <label for="name">Enter your name (no caps, no spaces):</label>
        <input type="text" id="name" name="name" required>
        <button type="submit">Download Passwords</button>
    </form>
    '''

@app.route('/download', methods=['POST'])
def download():
    """Encrypt and provide the passwords file for download."""
    name = request.form.get('name')

    # Validate input
    if not name or ' ' in name or not name.islower():
        return "Invalid name. Use only lowercase letters without spaces.", 400

    # Load passwords from passwords.txt
    with open("passwords.txt", "r") as file:
        passwords = file.read().splitlines()

    # Randomly select a password
    selected_password = random.choice(passwords)

    # Hash the selected password using SHA-256
    hashed_password = hashlib.sha256(selected_password.encode()).hexdigest()

    # Update plaintext_passwords
    plaintext_passwords = f"davidjmalan:{hashed_password}"

    encrypted_filename = "passwords.db"

    # Encrypt using AES-128
    key = hash_name(name)
    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv
    encrypted_data = cipher.encrypt(pad(plaintext_passwords.encode(), AES_BLOCK_SIZE))

    # Save the encrypted file
    with open(encrypted_filename, "wb") as f:
        f.write(iv + encrypted_data)

    # Provide the file for download
    return send_file(encrypted_filename, as_attachment=True)

@app.route('/fetch', methods=['GET'])
def fetch_key():
    """Return the secret key (hashed name) in a JSON response."""
    name = request.args.get('name')
    print(name)
    # Validate input
    if not name or ' ' in name or not name.islower():
        return jsonify({"error": "Invalid name. Use only lowercase letters without spaces."}), 400

    # Return the hashed key
    secret_key = hash_name(name)
    return jsonify({"secret_key": secret_key.hex()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
