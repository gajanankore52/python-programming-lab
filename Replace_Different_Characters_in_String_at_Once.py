# Python - Replace Different Characters in String at Once


s = 'geeksforgeeks is best'


d = {'e': '1', 'b': '6', 'i': '4'}

s1=''

# for ch in s:
    # if ch in d:
        # s1 +=d[ch]
    # else:
        # s1 +=ch

# print(s1)

# ===================

res =''.join([d[ch] if ch in d else ch for ch in s])

print(res)