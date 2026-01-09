#Accept N number from user and accept one number from user and check whether that no is present in array or not
#If that number is not present in a array then we have to return nearest number


def nearestNumber(arr,iNum):
    
    minDiff = arr[0] - iNum
    
    nearestNumber = 0
    if minDiff< 0 :
        
        minDiff=-minDiff
    
    
    for iCnt in range(len(arr)):
        
        diff = arr[iCnt]-iNum
        
        if diff<0:
            diff = -diff
        
        if diff == 0:
            
            nearestNumber = arr[iCnt]
            break
        
        else:
            if diff <= minDiff:
                minDiff = diff
                nearestNumber = arr[iCnt]
    
    return nearestNumber



def main():
    
    arr = []
    
    iNo = int(input("Enter no of element: "))
    
    iNumber = int(input("Enter one number: "))
    
    for i in range(iNo):
        
        value = int(input("Enter no: "))
        
        arr.append(value)
        
    
    iResult = nearestNumber(arr,iNumber)
        
    print("Nearest number is : ",iResult)


if __name__ =="__main__":
    main()