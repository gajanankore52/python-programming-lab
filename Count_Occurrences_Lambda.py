# Write a Python program to count the occurrences of items in a given list using lambda.


# A sample list with repeated items
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']


# We define a lambda that counts occurrences of 'item' in data
count_func = lambda item:data.count(item)

# Use a dictionary comprehension to apply the lambda to each unique item
# set(data) ensures we don't count the same wordmultiple times
occurrences = {item: count_func(item) for item in set(data)}

print('Item Frequencies')
print(occurrences)



