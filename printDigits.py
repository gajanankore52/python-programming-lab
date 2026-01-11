#accept number form user and print all digit of that number in reverse order


def printDigits(iNo):
    
    print('Digits are: ')
    while (iNo != 0):
        
        digit = iNo %10
        iNo = iNo//10
        
        print(digit)

def main():
    
    iNo = int(input('Enter one number: '))
    
    printDigits(iNo)


if __name__ == '__main__':
    main()