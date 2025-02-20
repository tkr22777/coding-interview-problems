from typing import List

# https://leetcode.com/problems/find-peak-element/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # Initialize left and right pointers for binary search
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # Case 1: First element is peak (no left neighbor)
            if mid == 0 and nums[mid] > nums[mid + 1]:
                return mid
            
            # Case 2: Middle element is peak
            elif mid > 0 and nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
                return mid
            
            # If right side is greater, peak must be on right side
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
            
            # If left side is greater, peak must be on left side
            else:
                right = mid - 1
            
        return left

s = Solution()
print(s.findPeakElement([1,2,3,1]) == 2)
print(s.findPeakElement([1,2,1,3,5,6,4]) == 5)
print(s.findPeakElement([1,2,3,4,5,6,7,6,5,4,3,2,1]) == 6)
