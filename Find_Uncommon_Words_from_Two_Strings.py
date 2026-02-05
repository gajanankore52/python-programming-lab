# Find Uncommon Words from Two Strings - Python

# Using collections.Counter

from collections import Counter

# s1 = "Geeks for Geeks"
# s2 = "Learning from Geeks for Geeks"

# s1 = Counter(s1.split()+s2.split())

# res = [word for word in s1 if s1[word]==1]

# print(res)
# ============================================

# Using set

# s1 = "Geeks for Geeks"
# s2 = "Learning from Geeks for Geeks"

# s1 = set(s1.split())
# s2 = set(s2.split())


# print(s2.difference(s1))
# =================================

#Using get()

s1 = "Geeks for Geeks"
s2 = "Learning from Geeks for Geeks"

d1 = {}

words = (s1 +" " + s2).split()

for word in words:
    d1[word] = d1.get(word,0)+1

res = [word for word in d1 if d1[word]==1]

print(res)
============================

