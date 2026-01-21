# Python - Find all close matches of input string from a list


s = ["Lion", "Li", "Tiger", "Tig"]
a = "Lion"



# for word in s:
    # if word.startswith(a) or a.startswith(word):
        # print(word, end=' ')
        
#==========================


for word in s:
    
    if word == a:
        print(word,end=' ')
        
# ======================================