"""
Question:
Write a Python function to perform a left rotation on a list.
Left rotation shifts each element of the list to the left by one position, and the first element moves to the end.
"""
"""
Input:
A list of numbers (integers or floats) and an integer k (number of rotations).
Output:
A list of numbers after k left rotations.
"""

def left_rotate_using_slice(numbers):
    return numbers[1:] + numbers[0:1]

def left_rotate_using_pop(numbers):
    numbers.append(numbers.pop(0))
    return numbers

def left_rotate(numbers):
    first = numbers[0]
    for i in range(1, len(numbers)):
        numbers[i-1] = numbers[i]
    numbers[len(numbers)-1] = first
    return numbers


numbers = [int(item) for item in input("Enter the numbers: ").split()]
print(f"List after a left rotation using slice: {left_rotate_using_slice(numbers)}")
print(f"List after a left rotation using pop: {left_rotate_using_pop(numbers)}")
print(f"List after a left rotation using pop: {left_rotate(numbers)}")