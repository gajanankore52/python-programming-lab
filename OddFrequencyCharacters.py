# Odd Frequency Characters 


from collections import Counter

# s = 'geekforgeeks is best for geeks'

# freq = Counter(s)

# res = [ch for ch,count in freq.items() if count %2 !=0]

# print(res)
# ================

s = 'geekforgeeks is best for geeks'

res = [ch for ch in set(s) if s.count(ch) % 2 != 0]

print(res)


# ==========================

s = 'geekforgeeks is best for geeks'

freq={}

for char in s:
    freq[char] = freq.get(char,0)+1
    
# res = list(map(lambda x:x if freq[x]%2 !=0,freq))

res =[x for x in freq if freq[x]%2 != 0]

print(res)