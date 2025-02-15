from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_length = 0
        count_dict = {0: -1}
        
        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
                
            if count in count_dict:
                max_length = max(max_length, i - count_dict[count])
            else:
                count_dict[count] = i
                
        return max_length

# Test cases
s = Solution()
print(s.findMaxLength([0,1]) == 2)
print(s.findMaxLength([0,1,0]) == 2)
print(s.findMaxLength([0,0,1,0,0,0,1,1]) == 6) 