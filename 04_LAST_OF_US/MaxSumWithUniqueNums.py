from typing import List
from collections import defaultdict

class Solution7:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        max_sum = 0
        nums_in_window = defaultdict(int)

        current_sum = 0
        for i in range(k):
            current_sum += nums[i]
            nums_in_window[nums[i]] += 1

        unique_nums = len(nums_in_window.keys())
        if unique_nums >= m:
            max_sum = current_sum
        # print("map: " + str(nums_in_window))
        # print("unique_nums: " + str(unique_nums))
        # print("cs: " + str(current_sum) + " ms:" + str(max_sum))

        for i in range(1, len(nums) - k + 1):
            # print("i:" + str(i) + "k:" + str(i + k - 1) + " sum:" + str(current_sum))

            vk = nums[i + k - 1]
            vip = nums[i - 1]
            current_sum = current_sum + vk - vip
            nums_in_window[vk] += 1
            nums_in_window[vip] -= 1
            if nums_in_window[vip] == 0:
                del nums_in_window[vip]

            unique_nums = len(nums_in_window.keys())
            if unique_nums >= m and current_sum > max_sum:
                max_sum = current_sum

            # print("map: " + str(nums_in_window))
            # print("unique_nums: " + str(unique_nums))
            # print("cs: " + str(current_sum) + " ms:" + str(max_sum))

        return max_sum 