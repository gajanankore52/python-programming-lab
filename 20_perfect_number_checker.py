 #Accept no from user and check whether that no is perfect or not

import math

def is_Perfect(n):
    # Perfect numbers must be positive
    if n <= 1:
        return False

    # Start with 1 because it's a divisor for evry number > 1
    divisor_sum = 1
    
    # Only loop up to the square root
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisor_sum += i
            # If the divisors are different (e.g., 2 and 14), add both
            if i * i != n:
                divisor_sum += n // i
    
    return divisor_sum == n


def main():
    try:
    
        num = int(input('Enter a number: '))

        if is_Perfect(num):
            print(f'{num} is a Perfect Number.')
        else:
            print(f'{num} is NOT a Perfect Number.')
    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ =="__main__":
    main()