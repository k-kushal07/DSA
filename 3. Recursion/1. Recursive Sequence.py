"""
Question:
Given a number n, find the nth term of the series S, which is defined recursively as:
S(n) = n + n * S(n-1), with S(0) = 1.
"""
"""
Input:
An integer n (n >= 0).
Output:
The nth term of the series S.
"""

def series(n):
    if n <= 0:
        return 1
    return n + n * series(n - 1)

num = int(input("Enter the value of n (n >= 0): "))
print(f"The {n}th term of the series is: {series(num)}")
