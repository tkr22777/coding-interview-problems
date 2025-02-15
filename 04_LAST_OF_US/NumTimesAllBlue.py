from typing import List

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        # nums:
        max_flip = 0
        elems = 0
        times = 0
        for flip in flips:
            max_flip = max(flip, max_flip)
            elems += 1
            if max_flip == elems:
                times += 1
        return times


s = Solution()
print(s.numTimesAllBlue([3, 2, 4, 1, 5]) == 2)
print(s.numTimesAllBlue([4, 1, 2, 3]) == 1)