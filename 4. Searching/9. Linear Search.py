"""
Question:
Write a Python function to perform linear search on a list.
The function should return the index of the target element if found, otherwise -1.
"""
"""
Input:
A list of integers and a target integer.
Output:
The index of the target if found, otherwise -1.
"""

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = list(map(int, input("Enter the list of numbers (space-separated): ").split()))
target = int(input("Enter the number to search: "))

index = linear_search(arr, target)
if index != -1:
    print(f"Element {target} found at index {index}")
else:
    print(f"Element {target} not found in the list")
