#Accept number from user and print its factors
#input 36
#output 1 2 3 4 6 12 18

def printFactors(iVal):
    
    print("Factors of", iVal , "is:")
    for i in range(1,(iVal//2)+1):
        if iVal%i == 0:
            print(i,end =" ")
        


def main():
    
    iNo = int(input("Enter number: "))
    
    printFactors(iNo)
    

if __name__=="__main__":
    main()