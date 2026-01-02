"""
Question:
Write a Python function to perform Quick Sort using Hoare's partition scheme.
Hoare's partition selects the first element as pivot and partitions the array so that:
- Elements <= pivot move to the left side
- Elements >= pivot move to the right side
The pivot may not end up in its final sorted position after each partition.
"""
"""
Input:
A list of integers.
Output:
The sorted list (in-place sorting).
"""

# Hoare Partition Function
def hoare_partition(arr, low, high):
    pivot = arr[low]  # Choose first element as pivot
    i = low - 1
    j = high + 1

    while True:
        # Move i to the right until arr[i] >= pivot
        i += 1
        while arr[i] < pivot:
            i += 1

        # Move j to the left until arr[j] <= pivot
        j -= 1
        while arr[j] > pivot:
            j -= 1

        # If pointers cross, return the index j
        if i >= j:
            return j

        # Swap elements on the wrong side
        arr[i], arr[j] = arr[j], arr[i]


# Quick Sort using Hoare's partition
def quick_sort(arr, low, high):
    if low < high:
        p = hoare_partition(arr, low, high)  # Partition index
        quick_sort(arr, low, p)              # Sort left side
        quick_sort(arr, p + 1, high)         # Sort right side


# Input
arr = list(map(int, input("Enter the array: ").split()))
quick_sort(arr, 0, len(arr) - 1)

# Output
print("Sorted array:", arr)

"""
Time Complexity:
Best Case: O(n log n)    (Balanced partitions)
Average Case: O(n log n)
Worst Case: O(n^2)       (Already sorted or bad pivot choice)

Space Complexity: O(log n) recursive stack

Note:
Hoare's partition is usually faster than Lomuto because it performs fewer swaps.
"""
