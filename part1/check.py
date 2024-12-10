import os
from dotenv import load_dotenv
import requests
import sys

# Load environment variables from .env file
load_dotenv()

def check(base_url, student_id):
    """
    Makes a GET request to the /check1 endpoint to verify if the ID and text match the mapping.

    Args:
        base_url (str): The base URL of the API (e.g., 'http://localhost:5000').
        student_id (str): The numeric Harvard ID of the student.

    Returns:
        str: "Solved!!" if the text matches, otherwise "Try again :(".
    """
    try:
        # Read submitted_text from sol.txt
        with open("sol.txt", "r") as file:
            submitted_text = file.read().strip()

        # Make GET request to the API
        response = requests.get(f"{base_url}/check1", params={"id": student_id, "text": submitted_text})
        response.raise_for_status()

        # Check the API response
        if response.json().get("response", False):
            return "Solved!!"
        else:
            return "Try again :("
    except FileNotFoundError:
        print("Error: 'sol.txt' file not found.")
        return "Missing solution text."
    except requests.RequestException as e:
        print(f"Error checking text: {e}")
        return "Request failed."

if __name__ == "__main__":
    # Ensure student_id is passed as an argument
    if len(sys.argv) != 1:
        print("Usage: python check.py")
        sys.exit(1)
    
    # Extract student_id from command-line arguments
    student_id = os.getenv("STUDENT_ID")
    
    # Get the base URL from the .env file
    base_url = os.getenv("SERVER_URL")
    if not base_url:
        print("Error: SERVER_URL not set in .env file.")
        sys.exit(1)

    # Call the check function and print the result
    result = check(base_url, student_id)
    print(result)
