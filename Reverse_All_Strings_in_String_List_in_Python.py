# Reverse All Strings in String List in Python

a = ["apple", "banana", "cherry", "date"]


b = []

# for item in a:
    
    # item = item[::-1]
    # b.append(item)
    
# # print(b)

# =================

# Using map() Function

res = list(map(lambda s:s[::-1],a))

print(res)