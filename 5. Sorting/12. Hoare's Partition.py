"""
Question:
    a Python function to perform Hoare's partitioning.
    Hoare’s partition chooses the first element as pivot and partitions the array so that:
    - All elements <= pivot are on the left side.
    - All elWriteements >= pivot are on the right side.
"""
"""
Input:
    A list of integers, and two integers: low (start index) and high (end index).
Output:
    The partition index (final position of pivot may not be exact).
"""

def hoare_partition(arr, low, high):
    pivot = arr[low]  # Choose first element as pivot
    i = low - 1
    j = high + 1
    while True:
        # Move i to the right until an element >= pivot is found
        i += 1
        while arr[i] < pivot:
            i += 1
        # Move j to the left until an element <= pivot is found
        j -= 1
        while arr[j] > pivot:
            j -= 1
        # If pointers cross, return partition index
        if i >= j:
            return j
        # Swap elements at i and j
        arr[i], arr[j] = arr[j], arr[i]

arr = list(map(int, input("Enter the array: ").split()))
low, high = 0, len(arr) - 1
p = hoare_partition(arr, low, high)
print("Array after partitioning:", arr)
print("Partition index:", p)

"""
Complexity:
    Best Case: O(n)        (Single pass)
    Average Case: O(n)
    Worst Case: O(n)
    Space Complexity: O(1) (In-place partitioning)
"""
