#Accept no from user and check whether that no is prime or not

def checkprime(iVal):
    
    for i in range(2,iVal//2+1):
        if iVal % i==0:
            break
    
    
    if i==iVal//2:
        return True
    else:
        return False


def main():
    
    iNo = int(input("Enter number: "))
    
    bRes = checkprime(iNo)
    
    if bRes:
        print('Prime number ')
    else:
        print('Not Prime')
    


if __name__ =="__main__":
    main()