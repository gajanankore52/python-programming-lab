#Accept no as x & y and generate the result as x**y 
#input 2,4
#output 16

def power(iVal1,iVal2):
    
    iMult = 1
    
    for i in range(iVal2):
        
        iMult = iMult*iVal1
    return iMult
    
    
def main():
    
    iNo1 = int(input('Enter 1st number : '))
    iNo2 = int(input('Enter 2nd number : '))
    
    result = power(iNo1,iNo2)
    
    print('Result is : ',result)

if __name__=="__main__":
    main()
