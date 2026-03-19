# === First Approch ===
# Given Three given lists
list1,list2,list3 = [1, 2, 3],[4, 5, 6],[7, 8, 9]

# Using map with a lambda function to sum elements
# The lambda takes one element from each list: x, y, and z
result = list(map(lambda x, y, z: x + y + z, list1, list2, list3))

# Displaying the result
print(f"Result: {result}")

# === Second Approch ===
# Using zip and list comprehension to sum elements element-wise

result = [x+y+z for x, y, z in zip(list1, list2, list3)]

# Output the result
print(f"Result: {result}")