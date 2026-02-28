# Finding 'n' Character Words in a Text File - Python

# Text Hello, how are you? This is a simple text.
# Input: n=3
# Output: ['how', 'are', 'you']

import re

def find_words_of_length(file_path,n):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
            # \b represent a word boundary
            # \w{n} matches exactly 'n' alphanumeric characters
            # The f-string allows us to insert the variable 'n' into the regex
        
            pattern =rf'\b\w{{{n}}}\b'
            
            words = re.findall(pattern,content)
        
        return words
        
    except FileNotFoundError:
        return "Error: File not found."
        
# Usage
n_value = 3
filename = 'fruits.txt'
result = find_words_of_length(filename, n_value)

print(f'Words with length {n_value}:')
print(result)
