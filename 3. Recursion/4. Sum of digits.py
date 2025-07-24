"""
Question:
Write a Python function to calculate the sum of digits of a given number using recursion.
"""
"""
Input:
An integer n (n >= 0).
Output:
The sum of digits of the given number.
"""

def sum_of_digits(num):
    if num == 0:
        return 0

    return num % 10 + sum_of_digits(num // 10)

num = int(input("Enter a number: "))
print(f"The sum of digits of {num} is: {sum_of_digits(num)}")
