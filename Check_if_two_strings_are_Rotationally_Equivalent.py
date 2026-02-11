# Python - Check if two strings are Rotationally Equivalent



str1 = 'geeks'
str2 = 'eksge'

flag=False
for i in range(len(str1)):
    
    if str1[i:] + str1[:i] == str2:
        flag=True
        break

   
                
print(f"Are two strings Rotationally equal ? : {flag}")