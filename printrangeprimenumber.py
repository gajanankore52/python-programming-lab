#Accept range from user and print all prime numbers

def printAllPrime(iFrom, iTo):
    
    print("All Prime numbers are: ")
    
    for i in range( iFrom,iTo+1):
        
        iNo = i
        for number in range(2,(iNo//2)+1):
            if iNo % number==0:
                break
        
        if number==iNo//2:
            print(iNo,end=" ")
        
        

def main():
    
    iStart = int(input("Enter start number: "))
    iEnd = int(input('Enter end number: '))
    
    printAllPrime(iStart,iEnd)


if __name__=="__main__":
    
    main()