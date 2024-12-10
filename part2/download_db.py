import requests
import sys
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def download_encrypted_db(base_url, student_id, output_file="passwords.db"):
    """
    Downloads the encrypted database for the given student ID.

    Args:
        base_url (str): The base URL of the API.
        student_id (str): The student ID.
        output_file (str): The name of the local file to save the database.

    Returns:
        None
    """
    try:
        # Make POST request to the /download API
        response = requests.post(f"{base_url}/download", data={"id": student_id}, stream=True)
        response.raise_for_status()

        # Write the response content to the output file
        with open(output_file, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Encrypted database saved to {output_file}")
    except requests.RequestException as e:
        print(f"Error during API call: {e}")
    except IOError as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    # Ensure student_id is passed as an argument
    if len(sys.argv) != 1:
        print("Usage: python download_db.py")
        sys.exit(1)

    # Extract student_id from command-line arguments
    student_id = os.getenv("STUDENT_ID")

    # Define the base URL
    base_url = os.getenv("SERVER_URL")
    if not base_url:
        print("Error: SERVER_URL not set in .env file.")
        sys.exit(1)

    # Call the function to download the database
    download_encrypted_db(base_url, student_id)