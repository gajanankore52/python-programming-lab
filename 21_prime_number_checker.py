#Accept no from user and check whether that no is prime or not
import math

def is_prime(n):
    # 1. Handle numbers less than 2 (0 and 1 are not prime) 
    if n < 2:
        return False
    
    # 2. Optimaztion: 2 is the only even prime
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # 3. Only check up to the square root
    # We can also skip even numbers in the loop by using a step of 2
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    
    return True


def main():
    try:
        num = int(input("Enter a number to check: "))
    
        if is_prime(num):
            print(f'{num} is a Prime Number. ')
        else:
            print(f'{num} is NOT a Prime Number. ')
    except ValueError:
        print("Invalid input! Please enter an integer.")    


if __name__ =="__main__":
    main()