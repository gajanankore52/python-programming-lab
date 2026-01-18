# Frequency of Numbers in String 


s = "geeks4feeks is No. 1 4 geeks"


iCnt =  0

# for i in range(len(s)):
    # if s[i].isdigit():
        # iCnt +=1

# print(iCnt)
# ========================


# s = "geeks4feeks is No. 1 4 geeks"

# res = sum(map(lambda x:x.isdigit(),s))

# print(res)

# ======================================


s = "geeks4feeks is No. 1 4 geeks"

iCnt = 0

digits = '0123456789'

for i in s:
    if i in digits: iCnt+=1
    

print(iCnt)
        