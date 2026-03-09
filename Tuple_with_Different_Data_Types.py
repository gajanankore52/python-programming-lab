# Write a Python program to create a tuple with different data types.

# Creating a tuple with different data types

mixed_tuple = ("Python", 2026, 3.14, True, [1, 2, 3])

# Printing the tuple and the type of its elements

print("The Tuple:",mixed_tuple)
print("-" * 30)

# Iterating to show the data type of each item

for item in mixed_tuple:
    
    print(f"Value: {str(item):<10} | Type: {type(item).__name__}")