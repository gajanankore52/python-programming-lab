# Python program to check if given string is pangram

# import string

# s = "The quick brown fox jumps over the lazy dog"



# res=all(letter in s.lower() for letter in string.ascii_lowercase)

# print(res)
# ==================================================


def is_pangram_count(s):
   
    unique_letters = ""
    
   
    for char in s:
   
        char_lower = char.lower()
        
   
        if char_lower >= 'a' and char_lower <= 'z' and char_lower not in unique_letters:
   
            unique_letters += char_lower
            
   
    return len(unique_letters) == 26


string1 = "The quick brown fox jumps over the lazy dog"
string2 = "Hello, world!"

print(f"'{string1}' is a pangram: {is_pangram_count(string1)}")
print(f"'{string2}' is a pangram: {is_pangram_count(string2)}")