# Counting the Frequencies in a List Using Dictionary in Python
# Input: ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']

# Output: {'apple': 2, 'banana': 3, 'orange': 1}


def count_frequencies(input_list):
    
    frequencies = {}
    
    for item in input_list:
        
        if item in frequencies:
            # Increment the count if the key exists
            frequencies[item] +=1
        else:
            # Initialize the count to 1 if it's the first time seeing it
            frequencies[item] = 1
    
    return frequencies


# Input
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana']

# Output
result = count_frequencies(data)
print(result)