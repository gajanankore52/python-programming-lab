#Accept N number from user and if substraction of two numbers(consecutive) is equal to third number then we have to add first no into third 
#number otherwise we have to add second number into third number



def patternDifference(arr):
    
    for iCnt in range(len(arr)-2):
        
        if arr[iCnt] - arr[iCnt+1] == arr[iCnt+2]:
            arr[iCnt+2] += arr[iCnt]
        else:
            arr[iCnt+2] +=arr[iCnt+1]
        
        
    print("After Modfication: ",arr)



def main():
    
    arr = []
    
    iNo = int(input("Enter no of element: "))
    
    for i in range(iNo):
        iValue = int(input("Enter no: "))
        
        arr.append(iValue)
        
    patternDifference(arr)
        

if __name__=="__main__":
    main()