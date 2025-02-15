from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            # print(f"left: {left} right: {right} mid: {mid}")
            if mid == left:
                if nums[mid] > nums[right]:
                    left = right
                break
            else:
                if nums[left] < nums[mid]:
                    if nums[mid] < nums[right]:
                        break
                    else:
                        left = mid + 1
                else:
                    right = mid

        return nums[left]


s = Solution()
print(s.findMin([3, 4, 5, 1, 2]) == 1)
print(s.findMin([4, 5, 6, 7, 0, 1, 2]) == 0)
print(s.findMin([11, 13, 15, 17]) == 11)
print(s.findMin([2, 1]) == 1)
print(s.findMin([3, 1, 2]) == 1)
print(s.findMin([5, 1, 2, 3, 4]) == 1) 