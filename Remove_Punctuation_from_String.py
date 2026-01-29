# Python - Remove Punctuation from String


#Using List Comprehension

s = "Hello, World! Python is amazing."
import string

res = ''.join([ch for ch in s if ch not in string.punctuation])

print(res)
