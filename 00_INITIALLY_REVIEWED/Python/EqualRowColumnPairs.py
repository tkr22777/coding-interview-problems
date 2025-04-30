"""
Given an n x n matrix, count pairs (r, c) where row r and column c are identical.
"""
from collections import defaultdict

# https://leetcode.com/problems/equal-row-and-column-pairs/

class Solution(object):
    def equalPairs(self, grid):
        n = len(grid)
        # Count occurrences of rows and columns with same values
        value_count = defaultdict(lambda: defaultdict(int))

        # Count rows
        for row in grid:
            value_count[tuple(row)]["rows"] += 1
        
        # Count columns
        for i in range(n):
            col = [grid[j][i] for j in range(n)]
            value_count[tuple(col)]["cols"] += 1

        # Calculate pairs
        total = 0
        for _, counts in value_count.items():
            if "rows" in counts and "cols" in counts:
                total += counts["rows"] * counts["cols"]

        return total


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        [
            [3, 2, 1],
            [1, 7, 6],
            [2, 7, 7]
        ],
        [
            [3, 1, 2, 2],
            [1, 4, 4, 5],
            [2, 4, 2, 2],
            [2, 4, 2, 2]
        ],
        [
            [11, 1],
            [1, 11]
        ],
        [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
    ]
    
    expected = [1, 3, 2, 9]
    
    for i, case in enumerate(test_cases):
        result = solution.equalPairs(case)
        print(f"Test {i+1}: {result == expected[i]}")