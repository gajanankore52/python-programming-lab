#Accept N number from user and check whether that array is palindrom or not


def checkPalindrom(ilist):
    
    i=0
    j=len(ilist)-1
    
    while (i < j):
        
        if ilist [i] != ilist[j]:
            break
        
        i += 1
        j -= 1
        
    if i >= j:
        return True
    else:
        return False  
   

def main():
    
    arr = []
    
    iNo = int(input('Enter number of elements: '))
    
    print('Enter numbers: ')
    
    for i in range(iNo):
        
        value = int(input())
        arr.append(value)

    iRes = checkPalindrom(arr)
    
    if iRes :
        print('Array is Palindrom ')
    else:
        print('Array is not Palindrom')
        

if __name__ == '__main__':
    main()