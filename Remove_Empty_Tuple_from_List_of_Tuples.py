# Write a Python program to remove an empty tuple(s) from a list of tuples.

# List containing some empty tuple

l = [(1, 2), (), (3, 4), (), ((),), (8, 9), ()]

# Filter out empty tuple
# 'if t' checks if the tuple is non-empty

result = [t for t in l if t]

print(result)
print('*'* 30)

l = [(1, 2), (), (3, 4), (), (8, 9)]

# filter(None, sequence) removes all Falsy values
result = list(filter(None, l))

print(result)

print('*'* 30)


l = [(1, 2), (), ((),)]

# Removes () and any tuple that is empty after being stripped of whitespace/nulls
# Here we check if the length of the tuple is greater than 0
result = [t for t in l if len(t) > 0]

print(result) 
