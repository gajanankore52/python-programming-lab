#Accept range from user and return difference betwwn summation of factors and non factors


def sumFactor(iNo):
    
    iSum1=iSum2= 0
    
    for i in range(1,iNo+1):
        
        if iNo % i== 0:
            iSum1 = iSum1+i
        else:
            iSum2 = iSum2+i
    
    print(iSum1)
    print(iSum2)
            
    return iSum1-iSum2
        

def main():
    
    iNo = int(input("Enter one number: "))
    
    result = sumFactor(iNo)
    
    print("Answer is: ",result)


if __name__=="__main__":
    
    main()