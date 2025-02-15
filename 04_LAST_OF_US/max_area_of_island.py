from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        visited = {}
        rows = len(grid)
        cols = len(grid[0])
        
        def maxAreaHelper(row, col) -> int:
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return -1
            
            if (row, col) in visited:
                return -2
            
            visited[(row, col)] = True
            
            if grid[row][col] == 0:
                return 0
            
            out = 0
            if grid[row][col] == 1:
                out += 1
            
            val = maxAreaHelper(row + 1, col)
            if val > 0:
                out += val
            val = maxAreaHelper(row - 1, col)
            if val > 0:
                out += val
            val = maxAreaHelper(row, col + 1)
            if val > 0:
                out += val
            val = maxAreaHelper(row, col - 1)
            if val > 0:
                out += val

            return out

        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    max_area = max(max_area, maxAreaHelper(row, col))
        return max_area
