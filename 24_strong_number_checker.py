#Accept number from user and check whether number is strong or not

import math
   
    
def is_strong_number(n):
    # Convert number to string to iterate through digits
    # Calculate sum of factorials using a generator expression

    digit_sum = sum(math.factorial(int(digit)) for digit in str(n))
    
    return digit_sum == n

        
def main():
    try:
        num = int(input('Enter a number to check: '))
        
        # Handle negative numbers (Strong numbers are usually positive integers)
        if num < 0:
            print('Strong numbers are typically defined for positive integers.')
        
        elif is_strong_number(num):
            print(f"{num} is a Strong Number.")
        
        else:
            print(f"{num} is NOT a Strong Number.")
    
    except ValueError:
        print('Invalid input! Please enter a valid integer.')


if __name__ == '__main__':
    main()








