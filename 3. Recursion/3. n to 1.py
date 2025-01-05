"""
Question:
Write a Python function to print numbers from n to 1 using recursion.
"""
"""
Input:
An integer n.
Output:
Numbers from n to 1 printed on the same line.
"""

def descending_order(n):
    if n <= 0:
        return
    
    print(n, end=" ")
    descending_order(n-1)

num = int(input("Enter a positive integer: "))
descending_order(num)
