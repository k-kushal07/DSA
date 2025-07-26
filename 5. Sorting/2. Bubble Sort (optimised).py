"""
Question:
Write a Python function to sort a list using the Bubble Sort algorithm.
Bubble Sort repeatedly swaps adjacent elements if they are in the wrong order.
"""
"""
Input:
A list of integers.
Output:
The sorted list in ascending order.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            break
    return arr

arr = list(map(int, input("Enter the list of numbers (space-separated): ").split()))
print("Sorted list:", bubble_sort(arr))

"""
Complexity:
    Best Case: O(n)        (Already sorted list, no swaps needed)
    Average Case: O(n^2)   (Random order)
    Worst Case: O(n^2)     (Reverse sorted list)
    Space Complexity: O(1) (In-place sorting)
"""