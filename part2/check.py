import requests
import sys
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def check(base_url, student_id, password):
    """
    Test the student's ID and password combination using the /check2 API endpoint.

    Args:
        base_url (str): The base URL of the API.
        student_id (str): The student's ID.
        password (str): The password to test.

    Returns:
        str: "Success!!" if the API response is True, otherwise "Try again :(".
    """
    try:
        # Make GET request to the /check2 API
        response = requests.get(f"{base_url}/check2", params={"id": student_id, "password": password})
        response.raise_for_status()

        # Check the API response
        if response.json().get("response"):
            return "Success!!"
        else:
            return "Try again :("
    except requests.RequestException as e:
        print(f"Error during API call: {e}")
        return "Request failed."

if __name__ == "__main__":
    # Ensure student_id and password are passed as arguments
    if len(sys.argv) != 1:
        print("Usage: python test_password.py")
        sys.exit(1)

    # Extract arguments
    student_id = os.getenv("STUDENT_ID")
    password = input("Enter the cracked password: ").strip()

    # Define the base URL
    base_url = os.getenv("SERVER_URL")
    if not base_url:
        print("Error: SERVER_URL not set in .env file.")
        sys.exit(1)

    # Call the function and print the result
    result = check(base_url, student_id, password)
    print(result)