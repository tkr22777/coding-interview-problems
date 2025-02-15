from typing import List

# https://leetcode.com/problems/find-peak-element/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if m - 1 < 0 and nums[m] > nums[m + 1]:
                return m
            elif m - 1 >= 0 and nums[m - 1] < nums[m] and nums[m] > nums[m + 1]:
                return m
            elif nums[m] < nums[m + 1]:
                l = m + 1
            else:
                r = m - 1
        return l


s = Solution()
print(s.findPeakElement([1,2,3,1]))
print(s.findPeakElement([1,2,1,3,5,6,4]))
