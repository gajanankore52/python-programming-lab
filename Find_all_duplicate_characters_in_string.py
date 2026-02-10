# Find all duplicate characters in string in Python

# s = "GeeksforGeeks"

# d = {}

# res = []

# Using Loop with Dictionary

# for ch in s:
    # d[ch] = d.get(ch,0)+1
    

# for c,cnt in d.items():
    
    # if cnt > 1:
        # res.append(c)
        
# print(res)
# ===============================

# Using collections.Counter

from collections import Counter

s = "GeeksforGeeks"

s=Counter(s)

res = [c for c,cnt in s.items() if cnt>1]

print(res)


    