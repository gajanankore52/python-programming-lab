#How to Remove Letters From a String in Python


s = "hello world"

str = ''
letter = 'l'

# for ch in s:
    
    # if ch != letter:
        # str += ch   
        
# print(str)

# ======================


# result = s.replace('l','')
# print(result)
    
    
# =============================


# result  = ''.join([ch for ch in s if ch !='l'])

# print(result)


# ==========================

s = "hello world"
idx = s.find('o')


if idx != -1 :
    s = s[:idx] + s[idx+1:]
    
print(s)