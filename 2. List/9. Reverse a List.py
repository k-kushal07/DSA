"""
Question:
Write a Python function to reverse a given list without using built-in functions like reverse() or slicing.
"""
"""
Input:
A list of numbers (integers or floats).
Output:
A list of numbers in reverse order.
"""

def reverse_list(numbers):
    n = len(numbers)
    for i in range(0, n//2):
        numbers[i], numbers[n-i-1] = numbers[n-i-1], numbers[i]
    return numbers

numbers = [int(item) for item in input("Enter the numbers: ").split()]
print(f"The reversed list is: {reverse_list(numbers)}")
