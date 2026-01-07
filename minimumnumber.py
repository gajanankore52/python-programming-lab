#Accept N no from user and return the minimum no from that N numbers

def minimumNumber(brr):
    
    min = brr[0]
    
    for iCnt in range(len(brr)):
        if brr[iCnt] < min:
            min=brr[iCnt]
    
    return min

def main():
    
    arr = []
    
    iNo = int(input("Enter no of elements: "))
    
    for i in range(iNo):
        value = int(input("Enter no: "))
        arr.append(value)
    
    result = minimumNumber(arr)
    print("Minimum no is: ",result)

if __name__ =="__main__":
    main()