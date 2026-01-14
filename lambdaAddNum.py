# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a 
# lambda function that multiplies argument x with argument y and prints the result.

# Sample Output:
# 25
# 48


num1 = lambda a:a+15


print(num1(10))


num2 = lambda x,y : x* y

print(num2(12,4))