#Accpet N number from user and return smallest perfect number


def smallPerfectNumber(ilist):
    
    smallPerfect = 0
    
    for num in range(len(ilist)):
        
        iNo = ilist[num]
        iSum = 0
        for value in range(1,iNo//2+1):
            if iNo % value == 0:
                iSum += value
                
        if iSum == iNo:
            print(f'Perfect no is: {iNo}')



def main():
    
    arr = []
    
    iNo = int(input("Enter number of element: "))
    
    print("Enter number: ")
    for i in range(iNo):
        value = int(input())
        arr.append(value)
        
        
    
    smallPerfectNumber(arr)
    
    # print(f"Smallest perfect number is: {result")


if __name__ == "__main__":
    main()