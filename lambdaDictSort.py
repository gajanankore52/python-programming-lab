# Write a Python program to sort a list of dictionaries using Lambda.

# Original list of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# Sorting the List of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]



mobile_models = [
                    {'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
                    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, 
                    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
                ]
                
mobile_models.sort(key = lambda x:x['color'])

print(mobile_models)