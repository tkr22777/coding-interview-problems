from collections import defaultdict

class Solution(object):
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def streak(num_sq, num):
            if num in num_sq:
                return 1 + streak(num_sq, num_sq[num])    
            else:
                return 0        

        num_sq = {}

        for num in nums:
            num_sq[num] = num * num
        
        max_streak = 0
        for num in nums:
            nums_streak = streak(num_sq, num)
            if max_streak < nums_streak:
                max_streak = nums_streak


        if max_streak > 1:
            return max_streak

        return -1
