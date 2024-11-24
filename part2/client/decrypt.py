from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

def decrypt_passwords(file_path, key):
    """
    Decrypt the passwords.db file using the provided key.
    """
    # convert key to byte format
    key = bytes.fromhex(key)

    try:
        with open(file_path, "rb") as encrypted_file:
            # Read the IV (first 16 bytes) and encrypted data
            iv = encrypted_file.read(16)
            encrypted_data = encrypted_file.read()

        # Create a cipher object and decrypt the data
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)

        return decrypted_data.decode()
    except Exception as e:
        print("Error decrypting the file:", e)
        return None

if __name__ == "__main__":
    secret_key = input("Enter the secret key you found from tcpdump: ").strip()
    file_path = "passwords.db"

    # Decrypt the passwords file
    decrypted_data = decrypt_passwords(file_path, secret_key)
    if decrypted_data:
        print("\nDecrypted Passwords:")
        print(decrypted_data)
    else:
        print("Failed to decrypt the passwords file.")
