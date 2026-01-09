#Accept number from user and check whether number is palindrom or not

def palindromNumber(iNo):
    
    temp = iNo
    
    iRev = 0
    
    while(iNo != 0):
        
        digit = iNo % 10
        iRev = iRev * 10 + digit
        iNo = iNo // 10
    
    if iRev == temp:
        return True
    else:
        return False        


def main():
    
    iNo = int(input('Enter number: '))
    
    iResult = palindromNumber(iNo)
    
    if iResult:
        print('Number is Palindrom')
    else:
        print('Number is Not Palindrom')


if __name__ == '__main__':
    main()