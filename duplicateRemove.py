#Accept N number from user and replace every duplicate occurence of number with zero


def duplicateRemove(ilist):
    
    for num in range(len(ilist)-1):
        
        if ilist[num] == 0:
            continue
        
        for i in range(num+1,len(ilist)):
            if ilist[num] == ilist[i]:
                
                ilist[i] = 0

    return ilist
    
    
def main():
    
    arr = []
    
    iNo = int(input("Enter number of element: "))
    
    print('Enter numbers: ')
    
    for i in range(iNo):
        value = int(input())
        arr.append(value)
        
    iResult = duplicateRemove(arr)
    
    print(f'After removing duplicate occurence list is: {iResult}')


if __name__ == "__main__":
    main()