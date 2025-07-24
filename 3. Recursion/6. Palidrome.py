"""
Question:
Write a Python function to check if a given string is a palindrome using recursion.
A palindrome is a string that reads the same forwards and backwards.
"""
"""
Input:
A string (can contain lowercase/uppercase letters, digits, symbols).
Output:
True if the string is a palindrome, False otherwise.
"""

def is_palindrome(s):
    # Base case: If the string is empty or has one character, it's a palindrome
    if len(s) <= 1:
        return True
    
    # If the first and last characters are not the same, it's not a palindrome
    if s[0] != s[-1]:
        return False
    
    # Recursive case: check the substring excluding first and last character
    return is_palindrome(s[1:-1])

# Input
input_str = input("Enter a string: ")

# Output
print(f"Is '{input_str}' a palindrome? {is_palindrome(input_str)}")
