#Accept number from user and return summetion of all number which are even

def sumEvenDigit(iNo):
    
    iSum = 0
    
    while(iNo != 0):
        
        digit = iNo % 10
        if digit % 2 == 0:
            iSum += digit
        
        iNo = iNo // 10
    
    return iSum


def main():
    
    iNo = int(input('Enter number: '))
       
    iResult = sumEvenDigit(iNo)
    
    print(f'Summetion of even digits is: {iResult}')


if __name__ == '__main__':
    main()