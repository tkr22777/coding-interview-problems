from typing import List

class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        min_val = nums[k]
        score = min_val * (k + 1)
        
        for i in range(k + 1, len(nums)):
            min_val = min(min_val, nums[i])
            score = max(score, min_val * (i + 1))
            
        return score

# Test cases
s = Solution()
print(s.maxScore([1,4,3,7,4,5], 3) == 15)
print(s.maxScore([5,5,4,5,4,1,1,1], 0) == 20) 