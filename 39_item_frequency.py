# Write a Python program to count the occurrences of items in a given list using lambda.


# A sample list with repeated items
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']


# Applying lambda to each unique item via map
unique_items = set(data)
count_func = lambda item: (item, data.count(item))
occurrences = dict(map(count_func, unique_items))

print('Item Frequencies')
print(occurrences)



