# Python - Ways to remove multiple empty spaces from string List

li = ["Hello   world", "   Python is  great  ", "   Extra  spaces here  "]

str1= list()

#Using str.split() and str.join()

# res = [ ' '.join(str.split()) for str in li]
    
# print(res)
# ===============================================

res = "   Python is  great  "

print(res.split())