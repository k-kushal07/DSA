"""
Question:
Write a Python function to compute the intersection of two sorted arrays.
The intersection should contain only unique elements present in both arrays.
"""
"""
Input:
Two sorted lists of integers.
Output:
A sorted list containing the intersection of both arrays.
"""

def intersection_sorted_arrays(arr1, arr2):
    i, j = 0, 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i += 1
            j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1

    return result

arr1 = list(map(int, input("Enter the first sorted array: ").split()))
arr2 = list(map(int, input("Enter the second sorted array: ").split()))
print("Intersection of arrays:", intersection_sorted_arrays(arr1, arr2))

"""
Complexity:
    Best Case: O(n + m)   (n and m are lengths of the arrays)
    Average Case: O(n + m)
    Worst Case: O(n + m)
    Space Complexity: O(min(n, m)) (Result array)
"""
