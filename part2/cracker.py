import hashlib
import sys

def hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

# TODO: Crack Malan's password using passwords.txt
def crack_password(hashed_password, password_file):
    passwords = []
    with open(password_file, 'r') as f:
        passwords = f.readlines()
    
    for password in passwords:
        if hash(password.strip()) == hashed_password:
            return "Cracked password: " + password.strip()
    return "Password not found :("

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python cracker.py <password_file>")
        sys.exit(1)
    
    hashed_password = input("Enter the hashed password: ").strip()

    # Command-line arguments
    password_file = sys.argv[1]  # Path to passwords.txt

    # Start brute force attack
    cracked_password = crack_password(hashed_password, password_file)
    print(cracked_password)
