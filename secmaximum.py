#Accept N number from user and find out second max no from that numbers

def secmaximum(arr):
    
    fMax = arr[0]
    sMax =arr[1]
    
    for iCnt in range(len(arr)):
        
        if fMax < arr[iCnt] :
            sMax=fMax
            fMax=arr[iCnt]
            
            
        elif sMax < arr[iCnt] and fMax!=arr[iCnt]:
            sMax=arr[iCnt]
    
    return sMax

def main():
    
    arr = []
    
    iNo = int(input("Enter no of elements: "))
    
    for i in range(iNo):
        value = int(input("Enter no: "))
        arr.append(value)
    
    result = secmaximum(arr)
    print("Second maximum no is: ",result)


if __name__=="__main__":
    main()