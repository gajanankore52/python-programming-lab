#Accept number from user and return summetion of digits of that number


def sumDigit(iNo):
    
    iSum = 0
    
    while(iNo != 0):
        
        digit = iNo % 10
        iSum = iSum + digit
        iNo = iNo // 10
        
    return iSum


def main():
    
    iNo = int(input('Enter number: '))
    
    iResult = sumDigit(iNo)
    
    print(f'Summetion of digit is: {iResult}')


if __name__ == '__main__':
    main()