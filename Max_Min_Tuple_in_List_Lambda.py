# Python: Find the maximum and minimum values in a given list of tuples using lambda function

# Write a Python program to find the maximum and minimum values in a given list of tuples using the lambda function.


# List of tuples: (item, price)
products = [("Keyboard", 25), ("Monitor", 150), ("Mouse", 15), ("Laptop", 1200)]

# Find the tuple with the maximum value at index 1 (price)
max_product = max(products, key=lambda x:x[1])

# Find the tuple with the minimum value at index 1 (price)
min_product = min(products, key=lambda x: x[1])

print(f"Most expensive: {max_product[0]} at ₹ {max_product[1]}")
print(f"Cheapest: {min_product[0]} at ₹ {min_product[1]}")