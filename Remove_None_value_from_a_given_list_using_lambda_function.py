# Python: Remove None value from a given list using lambda function


nums = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]

# 1st Way
result = list(filter(lambda x: x is not None,nums))

print(result)
# =====================================

# 2nd Way

result = list(filter(lambda x: x if isinstance(x, int) else None,nums))

print(result)