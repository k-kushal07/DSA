"""
Question:
Write a Python function to compute the power of a given number n raised to an integer exponent p,
denoted as n^p. The function should take two integers n and p as input and
return the result of n raised to the power p.
"""
"""
Input:
5 3
Output:
125
"""

def power(num, power):
    result = 1
    while power > 0:
        if power % 2 != 0:
            result = result * num
        num = num * num
        power = power // 2
    return result

num1, num2, *_ = [int(item) for item in input("Enter the numbers: ").split()]
print(f"{num1} raised to power {num2} is: ", power(num1, num2))