"""
Question:
Write a Python function to print numbers from 1 to n using recursion.
"""
"""
Input:
An integer n (n > 0).
Output:
Numbers from 1 to n printed on separate lines.
"""

def ascending_order(n):
    if n == 0:
        return
    ascending_order(n - 1)
    print(n, end=" ")

num = int(input("Enter a positive integer: "))
ascending_order(num)