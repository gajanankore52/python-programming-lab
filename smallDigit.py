#Accept number from user and return smallest digit from that number



def smallDigit(iNo):
    
    iMin = 9
    
    while(iNo != 0 and iMin != 0):
        
        digit = iNo % 10
        if digit < iMin:
            iMin = digit
        iNo = iNo //10
    return iMin



def main():
    
    iNo = int(input('Enter number: '))
    
    iResult = smallDigit(iNo)
    
    print(f'Smallest digit number is : {iResult}')

if __name__ == "__main__":
    main()
    