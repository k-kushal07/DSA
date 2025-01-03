"""
Question:
Write a Python function to find the median of a list of numbers.
The median is the middle number when the list is sorted. 
If the list has an even number of elements, the median is the average of the two middle numbers.
"""
"""
Input:
A list of numbers (integers or floats).
Output:
A float representing the median of the numbers in the list.
"""

def find_median(numbers):
    numbers.sort()
    
    if len(numbers) % 2 == 1:
        return numbers[len(numbers) // 2]
    else:
        mid1 = numbers[len(numbers) // 2 - 1]
        mid2 = numbers[len(numbers) // 2]
        return (mid1 + mid2) / 2

numbers = [int(item) for item in input("Enter the numbers: ").split()]
print(f"Median of the numbers {numbers} is: ", find_median(numbers))