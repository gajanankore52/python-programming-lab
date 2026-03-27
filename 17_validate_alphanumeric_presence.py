# Python program to check if a string has at least one letter and one number

def has_letter_and_number(s):

    # Flags to track if we've found what we need
    has_letter = False
    has_digit = False

    # One single pass through the string
    for char in s:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_digit = True
        
        # Optimization: If both are found, we can stop immediately
        if has_letter and has_digit:
            return True
    
    return False

def main():
    test_strings = [
        "geeksfo1rgeeks",  # True
        "python",          # False (no number)
        "12345",           # False (no letter)
        "!!1a!!"           # True
    ]

    for text in test_strings:
        result = has_letter_and_number(text)
        print(f"'{text}' -> {result}")
 
if __name__ == "__main__":
    main()