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

def lcm(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0

    largest = max(num1, num2)

    while True:
        if largest % num1 == 0 and largest % num2 == 0:
            return largest
        largest += 1

num1, num2, *_ = [int(item) for item in input("Enter the numbers: ").split()]
print(f"HCF of numbers {num1}, {num2} is: ", lcm(num1, num2))