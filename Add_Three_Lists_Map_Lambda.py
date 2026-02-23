# Add Three Lists Map Lambda



# Three given lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]


# Using map and lambda to add them element-wise
# The lambda takes one element from each list: x, y, and z
result = list(map(lambda x, y, z: x + y + z, list1, list2, list3))

# Displaying the result
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"List 3: {list3}")
print(f"Result: {result}")