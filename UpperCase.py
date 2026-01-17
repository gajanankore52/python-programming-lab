# Python - Uppercase Half String



# Using String Slicing

# s = "hello"

# iCnt = len(s)//2

# res = s[:iCnt].upper() + s[iCnt:]
# print(res)
# ======================================

s = "hello"

iCnt = len(s) // 2



res =''.join([s[i].upper() if i< iCnt else s[i] for i in range(len(s))])
print(res)