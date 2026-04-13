
# Write a Python program to split a given dictionary of lists into list of dictionaries using the map function.


def split_dict_of_lists(data):
    if not data:
        return []
        
    keys = data.keys()
    
    # zip(*data.values()) pairs index 0 of all lists, then index 1, etc.
    # map applies the lambda to every zipped tuple
    return list(map(lambda values: dict(zip(keys, values)), zip(*data.values())))


# Input
marks = {
    'Science': [88, 90, 95], 
    'Math': [92, 87, 89], 
    'English': [72, 78, 80]
}

# Execution
print(split_dict_of_lists(marks))
