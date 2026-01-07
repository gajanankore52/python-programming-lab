def maxNo(iVal1,iVal2):

    if iVal1 > iVal2:
        return iVal1
    else:
        return iVal2



def main():

    iNo1 = int(input("Enter First No: "))
    iNo2 = int(input("Enter Second No: "))

    result=maxNo(iNo1,iNo2)

    print("Maximum no is: ",result)





if __name__ == "__main__":
    main()