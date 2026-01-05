#write a program which accept one no and we have to check whether that no is even or odd



def checkEven(iVal):
    
    if iVal % 2 == 0:
        return True
    else:
        return False


def main():
    
    iNo = int(input("Enter One no: "))
    
    bResult = checkEven(iNo)
    
    if bResult == True:
        print("Number is Even")
    else:
        print("Number is Odd")


if __name__=="__main__":
    main()