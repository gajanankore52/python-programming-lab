# Write a Python function to check if a list is a palindrome or not. Return true otherwise false.

def is_palindrome(lst):
    """
    Checks if a list ia a palindrome
    Return True if it is, false oterwise.
    """
    
    return lst ==lst[::-1]


# Usage
print(is_palindrome([1,2,3,2,1]))
print(is_palindrome(['a','b','c']))