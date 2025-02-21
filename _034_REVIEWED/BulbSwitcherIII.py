from typing import List

# https://leetcode.com/problems/bulb-switcher-iii/
# There's a row of bulbs, each has a switch to turn on/off.
# This feels like a gotcha problem.

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_flip = 0
        elems = 0
        prefix_aligned = 0
        for flip in flips:
            max_flip = max(flip, max_flip)
            elems += 1
            if max_flip == elems:
                prefix_aligned += 1
        return prefix_aligned

# Test cases
s = Solution()
print(s.numTimesAllBlue([3, 2, 4, 1, 5]) == 2)
print(s.numTimesAllBlue([4, 1, 2, 3]) == 1)
print(s.numTimesAllBlue([2, 1, 3]) == 2)