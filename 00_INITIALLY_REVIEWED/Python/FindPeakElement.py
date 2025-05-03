from typing import List

"""
Find any peak element in an array (element greater than its neighbors).
Array bounds are considered -∞, so edges can be peaks too.
"""

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        # Binary search for peak
        while left < right:
            mid = (left + right) // 2
            
            # If ascending, peak is to the right
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            # If descending, peak is at mid or to the left
            else:
                right = mid
            
        # When left == right, we've found a peak
        return left


def test_find_peak():
    solution = Solution()
    test_cases = [
        ([1, 2, 3, 1], 2),         # Peak in middle
        ([1, 2, 1, 3, 5, 6, 4], 5), # Multiple peaks
        ([1], 0),                   # Single element
        ([2, 1], 0),                # Peak at start
        ([1, 2], 1),                # Peak at end
    ]
    
    for nums, expected in test_cases:
        result = solution.findPeakElement(nums)
        # Check value rather than index (multiple valid peak indices may exist)
        assert nums[result] == nums[expected], f"Test failed for {nums}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_find_peak()
