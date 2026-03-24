# Calculate the sum of two numbers given as strings

# Sample Data:
# Input: ('234242342341', '2432342342') -> Output: 236674684683
# Input: ('', '2432342342') -> Output: False
# Input: ('1000', '0') -> Output: 1000      
# Input: ('1000', '10') -> Output: 1010  

def calculate_string_sum(data_tuple):
    # Requirement: If any string is empty, return False
    
    if not all(data_tuple):
        return False
    
    # Convert all strings in the tuple to integers and sum them
    total = sum(map(int,data_tuple))

    # Return as a string to match your sample data format
    return str(total)

def main():
    # Test cases based on your sample data
    samples = [
        ("234242342341", "2432342342"),
        ("", "2432342342"),
        ("1000", "0"),
        ("1000", "10")
    ]

    for sample in samples:
        result = calculate_string_sum(sample)
        # print(f'Input: {sample} -> Output: {result}')


if __name__ == "__main__":
    main()