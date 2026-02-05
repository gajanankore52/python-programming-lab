# Python - Keys associated with Values in Dictionary


# Input: {'abc': [10, 30], 'bcd': [30, 40, 10]}
# Output: {10: ['abc', 'bcd'], 30: ['abc', 'bcd'], 40: ['bcd']}

d = {'gfg': [1, 2, 3], 'is': [1, 4], 'best': [4, 2]}
# output {1: ['gfg', 'is'], 2: ['gfg', 'best'], 3: ['gfg'], 4: ['is', 'best']}


dict1 = {}
for key,value in d.items():
    keys = key
    values = value
    
    for value in values:
        if value not in dict1:
            dict1[value] = [keys]
        else:
            dict1[value].append(keys)

print(dict1)
    