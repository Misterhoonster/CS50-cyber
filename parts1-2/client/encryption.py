import random
from PIL import Image
import os
from Crypto.Cipher import AES

def image_to_list(image_path):
    """
    Converts a grayscale image file to a 2D list of pixel values.
    
    Parameters:
        image_path (str): Path to the image file.
    
    Returns:
        list: 2D list of pixel values.
    """
    img = Image.open(image_path)
    img = img.convert('L')  # Convert image to grayscale (L mode)
    pixels = list(img.getdata())
    width, height = img.size
    return [pixels[i * width:(i + 1) * width] for i in range(height)]

def list_to_image(pixel_list, output_path):
    """
    Converts a 2D list of pixel values back to a grayscale image file.
    
    Parameters:
        pixel_list (list): 2D list of pixel values.
        output_path (str): Path to save the output image.
    """
    height = len(pixel_list)
    width = len(pixel_list[0])
    flattened_pixels = [pixel for row in pixel_list for pixel in row]
    img = Image.new('L', (width, height))  # Create grayscale image (L mode)
    img.putdata(flattened_pixels)
    img.save(output_path)

def ecb(image_matrix):
    """
    Encrypts a grayscale image matrix using ECB mode.
    
    Parameters:
        image_matrix (list): 2D list of pixel values.
    
    Returns:
        list: Encrypted 2D list of pixel values.
    """
    key = 0xAB
    height, width = len(image_matrix), len(image_matrix[0])
    encrypted_image = [[0 for _ in range(width)] for _ in range(height)]

    for i in range(height):
        for j in range(width):
            encrypted_image[i][j] = image_matrix[i][j] ^ key

    return encrypted_image

def generate_counter(nonce, block_number):
    """
    Generates a simple counter value for CTR mode encryption.
    
    Parameters:
        nonce (int): Initial nonce value.
        block_number (int): Block number.
    
    Returns:
        int: Counter value.
    """
    return (nonce << 64) | block_number

def proper_block_cipher(counter, key):
    # Ensure counter is 16 bytes (128 bits) for AES block size
    counter_bytes = counter.to_bytes(16, byteorder='big')
    
    # Create AES cipher in ECB mode since we're using it as a building block
    cipher = AES.new(key, AES.MODE_ECB)
    
    # Encrypt the counter value
    encrypted_counter = cipher.encrypt(counter_bytes)
    
    # Convert the result back to an integer for XOR operation with pixel
    return int.from_bytes(encrypted_counter[:1], byteorder='big')

def ctr(image_matrix):
    """
    Encrypts a grayscale image matrix using CTR mode.
    
    Parameters:
        image_matrix (list): 2D list of pixel values.
    
    Returns:
        list: Encrypted 2D list of pixel values.
    """
    key = os.urandom(32)
    nonce = random.getrandbits(64)

    height, width = len(image_matrix), len(image_matrix[0])
    encrypted_image = [[0 for _ in range(width)] for _ in range(height)]
    
    for i in range(height):
        for j in range(width):
            block_number = i * width + j
            counter = generate_counter(nonce, block_number)
            keystream = proper_block_cipher(counter, key)
            encrypted_image[i][j] = image_matrix[i][j] ^ keystream
    
    return encrypted_image

# Usage Example:
lst = image_to_list('./img/shavkat.jpeg')
ecb_lst = ecb(lst)
ctr_lst = ctr(lst)
list_to_image(ecb_lst, './img/shavkat_ecb.jpeg')
list_to_image(ctr_lst, './img/shavkat_ctr.jpeg')
