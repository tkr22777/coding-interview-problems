from typing import List

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        total = 0
        while i < j:
            total += int(str(nums[i]) + str(nums[j]))
            i += 1
            j -= 1
        if i == j:
            total += nums[i]
        return total

# Test cases
s = Solution()
print(s.findTheArrayConcVal([7,52,2,4]) == 596)
print(s.findTheArrayConcVal([5,14,13,8,12]) == 673) 