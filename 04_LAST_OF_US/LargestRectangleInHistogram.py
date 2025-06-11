"""
Largest Rectangle in Histogram

Problem Statement:
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.

Examples:
- Input: heights = [2,1,5,6,2,3]
  Output: 10
  Explanation: The largest rectangle has an area of 10 units, formed by the bars at indices 2, 3 
  (height = 5, width = 2).

- Input: heights = [2,4]
  Output: 4
  Explanation: The largest rectangle has an area of 4 units, formed by either both bars 
  (height = 2, width = 2) or just the second bar (height = 4, width = 1).

Constraints:
- 1 <= heights.length <= 10^5
- 0 <= heights[i] <= 10^4
"""

from typing import List

def largest_rectangle_area(heights: List[int]) -> int:
    """
    Calculate the area of the largest rectangle in the histogram.
    
    Args:
        heights: Array of integers representing histogram bar heights
        
    Returns:
        The area of the largest rectangle
    
    Approach hints:
    - Consider using a monotonic stack to efficiently find the boundaries of each rectangle
    - For each bar, we need to find how far left and right it can extend
    - The area for each bar is its height multiplied by its width (right boundary - left boundary + 1)
    - Consider using sentinel values to simplify the algorithm
    """
    # TODO: Implement your solution here
    pass


# Test cases
def test_largest_rectangle_area():
    test_cases = [
        {"heights": [2,1,5,6,2,3], "expected": 10},
        {"heights": [2,4], "expected": 4},
        {"heights": [1,1], "expected": 2},
        {"heights": [1,2,3,4,5], "expected": 9},
        {"heights": [5,4,3,2,1], "expected": 9},
        {"heights": [4,2,0,3,2,5], "expected": 6}
    ]
    
    for i, test_case in enumerate(test_cases):
        heights = test_case["heights"]
        expected = test_case["expected"]
        result = largest_rectangle_area(heights)
        status = "PASSED" if result == expected else f"FAILED (got {result}, expected {expected})"
        print(f"Test case {i+1}: {status}")


if __name__ == "__main__":
    # Uncomment the line below to run tests when you're ready
    # test_largest_rectangle_area()
    
    # Example usage
    heights = [2,1,5,6,2,3]
    print(f"Largest rectangle area: {largest_rectangle_area(heights)}") 