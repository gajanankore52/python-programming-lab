# Write a Python program to reverse strings in a given list of string values using lambda.
# Original lists:
# ['Red', 'Green', 'Blue', 'White', 'Black']

# Reverse strings of the said given list:
# ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']

colors_list = ["Red", "Green", "Blue", "White", "Black"]

result = list(map(lambda x:x[::-1],colors_list))

print(result)