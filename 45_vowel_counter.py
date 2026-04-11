# Count Number of Vowels using Sets in Given String - Python


s = "Set operations in Python"
vowels = set("aeiouAEIOU")

# Method: Filter and Count
# This is highly readable and handles every instance of a vowel
res = sum(1 for char in s if char in vowels)

print(f"Total Vowels: {res}")