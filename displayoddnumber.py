#Accept N numbers from user and display odds numbers

def displayOddNumber(brr):
        
        print("Odd numbers are: ")
        for iCnt in range(len(brr)):
            
            if brr[iCnt]%2!=0:
                print(brr[iCnt])
                

def main():
    
    arr = []
    
    iNo = int(input("Enter no of elements: "))
    
    for i in range(iNo):
        value =int(input("Enter no: "))
        arr.append(value)
        
    displayOddNumber(arr)


if __name__=="__main__":
    main()