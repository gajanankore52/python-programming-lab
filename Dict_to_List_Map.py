# Python: Split a given dictionary of lists into list of dictionaries using map function

# Write a Python program to split a given dictionary of lists into list of dictionaries using the map function.


def split_dict_of_lists(data):
    # 1. Get the keys: ['Science', 'Math', 'English']
    keys = data.keys()
    
    # 2. Use zip(*data.values()) to pair the elements by index
    # This turns [[88, 90], [92, 87], [72, 78]] into [(88, 92, 72), (90, 87, 78)]
    values_zipped = zip(*data.values())
    
    # 3. Use map to create a new dictionary for each zipped tuple
    # lambda v: dict(zip(keys, v)) pairs the keys back with the specific row values
    result = list(map(lambda v: dict(zip(keys, v)), values_zipped))
    
    return result

# Input Dictionary
marks = {
    'Science': [88, 90], 
    'Math': [92, 87], 
    'English': [72, 78]
}

# marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# Execution
output = split_dict_of_lists(marks)

print("Original Dictionary:")
print(marks)
print("\nList of Dictionaries:")
print(output)