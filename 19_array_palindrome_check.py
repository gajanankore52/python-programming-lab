#Accept N number from user and check whether that array is palindrom or not


def check_palindrome(ilist):
    """Checks if a list is a palindrome using two pointers."""

    i = 0
    j = len(ilist) - 1
    
    while i < j:
        
        if ilist [i] != ilist[j]:
            return False # Exit immediately on mismatch
        
        i += 1
        j -= 1
        
    return True  # If loop completes, it's a palindrome 

def main():
    try: 
        n = int(input('Enter number of elements: ')) 
        print(f'Enter {n} numbers:')
        # Using list comprehension for cleaner input collection
        arr = [int(input()) for _ in range(n)]

            
        if check_palindrome(arr):
            print('Array is a Palindrome')
        else:
            print('Array is NOT a Palindrome')
    except ValueError:
        print("Invalid input! Please enter integers only.")


if __name__ == '__main__':
    main()