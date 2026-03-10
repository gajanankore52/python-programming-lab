# Write a Python program to find repeated items in a tuple.

# A tuple with repeated elements

my_tuple = (10, 20, 30, 20, 40, 50, 30, 30, 60, 10)

# def find_repeats(tup):
    
    # seen = set()
    # repeats = set()
    
    # for item in tup:
        # if item in seen:
            # repeats.add(item)
        # else:
            # seen.add(item)
            
    # return list(repeats)


# result = find_repeats(my_tuple)
# print(f"Repeated items: {result}")



from collections import Counter

# A tuple with various repeated items
data = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)

# Count occurrences of all items
counts = Counter(data)

# Filter for items with a count greater than 1
repeats = {item: count for item, count in counts.items() if count > 1}

print(f"Repeated items and their counts: {repeats}")


from collections import Counter

# A tuple with various repeated items
data = (1, 2, 2, 3, 3, 3, 4, 4, 4, 4)

# Count occurrences of all items
counts = Counter(data)

# Filter for items with a count greater than 1
repeats = {item: count for item, count in counts.items() if count > 1}

print(f"Repeated items and their counts: {repeats}")
