# Count occurrences of an element in a list in Python

from collections import Counter

data = [1, 3, 2, 6, 3, 2, 8, 2, 9, 2, 7, 3]

# Method 1: The most direct way (Built-in)
def get_single_count(lst, target):
    return lst.count(target)

# Method 2: The efficient way for multiple lookups
# This creates a frequency map once (O(n))
counts_map = Counter(data)

print(f"Count of 3: {get_single_count(data, 3)}")
print(f"Count of 2: {counts_map[2]}")


