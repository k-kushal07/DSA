"""
Question:
Write a Python function to merge two sorted arrays into one sorted array.
"""
"""
Input:
Two sorted lists of integers.
Output:
A single merged sorted list.
"""

def merge_sorted_arrays(arr1, arr2):
    i, j = 0, 0
    merged = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged

arr1 = list(map(int, input("Enter the first sorted array (space-separated): ").split()))
arr2 = list(map(int, input("Enter the second sorted array (space-separated): ").split()))

print("Merged sorted array:", merge_sorted_arrays(arr1, arr2))

"""
Complexity:
    Best Case: O(n + m)     (n and m are lengths of the two arrays)
    Average Case: O(n + m)
    Worst Case: O(n + m)
    Space Complexity: O(n + m) (New merged array)
"""
