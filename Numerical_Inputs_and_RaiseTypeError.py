# Write a Python program that prompts the user to input two numbers 
# and raises a TypeError exception if the inputs are not numerical
# Raised when an operation or function is applied to an object of inappropriate type. 
# The associated value is a string giving details about the type mismatch.


def multiply_numbers(a, b):
    try:
        # Check if both inputs are either int or float
        if not (isinstance(a,(int, float)) and isinstance(b,(int,float))):
            raise TypeError("Both inputs must be numerical (int or float).")
            
        result = a * b
        print(f"The product is: {result}")
        return result
        
    except TypeError as e:
        print(f"Type Error caught: {e}")
        
        
# Example 1: Passing valid numbers
print("Test 1: Valid Numbers")
multiply_numbers(10, 5.5)

print("-" * 35)

# Example 2 : Passing a string and a number
print("Test 2: Invalid Types")
multiply_numbers("10", 5)
