#Accept N Nos from user and return addition of all even numbers.

def additionallEven(arr):
    
    iSum = 0
    
    for iCnt in range(len(arr)):
        
        if arr[iCnt]%2==0:
            iSum = iSum+arr[iCnt]
            
    return iSum

def main():
    
    arr = []
    
    iNo = int(input("Enter no of elements: "))
    
    for i in range(iNo):
        value = int(input("Enter no: "))
        arr.append(value)
    
    result = additionallEven(arr)
    print("Addition of all even numbers is: ",result)

if __name__=="__main__":
    main()