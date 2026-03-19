#Accept two numbers from user and print addition of common factor

def add_common_factors(num1,num2):
    
    iCnt = 1,iSum = 0
    while(iCnt <= num1//2) and (iCnt <= num2//2):
        
        if num1 % iCnt == 0 and num2 % iCnt == 0:                     
            iSum +=iCnt
        iCnt += 1
    
    return iSum

def main():
    try:
        no1 = int(input("Enter First Number: "))
        no2 = int(input("Enter Second  Number: "))
        
        result = add_common_factors(no1, no2)
        print(f"Addition of common factors is: {result}")
    
    except ValueError:
        print("Invalid input. Please enter integers only.")
  
if __name__=="__main__":
    main()