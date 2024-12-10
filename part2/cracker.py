import hashlib
import sys

# TODO: Crack Malan's password using passwords.txt
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
    crack_password(hashed_password, password_file)
