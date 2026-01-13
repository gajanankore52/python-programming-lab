# Python program to check if a string has at least one letter and one number


s = "geeksforgeeks"

l = any(ch.isalpha() for ch in s)

n = any(ch.isdigit() for ch in s)

print('True') if l and n else print('False')
    
 
