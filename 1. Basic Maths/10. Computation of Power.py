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

def power(num1, num2):
	temp = 0
	if (num2 == 0):
		return 1
	temp = power(num1, int(num2 / 2))
	if (num2 % 2 == 0):
	    return temp * temp
	else:
	    return num1 * temp * temp

num1, num2, *_ = [int(item) for item in input("Enter the numbers: ").split()]
print(f"{num1} raised to power {num2} is: ", power(num1, num2))