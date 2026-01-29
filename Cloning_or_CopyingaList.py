# Cloning or Copying a List


# Using copy()

a = [1, 2, 3, 4, 5]

b = a.copy()
# print(b)

print(id(a))
print(id(b))
# ========


import copy

# a = [[1, 2], [3, 4], [5, 6]]
a = [1, 2, 3, 4, 5]
b = copy.deepcopy(a)

# print(b)

print(id(a))
print(id(b))