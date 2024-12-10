import requests
import sys
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def main():
    # Ensure the script is called with a Harvard ID argument
    if len(sys.argv) != 1:
        print("Usage: python malan_request.py")
        sys.exit(1)
    
    # Get the Harvard ID from the command-line argument
    student_id = os.getenv("STUDENT_ID")

    # Validate that the Harvard ID is numeric
    if not student_id.isdigit():
        print("Error: Harvard ID must be numeric.")
        sys.exit(1)

    # Define the URL and payload
    base_url = os.getenv("SERVER_URL")
    if not base_url:
        print("Error: SERVER_URL not set in .env file.")
        sys.exit(1)

    payload = {"id": student_id}

    try:
        # Send the GET request
        response = requests.get(base_url + "/fetch", params=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.RequestException as e:
        print(f"Error during request: {e}")

if __name__ == "__main__":
    main()
