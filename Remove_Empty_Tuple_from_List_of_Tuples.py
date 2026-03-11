# Write a Python program to remove an empty tuple(s) from a list of tuples.

# List containing some empty tuple

l = [(1, 2), (), (3, 4), (), ((),), (8, 9), ()]

# Filter out empty tuple
# 'if t' checks if the tuple is non-empty

result = [t for t in l if t]

print(result)