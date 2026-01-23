# Ways to sort list of dictionaries by values in Python - Using lambda function


list1 = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]
       
       
print(sorted(list1,key=lambda x:x['age']))

