# https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/submissions/1261454295/
from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_i = nums[0]
        min_i = nums[0]
        min_diff = max_i - nums[1]
        max_diff = min_i - nums[1]
        max_res = max(max_diff * nums[2], min_diff * nums[2])
        for j in range(2, len(nums) - 1):
            max_i = max(max_i, nums[j - 1])
            min_i = min(min_i, nums[j - 1])

            max_diff = max(max_diff, max_i - nums[j])
            min_diff = min(min_diff, min_i - nums[j])

            max_res = max(max_res,
                          max(
                              max(max_diff, max_diff * nums[j + 1]),
                              max(min_diff, min_diff * nums[j + 1])
                          )
                          )

            # print(f"i: {j - 1}, max_i: {max_i}, min_i: {min_i}, max_diff: {max_diff}, j: {j}, min_diff: {min_diff}, k: {j+1}, max_res:{max_res} ")

        if max_res < 0:
            return 0
        return int(max_res)


s = Solution()
print(s.maximumTripletValue([12, 6, 1, 2, 7]))
print(s.maximumTripletValue([1, 10, 3, 4, 19]))
print(s.maximumTripletValue([1, 2, 3])) 