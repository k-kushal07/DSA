"""
Question:
Write a Python function to calculate the factorial of a given non-negative integer.
The function should take an integer n as input and return the factorial of n.
"""
"""
Input:
5
Output:
120
"""

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)

inp = int(input("Enter a positive number: "))
print(f"Factorial of number {inp} is: ", factorial(inp))