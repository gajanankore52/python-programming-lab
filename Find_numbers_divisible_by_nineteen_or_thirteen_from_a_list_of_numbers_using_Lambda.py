# Python: Find numbers divisible by nineteen or thirteen from a list of numbers using Lambda


nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]


res =list(filter(lambda x: (x% 19 ==0 or x%13==0),nums))

print(res)