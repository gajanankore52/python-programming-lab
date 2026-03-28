#Accept range from user and display all prime nos in that range

import math

def display_primes_in_range(start, end):
    
    print(f'Prime numbers between {start} and {end} are: ')
    
    for num in range(start, end+1):
        # 1. Primes must be greater than 1
        if num < 2:
            continue
        
        # 2. Check for factors using the square root optimization
        # The 'for...else' handles the logic cleanly
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                break
        
        else:
            # This block only runs if no factor was found
            print(num, end=" ")
    print() # New line at the end            
            
        
def main():
    try:
        i_start = int(input("Enter start of range: "))
        i_end = int(input("Enter end of range: "))

        # Ensure start is less than end
        if i_start > i_end:
            i_start, i_end = i_end, i_start

        display_primes_in_range(i_start, i_end)
    
    except ValueError:
        print("Invalid input! Please enter integers.")

if __name__=="__main__":
    main()