"""
Question:
Write a Python function to count the number of prime numbers less than a given integer.
"""
"""
Input:
10
Output:
4
"""

def count_primes(n):
    if n <= 2:
        return 0

    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    i = 2
    while i * i < n:
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
        i += 1

    return sum(is_prime)

inp = int(input("Enter a number: "))
print(f"Number of primes below {inp} are: ", count_primes(inp))
