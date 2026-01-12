#ACCept number from user and divide that number inot two part.
# we have to return addition of that two part


def sumDivide(iNo):
    
    iSum, iNo1,iNo2,iCnt,iCnt1,iCnt2,iRev = 0,0,0,0,0,0,0
    
    iTemp = iNo
    
    while(iNo != 0):
        
        iCnt +=1
        iNo = iNo//10
    
    iCnt1 = iCnt//2
    
    iCnt2 = iCnt - iCnt1
    
    iNo = iTemp
    
    while(iNo != 0):
        
        digit = iNo % 10
        iRev = iRev * 10 + digit
        iNo = iNo // 10
    
    print(f'Reverse number: {iRev}')
    
    iNo = iRev
    
    while(iCnt1 != 0):
        
        digit = iNo %10
        
        iNo1 = iNo1*10 + digit
        
        iNo = iNo //10
        iCnt1 = iCnt1 - 1
    
    print(f'iNo1 is : {iNo1}')
    
    while(iCnt2 != 0):
        
        digit = iNo % 10
        iNo2 = iNo2 * 10 + digit
        iNo = iNo //10
        iCnt2 -= 1
        
    print(f'iNo2 is : {iNo2}')
        
    
    iSum = iNo1 + iNo2
    
    return iSum
        



def main():
    
    iNo = int(input('Enter number : '))
    
    iResult = sumDivide(iNo)
    
    print(f'Summation of two part of number is : {iResult}')


if __name__ == '__main__':
    main()
    