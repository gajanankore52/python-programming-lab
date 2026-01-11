#Accept two numbers from user and print smallest common factor


def smallestCommonFactor(iNum1,iNum2):
    
    factor =0
    iCnt = 2
    while(iCnt <= iNum1//2) and (iCnt <= iNum2//2):
        
        if iNum1 % iCnt ==0 and iNum2 % iCnt ==0:
            
            factor =iCnt
            break
        iCnt += 1
    return factor



def main():
    
    
    iNo1 = int(input("Enter First Number: "))
    iNo2 = int(input("Enter Second  Number: "))
    
    iResult = smallestCommonFactor(iNo1,iNo2)
    
    print("Smallest Common factor Is : ",iResult)

if __name__=="__main__":
    main()