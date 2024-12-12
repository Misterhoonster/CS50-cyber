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

def plot_frequencies(ciphertext):
    """
    Analyzes and plots the frequency of lowercase letters in the ciphertext.

    Args:
        ciphertext (str): The encrypted text.

    Returns:
        None
    """
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

# TODO: Fill in freq analysis function
def frequency_analysis(ciphertext):
    """
    Provides a starting point for students to implement frequency analysis.

    Args:
        ciphertext (str): The encrypted text.

    Returns:
        dict: A guessed mapping of encrypted characters to plaintext characters.
    """
    # HINT: Use English letter frequencies to guess mappings.
    # Example: English letters "E", "T", "A", "O" are the most frequent in plaintext.
    # Compare these to the most frequent characters in the ciphertext.

    # TODO: Count letter frequencies in ciphertext
    lowercase_letters = [char for char in ciphertext if char.islower()]
    frequencies = Counter(lowercase_letters)
    
    # TODO: Sort by frequency
    sorted_items = sorted(frequencies.items(), key=lambda item: item[1], reverse=True)
    
    # TODO: Guess mappings based on frequency
    guessed_mapping = {}
    english_frequencies = "ETAOINSHRDLCUMWFGYPBVKJXQZ"  # Common letters in decreasing order
    encrypted_characters = [item[0] for item in sorted_items]  # Sorted ciphertext characters by frequency

    # TODO: Create a mapping by aligning frequent letters
    for i, char in enumerate(encrypted_characters):
        if i < len(english_frequencies):
            guessed_mapping[char] = english_frequencies[i].lower()

    # TODO: Print guessed mapping for debugging
    print("Guessed Mapping (encrypted -> plaintext):", guessed_mapping)

    return guessed_mapping

# TODO: Fill in decrypt function
def decrypt_with_mapping(ciphertext, mapping):
    """
    Decrypts the ciphertext using a given character mapping.

    Args:
        ciphertext (str): The encrypted text.
        mapping (dict): A dictionary mapping encrypted characters to plaintext characters.

    Returns:
        str: The decrypted text.
    """
    # TODO: Replace each encrypted character with its mapped plaintext character
    decrypted_text = ''.join(mapping.get(char, char) for char in ciphertext)
    return decrypted_text

if __name__ == "__main__":
    # Check for student_id argument
    if len(sys.argv) != 1:
        print("Usage: python frequency_analysis.py")
        sys.exit(1)
    
    # Get the student_id from environment variables
    student_id = os.getenv("STUDENT_ID")
    
    if not student_id.isdigit():
        print("Error: student_id must be numeric.")
        sys.exit(1)
    
    # Base URL for the Flask API
    base_url = os.getenv("SERVER_URL")
    if not base_url:
        print("Error: SERVER_URL not set in .env file.")
        sys.exit(1)
    
    # Fetch the ciphertext
    ciphertext = get_text(base_url, student_id)
    
    # Write to ciphertext file
    with open("./ciphertext.txt", "w") as f:
        f.write(ciphertext)
    
    # Plot frequencies
    # plot_frequencies(ciphertext)
    
    # Perform frequency analysis and decrypt
    guessed_mapping = frequency_analysis(ciphertext)
    decrypted_text = decrypt_with_mapping(ciphertext, guessed_mapping)
    
    # Print decrypted text (partial decryption with guessed mapping)
    print("\nDecrypted Text (partial):")
    print(decrypted_text[:500])  # Print the first 500 characters for review

    # HINT: Improve the guessed mapping iteratively and try decrypting again!