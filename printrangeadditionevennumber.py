#Accept range from user and return addition of even nos

def printAdditionEvenNumber(iFrom, iTo):
    
    iSum = 0
    for i in range( iFrom,iTo+1):
        
        if i% 2== 0:
            iSum+= i
            
    return iSum
        

def main():
    
    iStart = int(input("Enter start number: "))
    iEnd = int(input('Enter end number: '))
    
    result = printAdditionEvenNumber(iStart,iEnd)
    
    print("Addition of Even numbers are: ",result)


if __name__=="__main__":
    
    main()