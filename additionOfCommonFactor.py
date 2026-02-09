
#Accept two numbers from user and print addition of common factor


def addCommonFactor(iNum1,iNum2):
    
    factor = 0
    iCnt = 1
    iSum =0
    while(iCnt <= iNum1//2) and (iCnt <= iNum2//2):
        
        if iNum1 % iCnt ==0 and iNum2 % iCnt ==0:
            
            factor =iCnt
            
            iSum +=iCnt
        iCnt += 1
    
    return iSum


def main():
    
    
    iNo1 = int(input("Enter First Number: "))
    iNo2 = int(input("Enter Second  Number: "))
    
    iResult = addCommonFactor(iNo1,iNo2)
    
    print("Addition of common factor is : ",iResult)

if __name__=="__main__":
    main()