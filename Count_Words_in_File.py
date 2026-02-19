# Python File I/O: Takes a text file as input and returns the number of words of a given text file

# Write a Python program that takes a text file as input and returns the number of words of a given text file.

import re

def count_words_in_file(file_path):
    
    try:
        with open(file_path,'r',encoding='utf') as file:
            
            content = file.read()
            
            # regex \w+ matches one or more alphanumeric characters
            # This treats "word1,word2" as two separate words
            
            words = re.findall(r'\w+',content)
            
            return len(words)
            
    except FileNotFoundError:
        return "Error: The file was not found."
    
    except Exception as e:
        return f"An unexpected error occured: {e}"


# Usage
filename = 'second.txt'
word_count = count_words_in_file(filename)

print(f'Total number of words: {word_count}')