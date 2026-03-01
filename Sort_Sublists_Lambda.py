# Python: Sort each sublist of strings in a given list of lists using lambda


# Write a Python program to sort each sublist of strings in a given list of lists using lambda.


def sort_internal_sublists(data):
    # We use a list comprehension to go through each sublist
    # and return a new, sorted version of that sublist.
    # The 'key=lambda x: x' is optional here as strings sort 
    # alphabetically by default, but it demonstrates the lambda usage.
    
    return [sorted(sublist, key=lambda x: x) for sublist in data]


# Input: A list containing multiple unsorted sublists of strings
color_groups = [
    ["cherry", "apple", "banana"],
    ["indigo", "blue", "green", "azure"],
    ["white", "black"]
    ]

# Execution
result = sort_internal_sublists(color_groups)

print("Original:")
for group in color_groups: print(group)

print("\nInternal Sublists Sorted Alphabetically:")
for group in result: print(group)