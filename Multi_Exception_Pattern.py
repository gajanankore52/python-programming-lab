# The Multi-Exception Pattern

import sys

def get_user_age():
    print('Type "Ctrl+C" at any time to exit.')
    while True:
        try:
            # Step 1: Get input
            line = input("\nPlease enter your age: ")
            
            #Step 2: Validate integer format
            age = int(line)
            
            # Step 3: Logic check (Manaul ValueError)
            if age < 0 or age > 120:
                raise ValueError(f'{age} is not a realistic age.')
                
            print(f'Age recorded: {age}')
            break
        
        except ValueError as e:
            # Handles both 'abc' AND negative/huge numbers
            print(f"Input Error: {e}. Please try again.")
        
        except KeyboardInterrupt:
            # Handles Ctrl+C gracefully
            print("\n\nProgram cancelled by user. Exiting safely...")
            sys.exit(0)

get_user_age()