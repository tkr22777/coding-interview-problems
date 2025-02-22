# https://leetcode.com/problems/max-area-of-island/
from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        visited = {}
        rows = len(grid)
        cols = len(grid[0])

        def maxAreaHelper(row, col) -> int:
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0

            if grid[row][col] == 0:
                return 0

            if (row, col) in visited:
                return 0
            visited[(row, col)] = True

            out = 1 # since it is not 0, it is 1
            out += maxAreaHelper(row + 1, col)
            out += maxAreaHelper(row - 1, col)
            out += maxAreaHelper(row, col + 1)
            out += maxAreaHelper(row, col - 1)
            return out

        max_area = 0
        for row in range(rows):
            for col in range(cols):
                max_area = max(max_area, maxAreaHelper(row, col))
        return max_area

print(Solution().maxAreaOfIsland([[0,0,0,0,0,0,0,0]])==0)
print(
    Solution().maxAreaOfIsland(
        [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ]
    )
    == 6
)