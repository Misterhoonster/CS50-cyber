import hashlib
import sys

def hash(text):
    return hashlib.sha256(text.encode()).hexdigest()

# TODO: Use a brute-force approach to crack Malan's password
# TODO: Return either the cracked password or that the password was not found
def crack_password(hashed_password, password_file):
    pass

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
