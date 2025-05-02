#!/usr/bin/python

"""
Question:
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

from collections import defaultdict

def twoSum(nums, target):
    differences = defaultdict(set)
    
    # First pass: Store indices for each potential complement
    for index, number in enumerate(nums):
        diff = target - number
        differences[diff].add(index)
    
    # Second pass: Check if any number's complement exists
    result = []
    for index, number in enumerate(nums):
        # Get all indices where this number appears as a complement
        other_indices = differences[number]
        for other_index in other_indices:
            # Avoid using the same element twice and prevent duplicates
            if index < other_index:
                result.append([index, other_index])
    
    return result

# Python 3 compatible print statements
print(twoSum([16, 2, 3], 20))
print(twoSum([16, 2, 3, 4], 20))
