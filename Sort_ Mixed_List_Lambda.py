# Python: Sort a given mixed list of integers and strings using lambda

# Write a Python program to sort a given mixed list of integers and strings using lambda. Numbers must be sorted before strings.


def sort_mixed_list(mixed_list):
    # The lamda returns a tuple : (type_priority, actual_values)
    # Priority 0 : Integers/Floats
    # Priority 1 : Strings
    
    sorted_list = sorted(mixed_list, key=lambda x: (0,x) if isinstance(x, (int,float)) else (1,x))
    
    return sorted_list

# Input
data = ["banana", 10, "apple", 5, 2, "cherry", 8]

# Execution
result = sort_mixed_list(data)

print(f'Originak: {data}')
print(f'Sorted: {result}')