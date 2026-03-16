# Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.
# The base class for those built-in exceptions that are raised for various arithmetic errors: OverflowError, ZeroDivisionError, FloatingPointError


def perform_division(numerator, denominator):
    try:
        # This could raise ZeroDivisionError or OverflowError
        result = numerator / denominator
        print(f"Calculation successful: {result}")
        
    except ArithmeticError as e:
        # This catches ZeroDivisionError, OverflowError, and FloatingPointError
        print(f"Math Error: An arithmetic issue occured.")
        print(f"Specific Error Details: {e}")
    
        
# Test 1: Division by zero (a type of ArithmeticError)
print("Tesing Division by Zero:")
perform_division(10, 0)


print("-" * 35)

# Test 2: Handling extreme values(potential OverflowError)
print("Testing Potential Overflow:")
try:
    # Raising a number to an extreme power can trigger OverflowError
    result = 10.0 ** 1000
except ArithmeticError as e:
    print(f"Arithmetic Error caught: {e}")