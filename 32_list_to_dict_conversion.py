# Python - Convert List to List of dictionaries

# using for loop

a = ["name", "age", "city"]  
b = [["Alice", 25, "New York"], ["Bob", 30, "Los Angeles"], ["Charlie", 22, "Chicago"]] 

res = []
for values in b:
    
    res.append({ a[i]:values[i] for i in range(len(a))  })
    
print(res)


# ==================================

# Using Zip function


keys = ["name", "age", "city"]
data = [["Alice", 25, "New York"], ["Bob", 30, "Los Angeles"]]

# dict(zip(keys, values)) is the standard way to pair headers to data
res = [dict(zip(keys, values)) for values in data]

print(res)
    
    
    
    
# print(res)

