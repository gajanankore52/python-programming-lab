# Python - Swap commas and dots in a String


s = "14, 625, 498.002"

s = s.replace(',', '#')

s = s.replace('.', ',')

s = s.replace('#', '.')
print(s)