# Write a Python function to check if a list is a palindrome or not. Return true otherwise false.

def is_palindrome(lst):
    # Handle empty lists or single items (technically palindromes)

    if not lst:
        return True
    
    # Two-Pointer Approach (Memory Efficient)
    # This avoids creating a full copy of the list
    left = 0
    right = len(lst) - 1

    while left < right:
        # If any elements don't match, it's not a palindrom
        if lst[left] != lst[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Alternative: The "All" Generator (Very Pythonic)
def is_palindrome_fast(lst):
    # Compares the first half with the reversed second half
    
    return all(lst[i] == lst[-1-i] for i in range(len(lst) // 2))


def main():

    test_cases = [
        ([1,2,3,2,1], "Numeric Palindrome"),
        (['a','b','c'], "Non-Palindrome"),
        (['R', 'a', 'd', 'a', 'r'], "Case-Sensitive Check"),
        ([], "Empty List")
                ]

    for data, label in test_cases:
        result = is_palindrome_fast(data)
        print(f"{label}: {data} -> {result}")


if __name__ == "__main__":
    main()