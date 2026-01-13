#accept number from user and return reverse number


def reverseNumber(iNo):
    
    iRev = 0
    
    while(iNo != 0):
        
        digit = iNo % 10
        iRev = (iRev*10) + digit
        iNo = iNo // 10
        
    return iRev


def main():
    
    iNo = int(input('Enter number: '))
    
    iResult = reverseNumber(iNo)
    
    print(f'Reverse number is: {iResult}')


if __name__ =="__main__":
    main()