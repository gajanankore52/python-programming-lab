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


# a = ["name", "age", "city"]  
# b = [["Alice", 25, "New York"], ["Bob", 30, "Los Angeles"], ["Charlie", 22, "Chicago"]] 

# res = []
# for values in b:
    # res.append({a[i]:values[i] for i in range(len(a))})
    
    
    
    
# print(res)

