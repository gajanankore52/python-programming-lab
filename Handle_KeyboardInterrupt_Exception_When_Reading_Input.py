# Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.
# Raised when the user hits the interrupt key (normally Control-C or Delete). During execution, a check for interrupts is made regularly. 
# The exception inherits from BaseException so as to not be accidentally caught by code that catches Exception and thus prevent the interpreter from exiting.

import sys

def get_number_input():
    print("--- Press Ctrl+C at any time to cancel the operation ---")
    try:
        user_input = input("Please enter a number: ")
        print(f"You entered: {user_input}")
        
    except KeyboardInterrupt:
        # This block catches the Ctrl+C signal
        print("\n\nExecution interrupted by user (KeyboardInterrupt).")
        print("Cleaning up resources and exiting safely...")
        # Use sys.exit to close the program without a traceback
        sys.exit(0)

if __name__ == "__main__":
    get_number_input()
