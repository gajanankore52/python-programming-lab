# Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.Scripting Languages

# exception ZeroDivisionError:

# Raised when the second argument of a division or modulo operation is zero. 
# The associated value is a string indicating the type of the operands and the operation.


def safe_divide(numerator, denominator):
    
    try:
        # Attempt the division
        result = numerator / denominator
        print(f"Result: {result}")
    except ZeroDivisionError:
        # This block executes only if a division by zero occurs
        print("Error: You cannot divide by zero. Please check your denominator.")
    except TypeError:
        # Handles cases where inputes are not numbers
        print("Error: Please provide numeric values.")
    else:
        # Excutes if no exceptions were raised
        print("Division successful!")
    finally:
        # Excutes no matter what
        print("Execution complete.")

# Testing the fuction

safe_divide(10, 2)
print('-' * 55)
safe_divide(10, 0)
print('-' * 55)
safe_divide(10, 'A')