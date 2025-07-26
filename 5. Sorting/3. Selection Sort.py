"""
Question:
Write a Python function to sort a list using the Selection Sort algorithm.
Selection Sort repeatedly selects the smallest element from the unsorted part and places it at the beginning.
"""
"""
Input:
A list of integers.
Output:
The sorted list in ascending order.
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = list(map(int, input("Enter the list of numbers (space-separated): ").split()))
print("Sorted list:", selection_sort(arr))

"""
Complexity:
    Best Case: O(n^2)      (Even if already sorted, it still scans the rest of the list for min every time)
    Average Case: O(n^2)   (Random order)
    Worst Case: O(n^2)     (Reverse sorted list)
    Space Complexity: O(1) (In-place sorting)
    Stable: No
"""
