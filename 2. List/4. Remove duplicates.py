"""
Question:
Write a Python function to remove duplicates from a list of numbers without using extra space.
The task is to modify the input list in place to contain only unique elements, maintaining their original order.
"""
"""
Input:
A list of numbers (integers or floats).
Output:
The modified list with duplicates removed, maintaining the original order.
"""

def remove_duplicates(numbers):
    i = 0
    while i < len(numbers):
        j = i + 1
        while j < len(numbers):
            if numbers[j] == numbers[i]:
                del numbers[j]
            else:
                j += 1
        i += 1
    return numbers

numbers = [int(item) for item in input("Enter the numbers: ").split()]
print(f"List after removing duplicates: {remove_duplicates(numbers)}")
