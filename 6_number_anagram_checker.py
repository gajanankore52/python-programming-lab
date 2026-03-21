#Accept 2 Number from user and check whether that number are anagram or not

def is_anagram(num1 ,num2):

    # Convert numbers to strings, sort the characters, and compare
    return sorted(str(num1)) == sorted(str(num2))
    

def main():
    try:
        # Accepting input as string first to preserve structure
        val1 = input('Enter first number : ')
        val2 = input('Enter second number : ')
        
        # Basic check: if they don't have the same length, they can't be anagrams
        if len(val1) != len(val2):
            print(f'{val1} and {val2} are NOT anagrams (different lenghts).')
        
        elif is_anagram(val1,val2):
            print(f'Yes! {val1} and {val2} are anagrams.')

        else:
            print(f'No, {val1} and {val2} are NOT anagrams.')
    except ValueError:
        print("Invalid input. Please enter numbers only.")


if __name__ == '__main__':
    main()