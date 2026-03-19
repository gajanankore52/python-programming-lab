# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# Accept the input string from the console

values = input("Enter comma-separated numbers: ")

# Split the string by the comma character into a list
list_result = values.split(",")

# Convert the list into a tuple
tuple_result = tuple(list_result)

print(list_result)
print(tuple_result)