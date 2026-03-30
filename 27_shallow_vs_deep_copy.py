# Cloning or Copying a List

# Method 1: Shallow Copy using .copy()

a = [1, 2, 3, 4, 5]
b = a.copy()
print(b)


# Method 2: Deep Copy using copy.deepcopy()

import copy

a = [1, 2, 3, 4, 5]
b = copy.deepcopy(a)

print(b)
