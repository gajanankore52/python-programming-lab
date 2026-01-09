#Accept 10 numbers form user and return addition of even numbers


def additionofeven(arr):
    
    iSum = 0
    
    for iCnt in range(len(arr)):
        
        if arr[iCnt]%2 == 0:
            iSum=iSum+arr[iCnt]

    return iSum

def main():
    
    iNo = int(input("How many number you want to enter: "))
    
    brr = []
    
    print("Enter numbers: ")
    for i in range(iNo):
        iValue = int(input())
        brr.append(iValue)
        
    iResult = additionofeven(brr)
    
    print('Addition of even numbers are : ',iResult)
    


if __name__ == "__main__":
    main()