# Write a Python program to extract year, month, date and time using Lambda.

# Sample Output:
# 2020-01-15 09:03:32.744178
# 2020
# 1
# 15
# 09:03:32.744178


import datetime

# Get current date and time
now = datetime.datetime.now()
print(f"Full Timestamp: {now}\n")

# Store extraction logic in a dictionary for cleaner access
extractors = {
    "Year": lambda x: x.year,
    "Month": lambda x: x.month,
    "Day": lambda x: x.day,
    "Time": lambda x: x.time()
}

# Iterate through extractors to display results
for label, func in extractors.items():
    print(f"{label}: {func(now)}")