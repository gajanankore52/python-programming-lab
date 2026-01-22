# 8. Datetime Extractor Lambda

# Write a Python program to extract year, month, date and time using Lambda.

# Sample Output:
# 2020-01-15 09:03:32.744178
# 2020
# 1
# 15
# 09:03:32.744178


import datetime


now = datetime.datetime.now()

print(f'now: {now}')

year = lambda x : x.year
month = lambda x:x.month
day = lambda x: x.day
t = lambda x:x.time()



print(f'year:  {year(now)}')
print(f'month: {month(now)}')
print(f'day: {day(now)}')
print(f't: {t(now)}')