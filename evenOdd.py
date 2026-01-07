#Accept number from user and if no is even then increment the value of that no by 10 and if number is
#odd then decrement the value of that number by 10

def evenOdd(iValue):
    
    if iValue%2==0:
        return iValue+10
    else:
        return iValue-10


def main():
    
    iNo = int(input("Enter number: "))
    
    iRes = evenOdd(iNo)
    
    print('Final answer is:',iRes)
    


if __name__ =="__main__":
    main()