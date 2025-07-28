"""
Question:
    Write a Python function to perform Lomuto partitioning.
    Lomuto partition chooses the last element as pivot and partitions the array so that:
    - All elements <= pivot are on the left.
    - All elements > pivot are on the right.
"""
"""
Input:
    A list of integers, and two integers: low (start index) and high (end index).
Output:
    The partition index where the pivot is placed.
"""

def lomuto_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot at correct position
    return i + 1  # Return pivot element index

arr = list(map(int, input("Enter the array: ").split()))
low, high = 0, len(arr) - 1
p = lomuto_partition(arr, low, high)
print("Array after partitioning:", arr)
print("Pivot index:", p)

"""
Complexity:
    Best Case: O(n)        (Single partition scan)
    Average Case: O(n)
    Worst Case: O(n)
    Space Complexity: O(1) (In-place partitioning)
"""
