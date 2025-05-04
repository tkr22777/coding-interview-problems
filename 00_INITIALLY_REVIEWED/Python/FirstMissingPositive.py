"""
First Missing Positive
Find the smallest positive integer that does not exist in the array.
Example: [1,2,0] -> 3, [3,4,-1,1] -> 2, [7,8,9,11,12] -> 1
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        numMap = {}

        if len(nums) == 0:
            return 1

        for num in nums:
            if num <= len(nums) and num > 0:
                numMap[num] = True

        # The first missing positive must be from 1 to N + 1
        for i in range(1, len(nums) + 2):
            if i not in numMap: 
                return i


def test_first_missing_positive():
    s = Solution()
    
    test_cases = [
        ([1, 2, 0], 3),           # Missing 3
        ([3, 4, -1, 1], 2),       # Missing 2
        ([7, 8, 9, 11, 12], 1),   # Missing 1
        ([], 1),                  # Empty array
        ([1], 2),                 # Just one element
        ([1, 1], 2),              # Duplicates
        ([-1, -2], 1)             # All negative
    ]
    
    for nums, expected in test_cases:
        assert s.firstMissingPositive(nums) == expected, f"For {nums}: expected {expected}"
    print("All tests passed!")

if __name__ == "__main__":
    test_first_missing_positive()
