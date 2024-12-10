import requests
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os
from collections import Counter
import sys

# Load environment variables from .env file
load_dotenv()

def get_text(base_url, student_id):
    """
    Makes a GET request to the /get_text endpoint to fetch a randomly selected encrypted text.

    Args:
        base_url (str): The base URL of the API (e.g., 'http://localhost:5000').
        student_id (str): The numeric Harvard ID of the student.

    Returns:
        str: The ciphertext response from the API.
    """
    try:
        response = requests.get(f"{base_url}/get_text", params={"id": student_id})
        response.raise_for_status()
        text = response.json()['response']
        return text
    except requests.RequestException as e:
        print(f"Error fetching text: {e}")
        sys.exit(1)

def plot_frequencies(base_url, student_id):
    """
    Fetches the ciphertext and plots the frequency of lowercase letters.

    Args:
        base_url (str): The base URL of the API (e.g., 'http://localhost:5000').
        student_id (str): The numeric Harvard ID of the student.

    Returns:
        None
    """
    # Get the ciphertext
    ciphertext = get_text(base_url, student_id)

    # Write to ciphertext file
    with open("./ciphertext.txt", "w") as f:
        f.write(ciphertext)
    
    # Filter for lowercase letters only
    lowercase_letters = [char for char in ciphertext if char.islower()]
    
    # Count frequencies of each character
    frequencies = Counter(lowercase_letters)
    
    # Sort characters by frequency in decreasing order
    sorted_items = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)
    characters = [item[0] for item in sorted_items]
    counts = [item[1] for item in sorted_items]
    
    # Plot the bar graph
    plt.figure(figsize=(10, 6))
    plt.bar(characters, counts, alpha=0.75, color='skyblue', edgecolor='black')
    plt.title('Character Frequencies (Lowercase Letters)', fontsize=14)
    plt.xlabel('Characters', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Show the plot
    plt.show()

# TODO: More sophisticated frequency analysis
# TODO: Write a function to check a given mapping (decrypts ciphertext automatically using your guess)

if __name__ == "__main__":
    # Check for student_id argument
    if len(sys.argv) != 1:
        print("Usage: python frequency_analysis.py")
        sys.exit(1)
    
    # Get the student_id from command-line arguments
    student_id = os.getenv("STUDENT_ID")
    
    # Check if student_id is numeric
    if not student_id.isdigit():
        print("Error: student_id must be numeric.")
        sys.exit(1)
    
    # Base URL for the Flask API
    base_url = os.getenv("SERVER_URL")
    if not base_url:
        print("Error: SERVER_URL not set in .env file.")
        sys.exit(1)
    
    # Plot frequencies
    plot_frequencies(base_url, student_id)