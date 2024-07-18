"""
Question:
Write a Python function to check whether a given integer is a prime number.
The function should take an integer n as input and return True if the number is prime, and False otherwise.
"""
"""
Input:
37
Output:
True
"""


def is_prime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    else:
        i = 5
        while i*i < num:
            if num % i == 0 or num % i+2 == 0:
                return False
            i += 6
        return True

inp = int(input("Enter a number: "))
print(f"Is the number {inp} a prime numer? ", is_prime(inp))