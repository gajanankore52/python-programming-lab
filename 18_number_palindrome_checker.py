#Accept number from user and check whether number is palindrom or not

def is_palindrme_number(iNo):
    # Negative numbers are not palindromes (due to the '-' sign)
    if iNo < 0:return False

    # Option A: Mathematical approach (Memory efficient)
    temp = iNo
    iRev = 0
    
    while(iNo > 0):
        digit = iNo % 10
        iRev = (iRev * 10) + digit
        iNo //= 10
    
    return temp == iRev

def is_palindrome_fast(iNo):
    # Option B: String approach (Concise)
    s = str(iNo)
    return s==s[::-1]

def main():
    try:
        num = int(input('Enter number: '))

        # We'll use the mathematical version here
        if is_palindrme_number(num):
            print(f'{num} is a Palindrome')
        else:
            print(f'{num} is Not a Palindrome')
    
    except ValueError:
        print("Invalid input! Please enter a valid integer.")


if __name__ == '__main__':
    main()