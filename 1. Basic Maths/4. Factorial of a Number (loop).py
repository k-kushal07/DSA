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
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

inp = int(input("Enter a positive number: "))
print(f"Factorial of number {inp} is: ", factorial(inp))