#accept N number from user and print such no from array whoes magnitude is equal to multipliation of its immidiate neighbour

def patternMultiply(arr):
    
    for iCnt in range(1,len(arr)-1):
        
        if arr[iCnt-1] * arr[iCnt+1] == arr[iCnt]:
            print(f"{arr[iCnt-1]}* {arr[iCnt+1]} == {arr[iCnt]}")
            


def main():
    
    arr = []
    
    iNo = int(input("Enter no of elements: "))
    
    for i in range(iNo):
        value = int(input("Enter no: "))
        arr.append(value)
    
    patternMultiply(arr)
    


if __name__=="__main__":
    main()