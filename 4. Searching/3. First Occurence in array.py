"""
Question:
Write a Python function to find the index of the first occurrence of a given target in a sorted list using an iterative approach.
If the target is not present, return -1.
"""
"""
Input:
A sorted list of integers (can contain duplicates) and a target integer.
Output:
The index of the first occurrence of the target if found, otherwise -1.
"""

def first_occurrence_iterative(arr, target):
    low = 0
    high = len(arr) - 1
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            if arr[mid] == target && arr[mid-1] != arr[mid]:
                result = mid
                break
            else:
                high=mid-1
    return result

arr = list(map(int, input("Enter a sorted list of numbers (space-separated): ").split()))
target = int(input("Enter the number to search: "))

result = first_occurrence_iterative(arr, target)
if result != -1:
    print(f"The first occurrence of {target} is at index {result}")
else:
    print(f"Element {target} not found in the list")
