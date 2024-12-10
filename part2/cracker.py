import hashlib
import sys

def crack_password(hashed_password, password_file):
    # TODO: read passwords from the file
    with open(password_file, "r") as file:
        passwords = file.read().splitlines()

    # TODO: attempt to match the hash
    for password in passwords:
        # Hash the current password
        current_hash = hashlib.sha256(password.encode()).hexdigest()

        # Check if it matches the given hash
        if current_hash == hashed_password:
            print(f"Match found! Password: {password}")
            return password

    print("No match found.")
    return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python cracker.py <password_file>")
        sys.exit(1)
    
    hashed_password = input("Enter the hashed password: ").strip()

    # Command-line arguments
    password_file = sys.argv[1]  # Path to passwords.txt

    # Start brute force attack
    crack_password(hashed_password, password_file)
