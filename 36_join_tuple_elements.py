# Write a Python program to convert a tuple to a string.

# A tuple with mixed types
words = ("Python", "version", 3.12)

# Using a generator expression to convert all elements to strings before joining
result_string = " ".join(str(item) for item in words)

print(f"Result: {result_string}")