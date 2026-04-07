#Write a python program to count repeated characters in a string.


from collections import Counter

def count_duplicates(text, ignore_spaces=True):
    # Remove spaces if requested to avoid counting them as characters
    if ignore_spaces:
        text = text.replace(" ", "")
        
    # Counter creates the frequency map
    counts = Counter(text)
    
    # Filter for items with a count > 1
    return {char: count for char, count in counts.items() if count > 1}

# Execution
sample_str = 'thequickbrownfoxjumpsoverthelazydog'
result = count_duplicates(sample_str)

print(f"Repeated Characters: {result}")