"""
Question:
Write a Python function to count the number of occurrences of a given target in a sorted list using binary search.
"""
"""
Input:
A sorted list of integers (can contain duplicates) and a target integer.
Output:
The count of occurrences of the target in the list.
"""

def first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            if arr[mid-1] != arr[mid] or mid == 0:
                return mid
            else:
                high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result

def last_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            if mid != len(arr) - 1 and arr[mid] == arr[mid+1]:
                low = mid + 1
            else:
                return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result

def count_occurrences(arr, target):
    first = first_occurrence(arr, target)
    if first == -1:
        return 0
    last = last_occurrence(arr, target)
    return last - first + 1

# Input
arr = list(map(int, input("Enter a sorted list of numbers (space-separated): ").split()))
target = int(input("Enter the number to count: "))

# Output
count = count_occurrences(arr, target)
print(f"The number {target} occurs {count} times in the list.")
