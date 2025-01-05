"""
Question:
Write a Python function to find the maximum and minimum values in a given list without using built-in functions like max() or min().
"""
"""
Input:
A list of numbers (integers or floats).
Output:
Two numbers: the maximum and minimum values in the list.
"""

def find_max_and_min(numbers):
    max_value = numbers[0]
    min_value = numbers[0]

    for num in numbers:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num

    return max_value, min_value

numbers = [int(item) for item in input("Enter the numbers: ").split()]
print(f"The max and min elements are: {*find_max_and_min(numbers)}")
