# 9. String Number Checker Lambda

# Write a Python program to check whether a given string is a number or not using Lambda.


is_num = lambda num : num.replace('.','',1).isdigit()

# print(is_num('1000'))
# print(is_num('4.2365'))
# print(is_num('-12547'))
# print(is_num('00'))
# print(is_num('A001'))
# print(is_num('001'))



is_num1 = lambda r : is_num(r[1:]) if r[0]=='-' else is_num(r)

print(is_num1('-16.4'))
print(is_num1('-24587.11')) 

