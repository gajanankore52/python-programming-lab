# Count Number of Vowels using Sets in Given String - Python


s = "Python Programming"

# v = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

# res = sum([1 for ch in s if ch in v])

# print(res)
# =============================================================


s = "Set operations in Python"
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

res = sum(s.count(v) for v in set(s) & vowels)

print(res)

