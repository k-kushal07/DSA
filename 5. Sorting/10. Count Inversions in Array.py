"""
    Question:
    Write a Python function to count inversions in an array.
    An inversion is a pair (i, j) such that i < j and arr[i] > arr[j].
    """
    """
    Input:
    A list of integers.
    Output:
    An integer representing the number of inversions.
"""

def merge_and_count(arr, left, mid, right):
    left_part = arr[left:mid+1]
    right_part = arr[mid+1:right+1]
    i, j, k = 0, 0, left
    inversions = 0

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            inversions += (len(left_part) - i)  # All remaining in left_part are inversions
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
    return inversions

def merge_sort_and_count(arr, left, right):
    if left >= right:
        return 0
    mid = (left + right) // 2
    inversions = 0
    inversions += merge_sort_and_count(arr, left, mid)
    inversions += merge_sort_and_count(arr, mid + 1, right)
    inversions += merge_and_count(arr, left, mid, right)
    return inversions

def count_inversions(arr):
    return merge_sort_and_count(arr, 0, len(arr) - 1)


arr = list(map(int, input("Enter the array: ").split()))
print("Number of inversions:", count_inversions(arr))

"""
Complexity:
    Best Case: O(n log n)
    Average Case: O(n log n)
    Worst Case: O(n log n)
    Space Complexity: O(n)
"""
