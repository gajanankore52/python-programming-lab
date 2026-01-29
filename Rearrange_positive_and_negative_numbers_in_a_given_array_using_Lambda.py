# Python: Rearrange positive and negative numbers in a given array using Lambda

array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]
              # [2, 5, 7, 8, 9, -10, -3, -1]

res = sorted(array_nums,key=lambda i:0 if i==0 else -1/i)
print(res)

