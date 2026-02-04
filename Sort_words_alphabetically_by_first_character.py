#Sort words alphabetically by first character.

# Sample Data
# Input -> “Red Green Black White Pink”

# Output -> "Black Green Pink Red White”

str1 = "Calculate the sum of two said numbers given as strings."

str1 = str1.split(' ')

result = sorted(str1, key = lambda x:x[0])

print(' '.join(result))

