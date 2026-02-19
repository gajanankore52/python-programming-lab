# Python: Remove None value from a given list using lambda function

# Write a Python program to remove None values from a given list using the lambda function.



# A sample list containing strings, numbers, and None values

data = ["Apple", None, "Banana", 42, None, "Cherry", False]

# filter() takes a function and an iterable
# lambda x:x is not None returns True only if the value isn't None

clean_list = list(filter(lambda x:x is not None,data))

print("Original List:",data)
print("Cleaned List:",clean_list)