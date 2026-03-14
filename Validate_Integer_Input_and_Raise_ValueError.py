# Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

# Scripting Languagesexception ValueError:

# Raised when an operation or function receives an argument that has the right type but an inappropriate value, and the situation is not described by a more precise exception such as IndexError.

def get_valid_integer():
    
    while True:
        try:
            # Prompt the user for input
            user_input = input("Please enter an integer: ")
            
            # Attempt to convert input to an integer
            # This raises a ValueError if the input is like 'abc' or '10.5'
            value = int(user_input)
            
            print(f"Success! You entered the integer: {value}")
            return value
        
        except ValueError:
            # Handle the specific case where conversion fails
            print("Invalid input! That was not a valid integer. Please try again.")

# Run the function

get_valid_integer()