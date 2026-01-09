#Accept N number from user and return largest prime number


def largestPrimeNumber(ilist):
    
    lPrime = 0
    iCnt = 0
    iMax=2
    for ele in range(len(ilist)):
        
        iNum = ilist[ele]
        
        for iCnt in range(2,(iNum//2)+1):
            
            if iNum % iCnt ==0:
                break
        
        if iCnt == iNum//2:
            
            if iMax <iNum:
                iMax=iNum
                
                
    return iMax          
   

def main():
    
    arr = []
    
    iNo = int(input("Enter no of element: "))
    
    print(f"Enter {iNo} Numbers: ")
    
    for i in range(iNo):
        value = int(input())        
        arr.append(value)

    iResult = largestPrimeNumber(arr)
    
    print("Largest Prime number is: ",iResult)

if __name__ =="__main__":
    main()