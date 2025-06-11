"""
Trapping Rain Water

Problem Statement:
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

Examples:
- Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
  Output: 6
  Explanation: The elevation map is represented by the array [0,1,0,2,1,0,1,3,2,1,2,1]. 
  In this case, 6 units of rain water are being trapped.

- Input: height = [4,2,0,3,2,5]
  Output: 9
  Explanation: The elevation map is represented by the array [4,2,0,3,2,5].
  In this case, 9 units of rain water are being trapped.

Constraints:
- n == height.length
- 1 <= n <= 2 * 10^4
- 0 <= height[i] <= 10^5
"""

from typing import List

def trap(height: List[int]) -> int:
    """
    Calculate how much water can be trapped after raining.
    
    Args:
        height: A list of non-negative integers representing an elevation map
        
    Returns:
        The amount of water that can be trapped
    
    Approach hints:
    - You can use either a two-pointer approach or a stack-based solution
    - For each position, water trapped depends on the minimum of maximum heights to its left and right
    - Try to think about how to compute left_max and right_max efficiently
    """
    # TODO: Implement your solution here
    pass


# Test cases
def test_trap():
    test_cases = [
        {"height": [0,1,0,2,1,0,1,3,2,1,2,1], "expected": 6},
        {"height": [4,2,0,3,2,5], "expected": 9},
        {"height": [4,2,3], "expected": 1},
        {"height": [5,4,1,2], "expected": 1},
        {"height": [5,2,1,2,1,5], "expected": 14},
        {"height": [0,7,1,4,6], "expected": 7}
    ]
    
    for i, test_case in enumerate(test_cases):
        height = test_case["height"]
        expected = test_case["expected"]
        result = trap(height)
        status = "PASSED" if result == expected else f"FAILED (got {result}, expected {expected})"
        print(f"Test case {i+1}: {status}")


if __name__ == "__main__":
    # Uncomment the line below to run tests when you're ready
    # test_trap()
    
    # Example usage
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(f"Water trapped: {trap(height)}") 