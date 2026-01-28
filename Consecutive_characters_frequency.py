# Consecutive characters frequency - Python


# s = "aaabbccaaaa"

# temp=0
# res = []
# b=''
# for i in range(len(s)):
    # i=temp
    # b=''    
    # for j in range(i,len(s)):        
        
        # if s[i] == s[j]:            
            # b += s[i]

        # # if s[i] != s[j]:            
        # else:
            # temp = j
            # res.append(b)
            # break
    # if j==len(s)-1:
        # res.append(b)
        # break
# print(res)
#===============================================

s = "aaabbccaaaa"

res = []
count = 1

for i in range(0,len(s)-1):

    if s[i] == s[i+1]:
        count +=1
    else:
        res.append(s[i]*count)
        count=1
res.append(s[i]*count)
print(res)
            