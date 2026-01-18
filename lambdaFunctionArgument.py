# Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.

# Sample Output:
# Double the number of 15 = 30
# Triple the number of 15 = 45
# Quadruple the number of 15 = 60
# Quintuple the number 15 = 75


def numberMultiply(n):
    return lambda x:x*n



result = numberMultiply(2)
print(f'Double the number of 15 = {result(15)}')


result = numberMultiply(3)
print(f"Triple the number of 15 = {result(15)}")


result = numberMultiply(4)
print(f"Quadruple the number of 15 = {result(15)}")

result = numberMultiply(5)
print(f"Quintuple the number 15 = {result(15)}")