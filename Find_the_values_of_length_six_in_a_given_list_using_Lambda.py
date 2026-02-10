# Python: Find the values of length six in a given list using Lambda


weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


res = list(filter(lambda days:days if len(days)==6 else '',weekdays))

print(res)
