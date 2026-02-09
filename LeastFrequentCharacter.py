 # Python - Least Frequent Character in String

# from collections import Counter
# s = "GeeksforGeeks"
# freq = Counter(s)

# # print(freq)

# res = min(freq , key=freq.get)

# print(res)

# =================================

# s = "GeeksforGeeks"

# new = {}

# iCnt = 0

# for i in range(len(s)-1):
    # iCnt = 1
    # for j in range(i+1,len(s)):
        # if s[i] not in new:
            # if s[i]==s[j]:
                # iCnt += 1
        # if s[i] in new:
            # break
    # if s[i] not in new:
        # new[s[i]] = iCnt

# res = min(new,key=new.get)
# print(res)

# ======================



s = "GeeksforGeeks"

res = min(s, key = lambda char:s.count(char))

print(res)

