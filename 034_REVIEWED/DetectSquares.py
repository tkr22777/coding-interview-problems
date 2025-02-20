from typing import List
from collections import defaultdict

# https://leetcode.com/problems/detect-squares/

class DetectSquares:

    def __init__(self):
        self.grid = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        x, y = point[0], point[1]
        self.grid[x][y] += 1

    def count(self, point: List[int]) -> int:
        # Coordinate system explanation:
        #
        # y ^
        #   |
        # y_at_x  +-------------+  (x_ahead, y_at_x)
        #   |     |             |
        #   |     |             |
        #   |     |             |
        #   |     |             |
        # y +     +-------------+  (x_ahead, y)
        #   |     ↑
        #   |     (x,y) = point
        #   |
        #   +-----+-------------+-------------> x
        #         x        x_ahead
        #         |
        #     x_behind
        #
        # - (x,y) is the query point we're checking
        # - y_at_x is another y-coordinate found at the same x as query point
        # - width = y_at_x - y is the height of the potential square
        # - x_ahead = x + width is the x-coordinate to the right
        # - x_behind = x - width is the x-coordinate to the left
        
        square_count = 0
        x, y = point[0], point[1]
        for y_at_x, point_count in self.grid[x].items():
            if y == y_at_x: # the same x and y is not a square
                continue

            width = y_at_x - y

            # squares above
            x_ahead = x + width
            p2ps = self.grid[x_ahead][y] # points at x_ahead, y
            p3ps = self.grid[x_ahead][y_at_x] # points at x_ahead, y_at_x
            square_count += point_count * p2ps * p3ps

            x_behind = x - width
            p2ns = self.grid[x_behind][y]
            p3ns = self.grid[x_behind][y_at_x]
            square_count += point_count * p2ns * p3ns

        return square_count

detectSquares = DetectSquares()
detectSquares.add([3, 10])
detectSquares.add([11, 2])
detectSquares.add([3, 2])
print(1 == detectSquares.count([11, 10]))
print(0 == detectSquares.count([14, 8]))
detectSquares.add([11, 2])
print(2 == detectSquares.count([11, 10]))
print(2 == detectSquares.count([11, 10]))
