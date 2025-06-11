"""
Combination Sum II

Problem Statement:
Given a collection of candidate numbers (candidates) and a target number (target), find all unique 
combinations in candidates where the candidate numbers sum to target.
Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Examples:
- Input: candidates = [10,1,2,7,6,1,5], target = 8
  Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
  Explanation: These are all the ways to form combinations that sum to 8.

- Input: candidates = [2,5,2,1,2], target = 5
  Output: [[1,2,2],[5]]
  Explanation: We can use [1,2,2] or just [5] to form combinations that sum to 5.

Constraints:
- 1 <= candidates.length <= 100
- 1 <= candidates[i] <= 50
- 1 <= target <= 30
"""

from typing import List

def combination_sum_ii(candidates: List[int], target: int) -> List[List[int]]:
    """
    Find all unique combinations in candidates where the sum equals target.
    
    Args:
        candidates: Collection of candidate numbers
        target: Target sum
        
    Returns:
        List of all unique combinations that sum to target
    
    Approach hints:
    - Use backtracking to explore all combinations
    - Sort the candidates first to help handle duplicates
    - Skip duplicate elements at the same level of search to avoid duplicate combinations
    - Keep track of the current combination and remaining target during backtracking
    """
    # TODO: Implement your solution here

    candidates.sort()

    results = []
    backtrack(candidates, target, 0, [], results)
    return results


# # Helper function for backtracking
def backtrack(candidates: List[int], target: int, start: int, current_combination: List[int], results: List[List[int]]) -> None:
    pass
    


# Test cases
def test_combination_sum_ii():
    test_cases = [
        {
            "candidates": [10,1,2,7,6,1,5], 
            "target": 8, 
            "expected": [[1,1,6],[1,2,5],[1,7],[2,6]]
        },
        {
            "candidates": [2,5,2,1,2], 
            "target": 5, 
            "expected": [[1,2,2],[5]]
        },
        {
            "candidates": [2,3,6,7], 
            "target": 7, 
            "expected": [[7]]
        },
        {
            "candidates": [1,1,1,1,1,1,1,1,1,1], 
            "target": 5, 
            "expected": [[1,1,1,1,1]]
        },
        {
            "candidates": [1,2,3,4,5], 
            "target": 10, 
            "expected": [[1,2,3,4],[1,4,5],[2,3,5]]
        }
    ]
    
    for i, test_case in enumerate(test_cases):
        candidates = test_case["candidates"]
        target = test_case["target"]
        expected = sorted([sorted(combo) for combo in test_case["expected"]])
        result = combination_sum_ii(candidates, target)
        result_sorted = sorted([sorted(combo) for combo in result])
        status = "PASSED" if result_sorted == expected else f"FAILED (got {result_sorted}, expected {expected})"
        print(f"Test case {i+1}: {status}")


if __name__ == "__main__":
    # Uncomment the line below to run tests when you're ready
    # test_combination_sum_ii()
    
    # Example usage
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print(f"Combinations that sum to {target}: {combination_sum_ii(candidates, target)}") 