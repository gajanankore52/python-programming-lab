# python program to print even length words in a string


# Using list comprehension

s = "This is a python language"

# s =s.split()

# res = [word for word in s if len(word)% 2 == 0]
# print(res)

# ===========================================================


# Using filter()

# s = "Python is great"
# s = s.split()

# res =' '.join(list(filter(lambda word : len(word)%2==0, s)))

# print(res)

# ===========================================================


# Using for loop

a = "My name is shakshi"

s = a.split()

for word in s:
    
    if len(word)%2 == 0:
        print(word,end = ' ')
        
        
