d#Accept range from user and display all prime nos in that range


def rangePrime(iStart, iEnd):
    
    print('Prime nos are: ')
    for no in range(iStart,iEnd+1):
        
        iNo=no
        for i in range(2,iNo//2+1):
            if iNo%i==0:
                break
        
        if i==iNo//2:
            print(iNo)
            
            
        
def main():
    
    iStart = int(input("Enter first number: "))
    iEnd = int(input("Enter last number: "))
    
    rangePrime(iStart,iEnd)

if __name__=="__main__":
    main()