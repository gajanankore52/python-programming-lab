# Count occurrences of an element in a list in Python



# a = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]




# print(a.count(3))
# =====================

a = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]


count = 0

for num in a:
    
    if num == 1:
        count+=1
print(count)



# # ====================


# from collections import Counter

# a = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]

# res = Counter(a)

# print(res[2])




