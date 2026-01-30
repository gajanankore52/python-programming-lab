# Split and join a string in Python


# Using split() and join()
# a = "Hello, how are you?"

# b = a.split()
# b = ' '.join(b)

# print(b)

#=================================

a = "Hello, how are you?"

b = [word for word in a.split()]

b = ' '.join(b)

print(b)