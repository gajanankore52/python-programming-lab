# Python: Add two given lists using map and lambda

nums1 = [1, 2, 3,5]
nums2 = [4, 5, 6,5]

res = list(map(lambda a,b:a+b,nums1,nums2))

print(res)