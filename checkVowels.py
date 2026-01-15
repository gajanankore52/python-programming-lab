# Python Program to Accept the Strings Which Contains all Vowels

# s = "Geeksforgeeks"
# v = 'aeiou'


# print('True') if all(ch in s for ch in v) else print('False') 

# ==============================
# Using set()



s= "geeksforgeeks"

v= set('aeiou')

print('True') if v.issubset(set(s.lower())) else print('False')
    