"""
Max Area of Island
Find the maximum area of an island in a grid.
An island is a group of connected 1's (representing land) in the grid.
Connections can only be horizontal or vertical, not diagonal.
Example: [[0,1,1],[1,1,0]] has a max area of 4.

Time Complexity: O(R*C) where R = rows, C = columns
Space Complexity: O(R*C) for the visited set and recursion stack
"""

from typing import List, Dict, Tuple, Set

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Find the maximum area of any island in the grid.
        """
        if not grid or not grid[0]:
            return 0
            
        visited: Set[Tuple[int, int]] = set()
        rows, cols = len(grid), len(grid[0])

        def explore_island(row: int, col: int) -> int:
            """Calculate area of an island starting at position (row, col)."""
            # Check boundary conditions
            if (row < 0 or row >= rows or 
                col < 0 or col >= cols or 
                grid[row][col] == 0 or 
                (row, col) in visited):
                return 0

            # Mark as visited
            visited.add((row, col))
            
            # Current cell contributes 1 to the area
            area = 1
            
            # Explore all four directions
            area += explore_island(row + 1, col)  # Down
            area += explore_island(row - 1, col)  # Up
            area += explore_island(row, col + 1)  # Right
            area += explore_island(row, col - 1)  # Left
            
            return area

        # Check each cell in the grid
        max_area = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    max_area = max(max_area, explore_island(row, col))
                    
        return max_area


def test_max_area_of_island():
    """Test the maxAreaOfIsland function with various test cases."""
    solution = Solution()
    
    # Test case 1: No islands
    grid1 = [[0, 0, 0, 0, 0, 0, 0, 0]]
    assert solution.maxAreaOfIsland(grid1) == 0, "Test case 1 failed: should return 0 for grid with no islands"
    
    # Test case 2: Complex grid with multiple islands
    grid2 = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    ]
    assert solution.maxAreaOfIsland(grid2) == 6, "Test case 2 failed: should return 6 for the largest island"
    
    # Test case 3: Single cell island
    grid3 = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert solution.maxAreaOfIsland(grid3) == 1, "Test case 3 failed: should return 1 for a single cell island"
    
    # Test case 4: Full grid island
    grid4 = [
        [1, 1],
        [1, 1]
    ]
    assert solution.maxAreaOfIsland(grid4) == 4, "Test case 4 failed: should return 4 for a full grid island"
    
    print("All max area of island tests passed!")


if __name__ == "__main__":
    test_max_area_of_island()