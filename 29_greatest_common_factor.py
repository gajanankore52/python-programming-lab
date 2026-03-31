#Accept two numbers from user and print largest common factor

   
def get_gcf(a, b):
    while b:
        a, b = b, a % b
    return a

def main():
    
    num1 = int(input("Enter First number: "))
    num2 = int(input("Enter second number: "))
    
    print('Largest common factor is: ',get_gcf(num1,num2))

if __name__=="__main__":
    main()