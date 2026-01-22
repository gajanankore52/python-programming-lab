# Python program to find the sum of all items in a dictionary



d = {'a': 100, 'b': 200, 'c': 300}

# d =d.values()

# print(sum(d))

#============================

# using lambda

# res = sum((map(lambda x:d[x],d)))

# print(res)

#===============================


res =sum([d[key] for key in d])

print(res)