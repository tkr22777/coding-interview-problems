# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/description/

from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # keeping min_diff since it can be negative which can produce 
        # do we need to keep min_diff since, all nums are positive and thus
        # negatives will never amount to a max_res

        max_i = nums[0]
        max_diff = max_i - nums[1]
        max_res = max_diff * nums[2]

        for j in range(2, len(nums) - 1):
            max_i = max(max_i, nums[j - 1])
            max_diff = max(max_diff, max_i - nums[j])
            max_res = max(max_res, max_diff * nums[j + 1])
            # print(f"i: {j - 1}, nums[i]: {nums[j - 1]}, max_i: {max_i}, max_diff: {max_diff}, j: {j}, nums[j]: {nums[j]}, max_res:{max_res} ")

        if max_res < 0:
            return 0

        return int(max_res)


s = Solution()
print(s.maximumTripletValue([12, 6, 1, 2, 7]) == 77)
print(s.maximumTripletValue([1, 10, 3, 4, 19]) == 133)
print(s.maximumTripletValue([1, 2, 3]) == 0) 