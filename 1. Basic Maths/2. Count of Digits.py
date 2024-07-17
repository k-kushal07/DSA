"""
Question:
Write a Python function to count the number of digits in a given number.
Given an integer n, the function should return the count of digits in n.
"""
"""
Input:
An integer n.
Output:
An integer representing the number of digits in n.
"""

# Solution 1
inp = input("Enter a positive integer: ")
print(f"Count of digits in number {inp} is: ", len(inp))


# Solution 2
def count_digits(num):
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count

inp = int(input("Enter a positive integer: "))
print(f"Count of digits in number {inp} is: ", count_digits(inp))
