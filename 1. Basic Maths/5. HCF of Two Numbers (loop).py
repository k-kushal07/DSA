"""
Question:
Write a Python function to find the highest common factor (HCF) or greatest common divisor (GCD) of two given non-negative integers. The function should take two integers
a and b as input and return their HCF or GCD.
"""
"""
Input:
12 15
Output:
3
"""

def hcf(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1

num1, num2, *_ = [int(item) for item in input("Enter the numbers: ").split()]
print(f"HCF of numbers {num1}, {num2} is: ", hcf(num1, num2))