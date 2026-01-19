#Accept number from user and return largest digit from that number.


def maxDigit(iNo):
    
    maxDigit = 0
    iCnt = 0
    while(iNo != 0 and maxDigit != 9):
        
        digit = iNo % 10
        
        if maxDigit < digit:
            maxDigit = digit
        
        iNo = iNo // 10
        iCnt += 1
    
    print(iCnt)
    return maxDigit

def main():
    
    iNo = int(input('Enter number: '))
    
    iRes = maxDigit(iNo)
    
    print(f'Max digit is: {iRes}')
    

if __name__ == '__main__':
    main()
    