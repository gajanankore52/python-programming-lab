#Accept number from user and return such a digit which occures maxmum no of times


def maxDigit(iNo):
    
    
    
    max = 0
    maxDigit = 0
    ilist = [0,0,0,0,0,0,0,0,0]
    
    while(iNo != 0):
        
        digit = iNo % 10
        
        ilist[digit] = ilist[digit] + 1
        
        iNo = iNo //10
        
    
    for iCnt in range(9):
        
        if ilist[iCnt] > max :
            
            max = ilist[iCnt]
            maxDigit = iCnt
    
    return maxDigit


def main():
    
    iNo = int(input('Enter Number : '))
    
    iResult = maxDigit(iNo)
    
    print(f'Maximum occurs number is: {iResult} ')

if __name__ == '__main__':
    main()