"""
Question:
Write a Python function to compute the union of two sorted arrays.
The union should contain unique elements in sorted order.
"""
"""
Input:
Two sorted lists of integers.
Output:
A single sorted list containing the union of both arrays.
"""

def union_sorted_arrays(arr1, arr2):
    i, j = 0, 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            if not result or result[-1] != arr2[j]:
                result.append(arr2[j])
            j += 1
        else:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1

    while i < len(arr1):
        if not result or result[-1] != arr1[i]:
            result.append(arr1[i])
        i += 1
    while j < len(arr2):
        if not result or result[-1] != arr2[j]:
            result.append(arr2[j])
        j += 1

    return result

arr1 = list(map(int, input("Enter the first sorted array: ").split()))
arr2 = list(map(int, input("Enter the second sorted array: ").split()))
print("Union of arrays:", union_sorted_arrays(arr1, arr2))

"""
Complexity:
    Best Case: O(n + m)   (n and m are lengths of the arrays)
    Average Case: O(n + m)
    Worst Case: O(n + m)
    Space Complexity: O(n + m) (Result array)
"""
