from typing import List

"""
Find minimum element in a rotated sorted array using binary search.

Key Insights:
1. A rotated sorted array has two sorted portions with a pivot point
   Example: [4,5,6,7,0,1,2] -> [4,5,6,7] and [0,1,2] with pivot at 0

2. Properties that help locate minimum:
   - Left portion: All elements > elements in right portion
   - Right portion: All elements < elements in left portion
   - Minimum element is at the start of right portion (pivot)

3. Binary Search Strategy:
   - If left half is sorted (nums[left] < nums[mid]):
     * If right half is also sorted and larger than left half, min is at left
     * Otherwise, min is in right half
   - If left half is not sorted:
     * Min must be in left half (including mid)

Time: O(log n), Space: O(1)
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """Find minimum using modified binary search."""
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # Base case: when narrowed down to two elements
            if mid == left:
                return min(nums[left], nums[right])
            
            # Case 1: Left half is sorted (increasing)
            if nums[left] < nums[mid]:
                # If right half is also sorted and larger than left half,
                # then array isn't rotated, minimum is at start
                if nums[mid] < nums[right]:
                    return nums[left]
                # Otherwise, minimum must be in right half
                # (where the rotation happened)
                left = mid + 1
            # Case 2: Left half is not sorted
            # This means the rotation point (minimum) is in left half
            else:
                # Include mid as it could be the minimum
                right = mid
        
        return nums[left]


def test_find_min():
    solution = Solution()
    test_cases = [
        ([3, 4, 5, 1, 2], 1),      # Basic rotation: [1,2,3,4,5] rotated by 2
        ([4, 5, 6, 7, 0, 1, 2], 0), # Multiple rotations: [0,1,2,4,5,6,7] rotated by 4
        ([2, 1], 1),               # Minimal case: two elements
        ([5, 1, 2, 3, 4], 1),      # Single rotation: [1,2,3,4,5] rotated by 1
        ([1, 2, 3, 4, 5], 1),      # Edge case: no rotation
    ]
    
    for nums, expected in test_cases:
        assert solution.findMin(nums) == expected
    
    print("All tests passed!")


if __name__ == "__main__":
    test_find_min() 