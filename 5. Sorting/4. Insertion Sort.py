"""
Question:
Write a Python function to sort a list using the Insertion Sort algorithm.
Insertion Sort builds the sorted list one element at a time by inserting each new element into its correct position.
"""
"""
Input:
A list of integers.
Output:
The sorted list in ascending order.
"""

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = list(map(int, input("Enter the list of numbers (space-separated): ").split()))
print("Sorted list:", insertion_sort(arr))

"""
Complexity:
    Best Case: O(n)        (Already sorted list — only 1 comparison per element)
    Average Case: O(n^2)   (Random order)
    Worst Case: O(n^2)     (Reverse sorted list)
    Space Complexity: O(1) (In-place sorting)
    Stable: Yes
"""
