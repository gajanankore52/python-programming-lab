#Accept two nos from user and check whether 1st no is completly divisible by 2nd no or not

def check_divisible(dividend, divisor):
    
    if divisor == 0:
        return False
    
    # Directly return the result of the comparison
    return dividend % divisor == 0    
    

def main():
    try:
        # Using more descriptive variable name
        num1 = int(input("Enter the dividend (first number): "))
        num2 = int(input("Enter the divisor (second number): "))
    
        # In python, 'ifbResult:' is preferred over 'if bResult == True:'
    
        if check_divisible(num1, num2):
            print(f"{num1} is completely divisible by {num2}")
        else:
            print(f"{num1} is NOT completely divisible by {num2}")
    except ValueError:
        print('Invalid input! Please enter whole numbers only.')
        

if __name__ == "__main__":
    main()