#Accept N no from user and return the maximum no from that N numbers

def maximumNumber(brr):
    
    max = 0
    
    for iCnt in range(len(brr)):
        if brr[iCnt] > max:
            max=brr[iCnt]
    
    return max

def main():
    
    arr = []
    
    iNo = int(input("Enter no of elements: "))
    
    for i in range(iNo):
        value = int(input("Enter no: "))
        arr.append(value)
    
    result = maximumNumber(arr)
    print("Maximum no is: ",result)

if __name__ =="__main__":
    main()