# Count repeated characters in a string
#Write a python program to count repeated characters in a string.


from collections import Counter

str1 = 'thequickbrownfoxjumpsoverthelazydog'

res = {key:value for key,value in Counter(str1).items() if value > 1}

print(res)