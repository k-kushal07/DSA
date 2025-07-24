"""
Question:
Write a Python function to convert a given non-negative integer to its binary representation using recursion.
"""
"""
Input:
An integer n (n >= 0).
Output:
A string representing the binary form of the number.
"""

def binary_conversion(n):
    # Base case: binary of 0 or 1 is the number itself
    if n == 0:
        return "0"
    if n == 1:
        return "1"

    # Recursive case: binary of n is binary of n//2 followed by n%2
    return to_binary(n // 2) + str(n % 2)

# Input
num = int(input("Enter a non-negative integer: "))

# Output
print(f"Binary representation of {n} is: {binary_conversion(num)}")
