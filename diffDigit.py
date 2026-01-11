#Accept number from user and return difference between max and min number

def diffDigit(iNo):
    
    iMax = 0
    iMin = 9
    
    while(iNo != 0):
        
        digit = iNo % 10
        
        if digit > iMax :
            iMax = digit
        
        if digit < iMin:
            iMin = digit
        
        iNo = iNo // 10
        
    return iMax - iMin


def main():
    
    iNo = int(input('Enter number: '))
    
    iResult = diffDigit(iNo)
    
    print(f'Difference bet max and min number is : {iResult}')


if __name__ == '__main__':
    main()