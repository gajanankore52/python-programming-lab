 # Accept range from user and perform addition of all the element in that range

def sumofAddition(iStart, iEnd):
    
    iSum = 0
    
    for i in range(iStart,iEnd+1):
        
        iSum = iSum+i
    
    return iSum

def main():
    
    iStart = int(input("Enter First number: "))
    iEnd = int(input("Enter Last number: "))
    
    iRes = sumofAddition(iStart,iEnd)
    
    print("Addition is: ",iRes)


if __name__=="__main__":
    main()
