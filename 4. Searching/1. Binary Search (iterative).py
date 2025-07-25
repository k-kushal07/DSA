"""
Question:
Write a Python function to perform binary search on a sorted list using an iterative approach.
The function should return the index of the target element if found, otherwise -1.
"""
"""
Input:
A sorted list of integers and a target integer.
Output:
The index of the target if found, otherwise -1.
"""

def binary_search_iterative(arr, target):
    """
    Perform binary search iteratively.

    Parameters:
    arr (list): Sorted list of integers.
    target (int): The element to search for.

    Returns:
    int: Index of target if found, else -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        
        mid = (low + high) // 2  # Find the middle index
        print(low, high, mid)
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return -1  # Target not found

arr = list(map(int, input("Enter a sorted list of numbers (space-separated): ").split()))
target = int(input("Enter the number to search: "))

result = binary_search_iterative(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
