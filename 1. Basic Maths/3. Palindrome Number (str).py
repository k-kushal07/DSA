"""
Question:
Write a Python function to check whether a given integer is a palindrome.
A palindrome is a number that reads the same backward as forward.
The function should take an integer and return True if the number is a palindrome,
and False otherwise.
"""
"""
Input:
12321
Output:
Boolean representing whether the provided number is palidrome or not.
True
"""

def is_palindrome(num):
    return num == num[::-1]
        
inp = int(input("Enter a positive number: "))
print(f"Is the number {inp} palindrome?", is_palindrome(inp))