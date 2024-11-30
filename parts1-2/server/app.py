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


def ctr(text):    
    counter = 0
    cipher_text = ""
    for char in text:
        if char != " ":
            key = (counter % 26) + 1  
            random_number = (ord(char) + key) % 26 
            cipher_char = chr(random_number + 64)
            cipher_text += cipher_char
            counter += 1 
        else:
            cipher_text += char  
    
    return cipher_text

def ecb(text): 
    ecb_map = {}   
    cipher_text = ""
    for char in text:
        if char != " ":
            if char in ecb_map:
                cipher_text += ecb_map[char]
            else:
                random_number = random.randint(1, 26)
                while chr(random_number + 64) in ecb_map:
                    random_number = random.randint(1, 26)
                ecb_map[char] = chr(random_number + 64)
                cipher_text += ecb_map[char]
        else:
            cipher_text += char
    
    return cipher_text


def check_id_exists(student_id):
    """Check if the given student ID already exists in mapping.txt."""
    try:
        with open("mapping.txt", "r") as file:
            for line in file:
                if line.startswith(student_id + " - "):
                    return True
    except FileNotFoundError:
        # If mapping.txt does not exist, assume the ID does not exist
        return False
    return False

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



@app.route('/get_text', methods=['GET'])
def get_text():
    """Return a randomly selected text from texts.txt."""
    
    student_id = request.args.get('id')
    
    # Validate input: Ensure student_id is provided and is numeric
    if not student_id or not student_id.isdigit():
        return jsonify({"error": "Invalid ID. Please provide a numeric Harvard ID."}), 400
    

    # Return already selected text for existing ID
    with open("mapping.txt", "r") as file:
        for line in file:
            if line.strip() == "":
                break
            id_in_map, text_in_map = line.strip().split(' - ')
            if id_in_map == student_id:
                 # Return the existing text for this ID
                return jsonify({"text": text_in_map.strip().split('|')[1]})

    try:
        # Load texts from texts.txt file
        with open("texts.txt", "r") as excerpts:
            texts = excerpts.read().splitlines()
        
        # Randomly select one text line and encrypt it
        selected_text = random.choice(texts)
        encrypted_text = ecb(selected_text)
        
        with open("mapping.txt", "a") as mapping:
            # Store mapping (id - text) in mapping.txt
            mapping.write(f"{student_id} - {selected_text}|{encrypted_text}\n")
        
        # Return the selected text as JSON response
        return jsonify({"selected_text": encrypted_text})
    
    except FileNotFoundError:
        return jsonify({"error": "Please try again!"}), 500


@app.route('/check', methods=['GET'])
def check():
    """
    Check if the provided ID and text match the mapping in mapping.txt.
    """
    student_id = request.args.get('id')
    submitted_text = request.args.get('text')

    # Validate input
    if not student_id or not submitted_text:
        return jsonify({"error": "ID and text are required."}), 400
    
    try:
        with open('mapping.txt', 'r') as file:
            for line in file:
                if line.strip() == "":
                    break
                id_in_map, text_in_map = line.strip().split(' - ')
                if id_in_map == student_id and text_in_map.strip().split("|")[0] == submitted_text:
                    return jsonify({"message": "Correct!"})
        return jsonify({"message": "Try Again!"})
    except Exception as e:
        print(f"Error while reading the mapping")
        return False


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
