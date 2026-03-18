# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320

def compute_factorial(n):
    
    if n < 0:
        return "Factorial does not exist for negative numbers"
    elif n == 0:
        return 1
    else:
        factorial = 1
        for i in range(1,n + 1):
            factorial = factorial * i
        return factorial    
    
# Take input from the user
user_input = input('Enter numbers separated by commas: ')
# Convert the input string into a list of integers
numbers = [int(x) for x in user_input.split(',')]

# Compute factorials for each number
results = [str(compute_factorial(n)) for n in numbers]

# Print results in a comma-separated sequence
print(','.join(results))