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

def twoSum(nums, target):

    differences = {}
    index = 0
    for number in nums:
        diff = target - number
        indices = differences.get(diff, set())
        indices.add(index)
        differences[diff] = indices
        index = index + 1

    index = 0
    toReturn = []
    for number in nums:
        if number in differences:
            otherIndices = differences[number]
            for otherIndex in otherIndices:
                if index < otherIndex: #using less than to only return 3, 4 instead of 3, 4 and 4, 3
                    toReturn.append([index, otherIndex])
        index = index + 1
    return toReturn

print twoSum([16, 2, 3], 20)
print twoSum([16, 2, 3, 4], 20)
