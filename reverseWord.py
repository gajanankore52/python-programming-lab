#Reverse Words in a Given String in Python

# input = Geeks for Geeks
# output = Geeks for Geeks



s = "Geeks for Kore"


# reversed_str = ' ' . join(s.split(' ')[::-1])

# print(reversed_str)

# ======================================#



reversed_str = ''
words = s.split()
for word in reversed(words):
    reversed_str += word + ' '

print(reversed_str)

