#Accept two nos from user and check whether 1st no is completly divisible by 2nd no or not

def checkDivisible(iVal1, iVal2):
    
    if iVal1 < iVal2:
        return False
    
    if iVal1 % iVal2 ==0:
        return True
    else:
        return False

def main():
    
    iNo1 = int(input("Enter first no: "))
    iNo2 = int(input("Enter second no: "))
    
    bResult = checkDivisible(iNo1,iNo2)
    
    if bResult == True:
        print("Number is divisible")
    else:
        print("Number is not divisible")
        
        
if __name__ == "__main__":
    main()