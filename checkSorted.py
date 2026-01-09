#Accept array from user and check whether array is sorted or not


def checkSorted(ilist):
    
    for i in range(len(ilist)-1):
        
        if ilist[i] >= ilist[i+1]:
            break
    
    if i == len(ilist)-2:
        return True
    else:
        return False


def main():
    
    arr = []
    
    iNo = int(input('Enter number of element: '))
    
    print('Enter Numbers: ')
    
    for i in range(iNo):
        value = int(input())
        arr.append(value)
    
    
    iRes = checkSorted(arr)      
    
    if iRes:
        print('List is sorted')
    else:
        print('List is not sorted')


if __name__ == '__main__':
    main()