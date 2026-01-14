# Python program to capitalize the first and last character of each word in a string


s = "gajanan kore"

# O/p = HellO WorlD

s =s.split()

# ch = ''
# for word in s:
    
    # iCnt = len(word)
    # ch += word[0].upper() + word[1:iCnt-1] + word[iCnt-1].upper() + ' '
    
# print(ch)

# ==============================================


# s = "hello world"


# w = s.split()

# res = ' '.join([  
    
    # i[0].upper() + i[1:-1] + i[-1].upper() for i in w])
    
    
# print(res)

# ==================================================

s = "welcome to geeksforgeeks"

res =' '.join(map(lambda word : word[0].upper() + word[1:-1] + word[-1].upper(),s.split()))

print(res)