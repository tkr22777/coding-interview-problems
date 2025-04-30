# https://leetcode.com/problems/contiguous-array/
# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
# sort of a gotcha question

from typing import List

class Solution:

    def findMaxLength(self, nums: List[int]) -> int:
        # Balance starts at 0: +1 for 1s, -1 for 0s
        balance = 0
        max_length = 0
        # Store the first occurrence of each balance value
        # Initialize with balance 0 occurring at index -1
        balance_dict = {0: -1}
        
        for i in range(len(nums)):
            # Update balance: decrease for 0, increase for 1
            balance += -1 if nums[i] == 0 else 1
                
            if balance in balance_dict:
                # If we see this balance again, it means the elements between the current index
                # and the earliest index with this same balance must have equal 0s and 1s
                # (since they sum to zero change in balance)
                max_length = max(max_length, i - balance_dict[balance])
            else:
                # Record the first occurrence of this balance value's index
                balance_dict[balance] = i
                
        return max_length
    
s = Solution()
print(s.findMaxLength([0,1]) == 2)
print(s.findMaxLength([0,1,0]) == 2)
print(s.findMaxLength([0,0,1,0,0,0,1,1]) == 6)