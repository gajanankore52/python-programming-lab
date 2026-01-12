#Accept N numbers from user and dispaly all such consqutive pairs of numbers whoes addition is equal to next number.


def patternSum(arr):
    
    print('Pairs of number: ')
    for iCnt in range(len(arr)-2):
        
        if arr[iCnt] + arr[iCnt+1] == arr[iCnt+2]:
            print(f'{arr[iCnt]} + {arr[iCnt+1]} == {arr[iCnt+2]}')


def main():
    
    arr = []
    
    iNo = int(input("Enter no of elements: "))
    
    for i in range(iNo):
        value = int(input("Enter no: "))
        arr.append(value)
    
    patternSum(arr)
    


if __name__=="__main__":
    main()