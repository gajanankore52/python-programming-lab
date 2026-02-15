# Python File I/O: Find the longest words
# Write a python program to find the longest words.
import re

def find_longest_words(file_path):
    
    try:
        
        with open(file_path, 'r', encoding="utf-8") as file:
            # Read the entire content
            
            content = file.read()
            
            # Use regex to find all words (ignoring punctuation)
            # This splits by any non-alphanumeric character
            
            words = re.findall(r'\w+',content)
            
            if not words:
                return "The file is empty or contains no words."
            
            #Find the length of the longest words
            
            max_length = max(len(word) for word in words)
            
            # Extract all words that match that max length
            
            longest_words = [word for word in words if len(word) == max_length]
            
            # Remove duplicates using set() then convert to list
            
            unique_longest_words = list(set(longest_words))
            
            return unique_longest_words,max_length
              
    except FileNotFoundError:
        return "Error: File not found.", 0

#Usage
if __name__ =="__main__":
    
    filename = 'notes.txt'
    results,length = find_longest_words(filename)
    
    print(f'The longest words have {length} characters:')
    print(results)
