# Python: Convert string element to integer inside a given tuple using lambda


tuple_str =  (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))

# Unpacking (id, label, value) makes the logic self-documenting
result = tuple(map(lambda item: (int(item[0]), int(item[2])), tuple_str))

print(result)