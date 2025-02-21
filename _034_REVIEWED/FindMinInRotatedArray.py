from typing import List

# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize pointers
        start = 0
        end = len(nums) - 1
        
        while start < end:
            mid = (start + end) // 2
            
            # If we're down to two elements
            if mid == start:
                # If the left element is greater than right, minimum is on the right
                return nums[end] if nums[start] > nums[end] else nums[start]
            
            # If left portion is sorted (increasing)
            if nums[start] < nums[mid]:
                # If right portion is also increasing and lower than left portion
                # minimum must be at start
                if nums[mid] < nums[end]:
                    return nums[start]
                # Otherwise, minimum is in right portion
                start = mid + 1
            # If left portion is not sorted, minimum must be in left portion
            else:
                end = mid
        
        return nums[start]


s = Solution()
print(s.findMin([3, 4, 5, 1, 2]) == 1)
print(s.findMin([4, 5, 6, 7, 0, 1, 2]) == 0)
print(s.findMin([11, 13, 15, 17]) == 11)
print(s.findMin([2, 1]) == 1)
print(s.findMin([3, 1, 2]) == 1)
print(s.findMin([5, 1, 2, 3, 4]) == 1) 