# Python: Count the even, odd numbers in a given array of integers using Lambda

array_nums = [1, 2, 3, 5, 7, 8, 9, 10]


even_no = list(filter(lambda x:x %2==0,array_nums))
odd_no = list(filter(lambda num:num %2 != 0,array_nums))

print(len(even_no))
print(len(odd_no))

