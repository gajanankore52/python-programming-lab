 #Accept no from user and check whether that no is perfect or not

def checkPerfect(iVal):
    
    iSum=0
    
    for i in range(1,(iVal//2)+1):
        if iVal % i==0:
            iSum=iSum+i
    
    if iSum==iVal:
        return True
    else:
        return False


def main():
    
    
    iNo = int(input('Enter one number: '))
    
    bResult = checkPerfect(iNo)
    
    if bResult:
        print('Number is perfect..')
    else:
        print('Number is not perfect')

if __name__ =="__main__":
    main()