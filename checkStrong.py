#Accept number from user and check whether number is strong or not


def iFact(iValue):
    
    fact = 1
    while(iValue != 0):
        
        fact = fact * iValue
        iValue = iValue-1
    return fact
    
    
def checkStrong(iNo):
    
    iCnt = 0
    iSum = 0
    itemp = iNo
    while(iNo != 0):
        digit = iNo % 10
        iSum = iSum + iFact(digit)
        iNo = iNo // 10
    
    return True if iSum == itemp else False
       
        
def main():
    
    iNo = int(input('Enter number: '))
    
    iResult = checkStrong(iNo)
    
    
    print('Number is strong') if iResult else print('Number is not strong')
   
if __name__ == '__main__':
    main()








