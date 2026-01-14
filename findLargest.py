#Accept list from user and findout largest subarray which is sorted incresingly

def findLargest(ilist):
    
    iMax,iMin,iStart,iEnd = 0,0,0,0
    
    for i in range(len(ilist)-1):
        
        if ilist[i] <= ilist [i+1]:
            iEnd = i+1
        else:
            if (iMax - iMin) < (iEnd - iStart):
                iMin = iStart
                iMax = iEnd
        
            iStart,iEnd = i+1,i+1     
        
    print(f'Largest Subarray starts from {iMin} and End at {iMax}')
    
    
def main():
    
    arr = []
    
    iNo = int(input('Enter number of elements: '))
    
    print('Enter numbers: ')
    
    for i in range(iNo):
        value = int(input())
        arr.append(value)
        
    findLargest(arr)

if __name__ == '__main__':
    main()