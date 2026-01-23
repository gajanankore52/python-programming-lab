# Python - Avoid Spaces in string length

s = "geeks for geeks"

# res = len(s.replace(' ',''))

# print(res)
# ======================# ==============# ==============# ==============

# res = ''
# for ch in s:
    # if ch != ' ':
       # res += ch

# print(len(res))       

# ==============# ==============# ==============# ==============

# res =len([ch for ch in s if ch != ' '])

# print(res)

# ==============# ==============# ==============# ==============


res = len(list(filter(lambda ch : ch!= ' ',s)))

print(res)
