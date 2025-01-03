"""
Question:
Write a Python function that computes the average of a list of numbers.
Given a list of numbers, the task is to find the average. 
Average is calculated by dividing the sum of elements by the number of elements.
"""
"""
Input:
A list of numbers (integers or floats).
Output:
A float representing the average of the numbers in the list.
"""

def calculate_average(numbers):
    if len(numbers) == 0:
        return 0.0
    
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    return average

numbers = [int(item) for item in input("Enter the numbers: ").split()]
print(f"Average of the numbers {numbers} is: ", calculate_average(numbers))