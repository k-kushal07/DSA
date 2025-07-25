"""
Question:
Write a Python function to find the floor of the square root of a non-negative integer using binary search.
"""
"""
Input:
A non-negative integer n.
Output:
An integer representing the floor value of sqrt(n).
"""

def floor_sqrt(n):
    if n < 2:
        return n

    low, high = 1, n // 2
    ans = 1

    while low <= high:
        mid = (low + high) // 2
        if mid * mid == n:
            return mid
        elif mid * mid < n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1

    return ans

n = int(input("Enter a non-negative integer: "))
print(f"The floor square root of {n} is: {floor_sqrt(n)}")
