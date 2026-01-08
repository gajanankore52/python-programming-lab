#Accept two numbers from user and print largest common factor


def commonFactor(iVal1, iVal2):
    
    factor=0
    iCnt = 1
    while ((iCnt <= iVal1//2) and (iCnt <= iVal2//2)):
        
        if iVal1 % iCnt==0 and iVal2 % iCnt==0:
            factor=iCnt
        iCnt+=1
    
    return factor

def main():
    
    iNo1 = int(input("Enter First number: "))
    iNo2 = int(input("Enter second number: "))
    
    iResult = commonFactor(iNo1,iNo2)
    
    print('Largest common factor is: ',iResult)


if __name__=="__main__":
    main()