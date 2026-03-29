# Python Program to Accept the Strings Which Contains all Vowels

def contains_all_vowels(input_string):
    # Define vowels as a set 
    vowels = set('aeiou')

    # Convert input to lowercase and into a set once
    # This checks if vowels is a subset of the characters in the string

    return vowels.issubset(input_string.lower())


def main():
    test_cases = [
            "Education",        # True (contains a, e, i, o, u)
            "Geeksforgeeks",   # False
            "Abstentious",     # True
            "Python"           # False
        ]

    for word in test_cases:
        result = contains_all_vowels(word)
        print(f"'{word}' contains all vowels: {result}")


if __name__ == "__main__":
    main()