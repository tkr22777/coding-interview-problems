# https://leetcode.com/problems/longest-square-streak-in-an-array/
# feels like a gotcha question

from typing import List

class Solution:
    def __init__(self):
        self.nums_set = set()

    def streak(self, num: int) -> int:
        if num in self.nums_set:
            return 1 + self.streak(num * num)
        else:
            return 0

    def longestSquareStreak(self, nums: List[int]) -> int:
        # reset for each call
        self.nums_set = set()

        for num in nums:
            self.nums_set.add(num)

        max_streak = 0
        for num in nums:
            nums_streak = self.streak(num)
            if nums_streak > max_streak:
                max_streak = nums_streak

        if max_streak > 1:
            return max_streak

        return -1

print(Solution().longestSquareStreak([4,3,6,16,8,2])==3)
print(Solution().longestSquareStreak([2,3,5,6,7])==-1)