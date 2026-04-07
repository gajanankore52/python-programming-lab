# Python: Count the even, odd numbers in a given array of integers using Lambda

array_nums = [1, 2, 3, 5, 7, 8, 9, 10]

# True evaluates to 1, False to 0
# We count even numbers in one go
evens_count = sum(1 for x in array_nums if x % 2 == 0)
odds_count = len(array_nums) - evens_count

print(f"Even numbers: {evens_count}")
print(f"Odd numbers: {odds_count}")

