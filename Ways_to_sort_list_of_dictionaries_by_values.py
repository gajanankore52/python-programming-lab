 # Ways to sort list of dictionaries by values in Python – Using itemgetter

from operator import itemgetter


# data_list = [{"name": "Nandini", "age": 20},
             # {"name": "Manjeet", "age": 20},
             # {"name": "Nikhil", "age": 19}]
             
# print(sorted(data_list, key=itemgetter('age')))

# print(sorted(data_list, key=itemgetter('age','name')))

data = [('apple', 3), ('banana', 2), ('pear', 5)]
# sorted_data = sorted(data, key=itemgetter(1)) # Sorts by the second element (index 1)
sorted_data = sorted(data, key = lambda x:x[1])
print(sorted_data)
    # Output: [('banana', 2), ('apple', 3), ('pear', 5)]