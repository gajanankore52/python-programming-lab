# Python - Keys associated with Values in Dictionary

from collections import defaultdict
# input: {'abc': [10, 30], 'bcd': [30, 40, 10]}
# Output: {10: ['abc', 'bcd'], 30: ['abc', 'bcd'], 40: ['bcd']}


d = {'gfg': [1, 2, 3], 'is': [1, 4], 'best': [4, 2]}

e= {1: ['gfg', 'is'], 2: ['gfg', 'best'], 3: ['gfg'], 4: ['is', 'best']}

new = defaultdict(list)
for k,v in d.items():      
    
    for value in v:
        new[value].append(k)
print(dict(new))
