#Accept no from user and print table of that number (10 multiple of that number)
#input 5
#output 5 10 15 20 25 30 35 40 45 50

def main():
    
    iNo = 5
    
    for i in range(1,11):
        print(iNo*i,end=" ")


if __name__=="__main__":
    main()