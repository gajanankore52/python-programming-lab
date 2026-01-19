#Accept range from user and print all the number from that range

def printallnumber(iFrom, iTo):
    
    for i in range(iFrom, iTo+1):
        print(i,end =" ")
        


def main():
    
    iStart = int(input("Enter start number: "))
    iEnd = int(input('Enter end number: '))
    
    printallnumber(iStart,iEnd)


if __name__=="__main__":
    
    main()

