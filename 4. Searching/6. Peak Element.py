"""
Question:
Write a Python function to find a peak element in a list using binary search.
A peak element is an element that is not smaller than its neighbors.
If multiple peaks exist, return the index of any one of them.
"""

def find_peak(arr):
    N = len(arr)
    if N == 1:
        return 0
    elif arr[N-1] > arr[N-2]:
        return N-1
    elif arr[0] > arr[1]:
        return 0

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
            return mid
        elif arr[mid] < arr[mid+1]:
                low = mid+1
        elif arr[mid] < arr[mid-1]:
            high = mid-1

    return -1

# Input
arr = list(map(int, input("Enter the list of numbers (space-separated): ").split()))

# Output
peak_index = find_peak(arr)
print(f"A peak element is {arr[peak_index]} at index {peak_index}")
