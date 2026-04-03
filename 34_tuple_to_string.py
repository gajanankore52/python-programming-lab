# Write a Python program to convert a tuple to a string.

# A tuple with mixed types
data_tuple = ('V', 'e', 'r', 's', 'i', 'o', 'n', ' ', 3)

# Use map() or a generator expression to ensure all elements are strings
result_string = "".join(map(str, data_tuple))

print(f"Original Tuple: {data_tuple}")
print(f"Converted String: {result_string}")