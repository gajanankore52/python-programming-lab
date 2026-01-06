#Accept range from user and print all perfect numbers

def printAllPerfect(iFrom, iTo):
    
    print("All Perfect numbers are: ")
    iSum = 0
    for i in range( iFrom,iTo+1):
        
        iNo = i
        for number in range(1,(iNo//2)+1):
            if iNo % number==0:
                iSum =iSum+number
        
        if iNo==iSum:
            print(iNo,end=" ")
        
        iSum = 0

def main():
    
    iStart = int(input("Enter start number: "))
    iEnd = int(input('Enter end number: '))
    
    printAllPerfect(iStart,iEnd)


if __name__=="__main__":
    
    main()