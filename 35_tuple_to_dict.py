# Write a Python program to convert a tuple to a dictionary.

# Scenario A: Your current logic (Best for nested pairs)
tuple_of_pairs = (("name", "Alice"), ("age", 30), ("city", "New York"))
result_dict = dict(tuple_of_pairs)

# Scenario B: Flat tuple conversion (Every two elements become a pair)
flat_tuple = ('name', 'Alice', 'age', 30, 'city', 'New York')
# zip() pairs elements from two slices: [start:stop:step]
it = iter(flat_tuple)
result_dict_flat = dict(zip(it, it))


print(f"Nested Conversion: {result_dict}")
print(f"Flat Conversion: {result_dict_flat}")

