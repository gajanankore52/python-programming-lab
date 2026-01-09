#Accept number from user and check whether that number is armstrong number or not

def power(digit,iCnt):
    
    Ans = 1

    while(iCnt != 0):
        
        Ans = Ans * digit
        iCnt -= 1
    
    return Ans

def countDigit(iValue):
    
    iCnt = 0
    
    while(iValue != 0):
        
        iCnt += 1
        iValue = iValue // 10
    
    return iCnt

def checkArmstrong(iNo):
    
    iSum = 0
    itemp = iNo
    
    iCnt = countDigit(iNo)
    
    while(iNo != 0):
        
        digit = iNo % 10
        iSum = iSum + power(digit,iCnt)
        iNo = iNo // 10
    
    return True if itemp == iSum else False

def main():
    
    iNo = int(input('Enter number: '))
    
    iResult = checkArmstrong(iNo)
    
    print('Number is Armstrong') if iResult else print('Number is not Armstrong')

if __name__ == '__main__':
    main()