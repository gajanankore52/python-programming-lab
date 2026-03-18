# Write a program which will find all such numbers which are divisible by 7 but are not a divisible of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# Create an empty list to store the results
results = []

# Iterare through the range from 2000 to 3200 (3201 is used to include 3200)

for num in range(2000,3201):
    if (num % 7 ==0) and (num % 5!=0):
        # Convert to string to make joining easier later
        results.append(str(num))
        
# Print the list as a comma-separated string

print(','.join(results))