# Python: Find intersection of two given arrays using Lambda



array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
array_nums2 = [1, 2, 4, 8, 9]



res = list(filter(lambda x : x in array_nums2,array_nums1))

print(res)
