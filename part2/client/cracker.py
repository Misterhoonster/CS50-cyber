import hashlib
import sys

def crack_password(hashed_password, password_file):
    # Read passwords from the file
    with open(password_file, "r") as file:
        passwords = file.read().splitlines()

    # Attempt to match the hash
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
    if len(sys.argv) != 3:
        print("Usage: python cracker.py <hashed_password> <password_file>")
        sys.exit(1)

    # Command-line arguments
    hashed_password = sys.argv[1]  # Example: "5d41402abc4b2a76b9719d911017c592"
    password_file = sys.argv[2]  # Path to passwords.txt

    # Start brute force attack
    crack_password(hashed_password, password_file)
