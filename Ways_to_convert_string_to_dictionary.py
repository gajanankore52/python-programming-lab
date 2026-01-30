# Ways to convert string to dictionary

s = "{'a': 1, 'b': 2, 'c': 3}"

res =s.split('"')

iCnt=0
for word in res:
    print(word, end="\n ")
    iCnt +=1
    
print(iCnt)

