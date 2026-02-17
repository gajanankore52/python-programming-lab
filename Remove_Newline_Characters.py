# Python File I/O: Remove newline characters from a file

# Write a Python program to remove newline characters from a file.

def remove_newlines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            
            # list comprenhension to strip each line
            # .strip() remove whitespace and \n from both ends
            lines = [line.strip() for line in file]
            
            # Join the list back into one string with a space (or nothing)
            
            clean_text = ' '.join(lines)
            return clean_text
           
    except FileNotFoundError:
        return "File not found."


# Usage
print(remove_newlines('second.txt'))