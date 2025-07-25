"""
Question:
Write a Python function to count the number of 1s in a sorted binary array using binary search.
"""
"""
Input:
A sorted binary list (only 0s and 1s).
Output:
An integer representing the count of 1s.
"""

def count_ones(arr):
    low = 0
    high = len(arr) - 1
    last_one_index = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == 1:
            last_one_index = mid
            low = mid + 1
        else:
            high = mid - 1

    return last_one_index+1

arr = list(map(int, input("Enter a sorted binary array (0s and 1s): ").split()))
print(f"Number of 1s in the array: {count_ones(arr)}")
