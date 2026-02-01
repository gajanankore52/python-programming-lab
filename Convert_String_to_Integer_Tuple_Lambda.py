# Python: Convert string element to integer inside a given tuple using lambda


tuple_str =  (('233', 'ABCD', '33'), ('1416', 'EFGH', '55'), ('2345', 'WERT', '34'))

result = tuple(map(lambda x:(int(x[0]),int(x[2])),tuple_str))

print(result)