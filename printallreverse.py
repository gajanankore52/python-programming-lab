#Accept range from user and print all the number in reverse no

def printallnumberreverse(iFrom, iTo):
    
    for i in range(iTo, iFrom-1,-1):
        print(i,end =" ")
        


def main():
    
    iStart = int(input("Enter start number: "))
    iEnd = int(input('Enter end number: '))
    
    printallnumberreverse(iStart,iEnd)


if __name__=="__main__":
    
    main()