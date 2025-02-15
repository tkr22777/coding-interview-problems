from typing import List
from collections import defaultdict

class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                diagonals[i + j].append(nums[i][j])
                
        result = []
        curr_diagonal = 0
        
        while curr_diagonal in diagonals:
            result.extend(reversed(diagonals[curr_diagonal]))
            curr_diagonal += 1
            
        return result

# Test cases
s = Solution()
print(s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(s.findDiagonalOrder([[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]])) 