"""
Question:
Write a Python function to reverse a list of numbers.
The task is to return a new list where the elements are in the reverse order.
"""
"""
Input:
A list of numbers (integers or floats).
Output:
A list of numbers in the reverse order.
"""

def reverse_list(numbers):
    start = 0
    end = len(numbers) - 1

    while s < e:
        numbers[start], numbers[end] = numbers[end], numbers[start]
        start = start + 1
        end = end - 1

    return numbers

numbers = [int(item) for item in input("Enter the numbers: ").split()]
print(f"Reversed list: {reverse_list(numbers)}")
