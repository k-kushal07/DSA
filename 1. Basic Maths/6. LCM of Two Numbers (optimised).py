"""
Question:
Write a Python function to find the least common multiple (LCM) of two given non-negative integers. The function should take two integers
a and b as input and return their LCM.
"""
"""
Input:
5 15
Output:
15
"""

def hcf(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1

def lcm(num1, num2):
    return num1 * num2 // hcf(num1, num2)

num1, num2, *_ = [int(item) for item in input("Enter the numbers: ").split()]
print(f"HCF of numbers {num1}, {num2} is: ", lcm(num1, num2))