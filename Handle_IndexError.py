# Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.
# Raised when a sequence subscript is out of range. (Slice indices are silently truncated to fall in the allowed range; if an index is not an integer, TypeError is raised.)

def get_item_at_index(data_list,index):
    try:
        # Attempt to access the element
        item = data_list[index]
        print(f"Success! Item at index {index} is: {item}")
        return item
    
    except IndexError:
        # This block runs if the index is beyond the list's boundaries
        print(f"Error: Index {index} is out of range.")
        print(f"The list only has {len(data_list)} items (valid indices: 0 to {len(data_list)-1}).")
        return None

# Example usage

my_fruits = ["Apple", "Banana", "Cherry"]

# Test 1: Valid Index
get_item_at_index(my_fruits, 1)

print("-"*35)

# Test 2: Our of Rnge Index
get_item_at_index(my_fruits, 10)