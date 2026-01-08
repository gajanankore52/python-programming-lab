#Accept two numbers from user and print largest common factor


def largestCommonFactor(iNum1,iNum2):
    
    factor = 0
    iCnt = 1
    while(iCnt <= iNum1//2) and (iCnt <= iNum2//2):
        
        if iNum1 % iCnt ==0 and iNum2 % iCnt ==0:
            
            factor =iCnt
        iCnt += 1
    return factor



def main():
    
    
    iNo1 = int(input("Enter First Number: "))
    iNo2 = int(input("Enter Second  Number: "))
    
    iResult = largestCommonFactor(iNo1,iNo2)
    
    print("Largest common factor is : ",iResult)

if __name__=="__main__":
    main()