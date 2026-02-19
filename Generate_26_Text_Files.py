# Python File I/O: Generate 26 text files named A.txt, B.txt, and so on up to Z.txt

# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.

import string
import os

def generate_alphabet_files(directory = "alpabet_files"):
    
    # Create a directory so we don't clutter the main folder
    
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    
    # string.ascii_uppercase provides 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for letter in string.ascii_uppercase:
        filename = os.path.join(directory, f'{letter}.txt')
        
        
        with open(filename, 'w', encoding='utf-8') as f:
            # Writing the letter inside the file just so they aren't empty
            f.write(f'This is the file for the letter {letter}.')

    print(f"Successfully generated 26 files in the '{directory}' folder.")


# Usage
generate_alphabet_files()