#Accept number from user and check whether that number is armstrong number or not

def is_armstrong(n):
    
    # Convert to string to easily access digits and find the power (length)
    s = str(n)
    power = len(s)
    
    # Calculate sum: for each character, convert back to int, raise to power
    total = sum(int(digit) ** power for digit in s)
    return total == n


def main():
    try:
        num = int(input('Enter a number to check: '))
        
        # Using a simple if-else for the final print
        if is_armstrong(num):
            print(f"{num} is an Armstrong number.")
        else:
            print(f"{num} is not an Armstrong number.")
            
    except ValueError:
        print("Invalid input! Please enter a whole number.")

if __name__ == '__main__':
    main()