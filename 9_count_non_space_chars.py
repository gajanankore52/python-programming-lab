# Avoid Spaces in string length

# === First Approach ===
s = "geeks for geeks"

# This counts 1 for every character that is NOT a space
res = sum(1 for char in s if char != ' ')

print(res)

# === Second Approch ===

s = "geeks \t for \n geeks"

# .split() without arguments splits by any whitespace and removes it
res = sum(len(word) for word in s.split())
print(res)      

# === Third Approch

import re

s = "geeks for geeks"
res = len(re.findall(r'\S', s))

print(res)

# === Fourth Approach ===

res = len(list(filter(lambda ch : ch!= ' ',s)))
print(res)
