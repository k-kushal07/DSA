"""
Question:
Write a Python function to find the sum of the first n natural numbers.
A natural number is any positive integer (1, 2, 3, ...).
Given an integer n, the function should return the sum of all natural numbers from 1 to n.
"""

"""
Input:
An integer n representing the number of natural numbers to sum.

Output:
An integer representing the sum of the first n natural numbers.
"""

def sum_of_natural_numbers(num):
    if num < 1:
        return -1
    return num * (num + 1) // 2

inp = int(input("Enter a positive integer: "))
print(f"Sum of First {inp} natural numbers is:",  sum_of_natural_numbers(inp))