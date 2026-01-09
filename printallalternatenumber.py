#Accept range from user and print all the number in reverse no

def printallnumberalternate(iFrom, iTo):
    
    for i in range( iFrom,iTo+1,2):
        print(i,end =" ")
        


def main():
    
    iStart = int(input("Enter start number: "))
    iEnd = int(input('Enter end number: '))
    
    printallnumberalternate(iStart,iEnd)


if __name__=="__main__":
    
    main()