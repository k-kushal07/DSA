"""
Question:
Write a Python function to merge two sorted subarrays of a single array into one sorted section.
"""
"""
Input:
An array, and three integers: left, mid, right such that:
- The subarray arr[left:mid+1] is sorted.
- The subarray arr[mid+1:right+1] is sorted.
Output:
The array with the section arr[left:right+1] merged into sorted order.
"""

def merge_subarrays(arr, left, mid, right):
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

arr = list(map(int, input("Enter the array: ").split()))
left, mid, right = map(int, input("Enter left, mid, right indices: ").split())
merge_subarrays(arr, left, mid, right)
print("Array after merging subarrays:", arr)

"""
Complexity:
    Best Case: O(n)      (n = right - left + 1)
    Average Case: O(n)
    Worst Case: O(n)
    Space Complexity: O(n) (Temporary arrays for merging)
"""
