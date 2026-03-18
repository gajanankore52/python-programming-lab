# Write a Python program to create an iterator from several iterables in a sequence and display the type and elements of the new iterator.

import itertools

# Define several iterables
list_data = [10, 20, 30]
tuple_data = ('A' 'B', 'C')
range_data = range(5,8)

# Create an iterator from the sequences
combined_iterator = itertools.chain(list_data, tuple_data, range_data)

# Display the type of the new ierator
print(f"Type of the new iterator: {type(combined_iterator)}")

# Display the elements
print("Elements in the iterator:")
for item in combined_iterator:
    print(item, end=" ")