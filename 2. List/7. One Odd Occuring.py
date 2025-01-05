"""
Question:
Given an array of positive integers, all numbers occur an even number of times except one number which occurs an odd number of times. 
Find the number in O(n) time and constant space.
"""
"""
Input:
A list of positive integers.
Output:
An integer that occurs an odd number of times.
"""

"""
XOR (^) has a few useful properties:
a^a = 0, Any number XORed with itself is 0.
a^0 = a, Any number XORed with 0 remains unchanged.

By XORing all the elements in the array:
The numbers that occur an even number of times cancel each other out (result in 0).
The number that occurs an odd number of times remains.
"""

def find_odd_occurrence(numbers):
    result = 0
    for num in numbers:
        result ^= num
    return result

numbers = [int(item) for item in input("Enter the numbers: ").split()]
print(f"The number that occurs an odd number of times is: {find_odd_occurrence(numbers)}")
