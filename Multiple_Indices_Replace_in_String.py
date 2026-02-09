# Multiple Indices Replace in String - Python


s = "geeksforgeeks is best"
li = [2, 4, 7, 10]
ch = '*'

str1 = ''


# Using For Loop

# iCnt = 0
# for i in range(len(s)):
    
    # if iCnt in li:
        # str1 += ch
    # else:
        # str1 +=s[i]
    # iCnt += 1
# print(str1)
        
#==================================

#Using String Slice

# s1 = ''
# for iCnt in li:
    # s = s[:iCnt] + ch + s[iCnt+1:]

# print(s)
# =====================================


#Using List Comprehension

# s = "geeksforgeeks is best" 
# li = [2, 4, 7, 10]  # Indices to replace   
# ch = '*'     # Replacement character

# temp = list(s)

# res = ''.join([ch if idx in li else ele for idx,ele in enumerate(temp)])

# print(res)

#========================================

#Using map function



s = "geeksforgeeks is best"  
li = [2, 4, 7, 10]  # Indices to replace
ch = '*'

res = ''.join(map(lambda x : ch if x[0] in li else x[1] ,enumerate(s)))

print(res)

print(list(enumerate(s)))