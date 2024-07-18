"""
Question:
Write a Python function to check whether a given integer is a palindrome.
A palindrome is a number that reads the same backward as forward.
The function should take an integer and return True if the number is a palindrome,
and False otherwise.
"""
"""
Input:
An integer n
12321
Output:
Boolean representing whether the provided number is palidrome or not.
True
"""

def is_palindrome(num):
    temp_num = num
    reversed_num = 0

    while(temp_num):
        remainder = temp_num % 10
        reversed_num = temp_num * 10 + remainder
        temp_num //= 10
        
    return original_num == reversed_num
        
inp = int(input("Enter a positive number: "))
print(f"Is the number {inp} palindrome?", is_palindrome(inp))