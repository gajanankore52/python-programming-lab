# Python File I/O: Count the frequency of words in a file

# Write a  Python program to count the frequency of words in a file.

import re
from collections import Counter

def count_word_frequency(file_path):
    
    try:
        
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read the entire file and convert to lowercase
            # Lowercase ensures "The" and "the" are counted as the same word
            
            text = file.read().lower()
            
            # Use Regex to find words only ((ignoring punctuation like commas/periods)
            words = re.findall(r'\b\w+\b',text)
            
            # Counter creates a dictionary: {word: count}
            word_counts = Counter(words)
            
            return word_counts
    
    except FileNotFoundError:
        print('Error: The file was not found.')
        return None
           
# Usage

if __name__ =="__main__":
    
    filename = "notes.txt"
    frequencies = count_word_frequency(filename)
    
    if frequencies:
    # Display the 10 most common words
        print("Top 10 most frequent words:")
        for word, count in frequencies.most_common(10):
            print(f"{word}: {count}")