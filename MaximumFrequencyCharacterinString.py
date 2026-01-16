# Maximum Frequency Character in String - Python


# s = "Gznjznzn"

# dic = {}
# iCnt = 0
# for i in range(len(s)):
    # iCnt = 1
    
    # for j in range(i+1,len(s)-1):
        # if s[i] not in dic:
            # if s[i]==s[j]:
                # iCnt +=1
    # if s[i] not in dic:
        # dic[s[i]]=iCnt

# # print(dic)

# res = max(dic,key=dic.get)        

# print(res)
# ====================


# from collections import Counter

# s = "hello world"

# # Count the frequency of characters
# frequency = Counter(s)

# print(max(frequency,key=frequency.get))
    
# ===============

# s = "hello world"

# # Create a dictionary to store character frequencies
# freq = {}

# # Count the frequency of each character
# for char in s:
    # freq[char] = freq.get(char,0)+1


# # Get the character with the maximum frequency
# max_char = max(freq, key=freq.get)

# print(max_char)
# ==================


# s = "hello world"

# # Sort the string and find the character with the maximum frequency
# max_char = sorted(set(s), key=lambda char: s.count(char), reverse=True)[0]

# # print(sorted(set(s)))
# print(max_char)
# =====================================


