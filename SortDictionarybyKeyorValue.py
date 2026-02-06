# Sort Python Dictionary by Key or Value 


# d = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15}

# res = sorted(d)

# res = {keys:d[keys]  for keys in res}

# print(res)

# =========================================

# d = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15}

# mykeys = list(d.keys())

# mykeys.sort()

# dict1 = {key: d[key] for key in mykeys}

# print(dict1)

# ==========================================

# Displaying the Keys in Sorted Order using sorted() on Keys

# d = {2: 56, 1: 2, 5: 12, 4: 24}

# print('Dictionary is: ',d)


# for i in sorted(d):
    # print(i, end =' ')
# ==========================================

# Sorting the dictionary by key using OrderedDict

# from collections import OrderedDict

# d = {'ravi': '10', 'rajnish': '9', 'abc': '15'}
# d1 = OrderedDict(sorted(d.items()))
# print(d1)

# ==============================================


# Sorting Alphabetically by Values using Sorted

d = {2: 56, 100: 2, 3: 323}

print('Dictionary: ',d)

# sorted_items = sorted(d.items(), key=lambda k : (k[0],k[1]))
sorted_items = sorted(d.items(), key = lambda x:x[0])
print(sorted_items)

# ===================================================