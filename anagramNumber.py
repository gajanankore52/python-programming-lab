#Accept Number fromuser and check whether that number are anagram or not



def checkAnagram(iNo1, iNo2):
    
    
    ilist1 = [0]*10
    ilist2 = [0]*10
    
    while(iNo1 != 0):
        
        digit = iNo1 % 10
        ilist1[digit] = ilist1[digit] + 1
        iNo1 = iNo1 // 10
        
    while(iNo2 != 0):
        
        digit = iNo2 % 10
        ilist2[digit] = ilist2[digit] + 1
        iNo2 = iNo2 // 10
        
   

    for i in range(len(ilist1)):
        
        if ilist1[i] != ilist2[i]:
            break
    else:
        return True
    

def main():
    
    
    iNo1 = int(input('Enter First number : '))
    iNo2 = int(input('Enter Second number : '))
    
    iResult = checkAnagram(iNo1,iNo2)
    
    print('Number is Anagram ')if iResult else print('Number is not Anagram')


if __name__ == '__main__':
    main()