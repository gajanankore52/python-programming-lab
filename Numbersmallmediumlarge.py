#Accept no from user and display below output
#if no is less than 50 = small
#if no is greater than 50 and less than 100 = medium
#if no is greater then 100 = large


def main():
    
    iNo = int(input("Enter one number: "))
    
    if iNo < 50:
        print("Small")
    elif iNo >= 50 and iNo < 100:
        print("Medium")
    else:
        print("Large")


if __name__=="__main__":
    main()