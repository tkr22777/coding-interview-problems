"""
Longest Square Streak
Find length of longest "square streak" sequence in an array.
A square streak is a sequence [x, x², x⁴, x⁸, ...] where each element is the square of the previous.
Return the longest streak length, or -1 if no streak of length > 1 exists.
Example: [4,3,6,16,8,2] → 3 (streak is [2,4,16])
"""

from typing import List

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        if not nums:
            return -1
            
        # Create a set for O(1) lookup
        nums_set = set(nums)
        
        # Count occurrences of 1 (special case)
        count_of_ones = nums.count(1)
        
        # Calculate streak length iteratively for each number
        max_streak = 0
        for num in nums:
            # Special case: if num is 1, handle separately to avoid infinite loop
            if num == 1:
                # Only count as streak if there are at least 2 ones
                if count_of_ones >= 2:
                    max_streak = max(max_streak, 2)  # At most 2, since all subsequent values are 1
                continue
                
            current = num
            streak_length = 0
            
            # Follow the square streak iteratively
            while current in nums_set:
                streak_length += 1
                next_value = current * current
                
                # Check if we'll overflow or definitely won't find next value
                if next_value > 10**9:
                    break
                    
                current = next_value
            
            if streak_length > 1:  # Only count streaks of length > 1
                max_streak = max(max_streak, streak_length)
        
        return max_streak if max_streak > 0 else -1


def test_longest_square_streak():
    solution = Solution()
    
    test_cases = [
        ([4, 3, 6, 16, 8, 2], 3),         # Streak: [2,4,16]
        ([2, 3, 5, 6, 7], -1),            # No streaks of length > 1
        ([1, 4, 16, 256], 3),             # Longest possible streak from 4
        ([4, 8, 16], 2),                  # Streak: [4,16]
        ([1, 2, 4, 8, 16, 32], 3),        # Multiple possible streaks
        ([100], -1),                      # Single element
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 2), # Only short streaks
        ([1], -1),                        # Just 1 (not a streak)
        ([1, 1, 1], 2)                    # Multiple 1s (should count as streak of length 2)
    ]
    
    for nums, expected in test_cases:
        result = solution.longestSquareStreak(nums)
        assert result == expected, f"For {nums}: expected {expected}, got {result}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_longest_square_streak()