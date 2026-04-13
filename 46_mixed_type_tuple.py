
# Creating a tuple with string and integers

# A descriptive way to define a mixed tuple
data_record = ("apple", "banana", "cherry", 1, 2, 3)

# Demonstrating Unpacking (if you know the structure)
# This assigns the first three to strings and the last three to integers
s1, s2, s3, i1, i2, i3 = data_record

print(f"Tuple Content: {data_record}")
print(f"Type: {type(data_record)}")
print(f"Extracted Integer: {i1}")