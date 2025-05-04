"""
Maximum Triplet Value
Find the maximum value of (nums[i] - nums[j]) * nums[k] where i < j < k.
Return 0 if no valid triplet exists or if the maximum value is negative.
Example: [12,6,1,2,7] -> 77 (using i=0, j=2, k=4: (12-1)*7 = 77)

Time Complexity: O(n) where n is the length of the array
Space Complexity: O(1) - using only constant extra space
"""

from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        """
        Calculate the maximum value of (nums[i] - nums[j]) * nums[k] for valid triplets.
        
        Args:
            nums: List of integers
            
        Returns:
            Maximum value of (nums[i] - nums[j]) * nums[k] where i < j < k, or 0 if no positive value exists
        """
        # Handle case with fewer than 3 elements
        if len(nums) < 3:
            return 0
            
        # Initialize values for the first possible triplet
        max_i = nums[0]                 # Max value encountered at position i
        max_diff = max_i - nums[1]      # Max difference (nums[i] - nums[j])
        max_res = max_diff * nums[2]    # Initial triplet value
        
        # Process remaining elements
        for j in range(2, len(nums) - 1):
            # Update max value seen at position i
            max_i = max(max_i, nums[j - 1])
            
            # Update max difference between any nums[i] and current nums[j]
            max_diff = max(max_diff, max_i - nums[j])
            
            # Calculate triplet value and update max result
            max_res = max(max_res, max_diff * nums[j + 1])
        
        # Return 0 if no positive value exists
        return max(max_res, 0)


def test_maximum_triplet_value():
    """Test the maximumTripletValue function with various test cases."""
    solution = Solution()
    
    # Test case 1: Basic case
    assert solution.maximumTripletValue([12, 6, 1, 2, 7]) == 77, "Failed test case 1: should return 77"
    
    # Test case 2: Another example
    assert solution.maximumTripletValue([1, 10, 3, 4, 19]) == 133, "Failed test case 2: should return 133"
    
    # Test case 3: Minimum elements, no valid triplet
    assert solution.maximumTripletValue([1, 2, 3]) == 0, "Failed test case 3: should return 0"
    
    # Test case 4: Small positive result
    assert solution.maximumTripletValue([10, 5, 1]) == 5, "Failed test case 4: should return 5 for (10-5)*1"
    
    # Test case 5: Truly negative result
    assert solution.maximumTripletValue([1, 10, 3]) == 0, "Failed test case 5: should return 0 for negative result"
    
    # Test case 6: Fewer than 3 elements
    assert solution.maximumTripletValue([1, 2]) == 0, "Failed test case 6: should return 0 for array with < 3 elements"
    
    print("All maximum triplet value tests passed!")


if __name__ == "__main__":
    test_maximum_triplet_value() 