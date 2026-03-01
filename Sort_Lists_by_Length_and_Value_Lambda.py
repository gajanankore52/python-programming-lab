# ython: Sort a list of lists by length and value using lambda

# Write a Python program to sort a given list of lists by length and value using lambda.

def sort_nested_list(data):
    # key = lambda x: (len(x),x)
    # Primary: len(x) -> Sorts by number of elements
    # Secondary: x-> Sorts lexicographically by the values inside
    
    return sorted(data,key=lambda x: (len(x),x))



# Input
list_of_lists = [[1, 2, 3], [1, 2], [3, 4], [1, 1, 1], [0]]

# Execution

result = sort_nested_list(list_of_lists)

print(f"Sorted List of Lists: {result}")
