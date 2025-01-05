"""
Question:
Write a Python function to perform a left rotation on a list without using the pop function.
Left rotation shifts each element of the list to the left by one position, and the first element moves to the end.
"""
"""
Input:
A list of numbers (integers or floats) and an integer k (number of rotations).
Output:
A list of numbers after k left rotations.
"""

def left_rotate_list(numbers, k):
    # Handle cases where k > len(numbers)
    k %= len(numbers)
    for _ in range(k):
        first_element = numbers[0]
        for i in range(len(numbers) - 1):
            numbers[i] = numbers[i + 1]
        numbers[-1] = first_element
    return numbers

*numbers, k = [int(item) for item in input("Enter the numbers: ").split()]
print(f"List after {k} left rotations: {left_rotate_list(numbers, k)}")