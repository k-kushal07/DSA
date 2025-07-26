"""
Question:
Write a Python function to sort a list using the Merge Sort algorithm.
Merge Sort divides the array into halves, recursively sorts them, and merges them back.
"""
"""
Input:
A list of integers.
Output:
The sorted list in ascending order.
"""

def merge(arr, left, mid, right):
    left_part = arr[left:mid+1]
    right_part = arr[mid+1:right+1]

    i, j, k = 0, 0, left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)


arr = list(map(int, input("Enter the list of numbers (space-separated): ").split()))
merge_sort(arr, 0, len(arr) - 1)
print("Sorted list:", arr)

"""
Complexity:
    Best Case: O(n log n)      (Always divides array into halves)
    Average Case: O(n log n)
    Worst Case: O(n log n)
    Space Complexity: O(n)     (Temporary arrays for merging)
    Stable: Yes
"""
