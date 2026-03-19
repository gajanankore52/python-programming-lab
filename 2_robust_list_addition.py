# === First Approch ===
# Add two given lists using map and lambda

nums1, nums2 = [1, 2, 3,5], [4, 5, 6,5]

result = list( map (lambda a, b : a + b, nums1, nums2) )

print(f"Result: { result }")

# === Second Approch
# From itertools import zip_longest
# Two given lists of potentially different lengths

from itertools import zip_longest
nums1 = [1, 2, 3, 5, 10]
nums2 = [4, 5, 6, 5]

# Using zip_longest to handle unequal lengths, filling missing values with 0
# A cleaner way using a list comprehension with zip_longest:

res_clean = [x + y for x, y in zip_longest(nums1, nums2, fillvalue=0)]

print(f"Result with padding: {res_clean}")