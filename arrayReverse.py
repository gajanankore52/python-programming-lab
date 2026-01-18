#Accept N number from user and reverse that array in place

def reverseArray(ilist):
    
    temp = 0
    i=0
    j=len(ilist)-1
    
    while(i < j):
        
        temp = ilist[i]
        ilist[i] = ilist[j]
        ilist[j] = temp
        
        i += 1
        j -= 1
    
    return ilist


def main():
    
    arr = []
    
    iNo = int(input('Enter number of element: '))
    
    print('Enter number: ')
    
    for num in range(iNo):
        value = int(input())
        arr.append(value)
        
    
    iResult = reverseArray(arr)
    
    print(f'Reverse array is: {iResult}')


if __name__ == '__main__':
    main()