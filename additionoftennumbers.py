#Accept 10 numbers from user and retunr addition of all numbers

def addition(arr):
    
    iSum = 0
    
    for iCnt in range(len(arr)):
        
        iSum = iSum + arr[iCnt]
        
    return iSum

def main():
    
    iNo = int(input("How many numbers you want to enter: "))
    
    list1 = []
    print(f"Enter {iNo} numbers : ")
    
    for i in range(iNo):
        iValue = int(input())
        
        
        list1.append(iValue)
    
    iResult = addition(list1)
    
    print("Addition of all numbers are: ",iResult)


if __name__ == "__main__":
    main()
