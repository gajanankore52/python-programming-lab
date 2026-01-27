# String slicing in Python to Rotate a String

# Using Slicing

s = "GeeksforGeeks"
d = 2

left = s[d:]+s[:d]

right = s[-d:] + s[:-d]

print(left)
print(right)
