# Convert a List of Characters into a String - Python

a = ['P', 'y', 't', 'h', 'o', 'n']

# The empty string '' is the separator. 
# It tells Python: "Take every element and stick them together with nothing in between."
res = "".join(a)

print(res)
#==================================

# Using reduce()


from functools import reduce

a = ['P', 'y', 't', 'h', 'o', 'n']
res = reduce(lambda x,y: x+y,a)
print(res)

