# Specific Characters Frequency in String List



# Using dictionary
a = ["geeksforgeeks is best for geeks"]

# char list
b = ['e', 'b', 'g']


dict1 = {}

for x in a:
    
    for y in x:
        if y in b:
            dict1[y] = dict1.get(y,0)+1
        
print(dict1)
# # ========================================


# Using collections.Counter


# from collections import Counter

# a = ["geeksforgeeks is best for geeks"]

# # char list
# b = ['e', 'b', 'g']

# res = {key: val for key, val in Counter("".join(a)).items() if key in b}
# print(res)

# ====================================================

# Using filter()



from collections import Counter


a = ["geeksforgeeks is best for geeks"]


b = ['e', 'b', 'g']

filtered_str = "".join(filter(lambda x: x in b, "".join(a)))

print(filtered_str)
# res = dict(Counter(filtered_str))
# print(res)
# =================================

