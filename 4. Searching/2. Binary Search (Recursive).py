"""
Question:
Write a Python function to perform binary search on a sorted list using recursion.
The function should return the index of the target element if found, otherwise -1.
"""
"""
Input:
A sorted list of integers and a target integer.
Output:
The index of the target if found, otherwise -1.
"""

def binary_search_recursive(arr, target):
    """
    Recursive binary search wrapper (simplified for user).
    """
    def helper(low, high):
        if low > high:
            return -1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return helper(mid + 1, high)
        else:
            return helper(low, mid - 1)
    return helper(0, len(arr) - 1)

arr = list(map(int, input("Enter a sorted list of numbers (space-separated): ").split()))
target = int(input("Enter the number to search: "))

result = binary_search_recursive(arr, target)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")
