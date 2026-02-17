# Python File I/O: Read a random line from a file

# Write a Python program to read a random line from a file.
import random

def read_random_line(file_path):
    
    try:
        with open(file_path, 'r', encoding ='utf-8') as file:
            
            lines = file.readlines()
            
            if not lines:
                return 'The file is empty'
            
            # random.choice picks one element from the list at random
            return random.choice(lines).strip()
    
    except FileNotFoundError:
        return 'File not found.'
            

# Usage

print(read_random_line('first.txt'))