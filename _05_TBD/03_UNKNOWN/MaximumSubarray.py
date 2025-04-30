#!/usr/bin/python

class Solution(object):

    def maxSubArray(self, nums):

        """
        :type nums: List[int]
        :rtype: int
        """

        if nums is None:
            return None;

        length = len(nums)

        if (length < 1):
            return 0

        max_sum = nums[0]

        i = 0
        while i < length:

            j = i;

            while i == j or (temp_sum > 0 and j < length):
                if i == j:
                    temp_sum = nums[i]
                else:
                    temp_sum += nums[j]
                if temp_sum > max_sum:
                    max_sum = temp_sum
                j += 1

            i = j;

        return max_sum

    def sumInclusive(self, nums, i, j):

        sum = 0
        for k in range(i, j + 1):
            sum += nums[k]
        return sum


print Solution().maxSubArray([0, 1, 2, 3])
print Solution().maxSubArray([1])
print Solution().maxSubArray([])
print Solution().maxSubArray([5, 6, -1, 11])
print Solution().maxSubArray([5, 6, -12, 15])
