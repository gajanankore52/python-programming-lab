# Write a Python program to unzip a list of tuples into individual lists


# Input list of tuple

l = [(1, 2),(3, 4),(8, 9)]

# Use zip with the unpacking operator *
# This effectively call zip((1, 2), (3, 4), (8, 9))

unzipped = list(zip(*l))

print(unzipped)