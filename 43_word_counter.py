
# Write a Python program that takes a text file as input and returns the number of words of a given text file.

import re

def count_words_in_file(file_path):
    word_count = 0
    try:
        # 'utf-8' is the standard encoding for text files
        with open(file_path,'r',encoding='utf') as file:
            for line in file:
                # Find all owrds in the current line and add to total
                words = re.findall(r'\w+',line)
                word_count += len(words)
            
        return word_count
            
    except FileNotFoundError:
        return "Error: The file was not found."
    
    except Exception as e:
        return f"An unexpected error occured: {e}"


# Usage
filename = 'second.txt'
word_count = count_words_in_file(filename)

print(f'Total number of words: {word_count}')