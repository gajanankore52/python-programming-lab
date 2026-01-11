#Accept number from user and return its generic root 



def genericRoot(iNo):
    
    iSum = 0
    
    
    while(1):
        
        iSum = 0
        while(iNo != 0):
            
            digit = iNo % 10
            iSum = iSum + digit
            iNo = iNo // 10
        
        if iSum > 9:
            iNo = iSum
        else:
            break
    
    return iSum


def main():
    
    iNo = int(input('Enter number : '))
    
    iResult = genericRoot(iNo)
    
    print(f'Generic root of {iNo} is {iResult}')


if __name__ == '__main__':
    main()