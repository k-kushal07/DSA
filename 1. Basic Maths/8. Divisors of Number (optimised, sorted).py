"""
Question:
Write a Python function to find all the divisors of a given non-negative integer. The function should take an integer 
n as input and return a list of all its divisors.
"""
"""
Input:
100
Output:
1 2 4 5 10 20 25 50 100
"""


def get_divisors(num):
    small_divisors = []
    large_divisors = []
    i = 1
    while i*i < num:
        if not num % i:
            small_divisors.append(i)
            if i*i != num:
                large_divisors.append(num/i)
    return small_divisors + large_divisors[::-1]

inp = int(input("Enter a number: "))
print(f"Divisors of number {inp} are: ", get_divisors(inp))