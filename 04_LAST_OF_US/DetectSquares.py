from typing import List
from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.grid = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        x, y = point[0], point[1]
        self.grid[x][y] += 1

    def count(self, point: List[int]) -> int:
        # for x in self.grid.keys():
        #     for y in self.grid[x].keys():
        #         print("i: " + str(x) + "\t y:" + str(y) + "\t v:" + str(self.grid[x][y]))
        # print("point: " + str(point))

        x0, y0 = point[0], point[1]
        s_count = 0
        for y1, p_count in self.grid[x0].items():
            # print("y1: " + str(y1))

            d = y1 - y0
            # print("dist: " + str(d))
            if d == 0:
                continue

            x2p = x0 + d
            p2ps = self.grid[x2p][y0]
            p3ps = self.grid[x2p][y1]
            s_count += p_count * p2ps * p3ps

            x2n = x0 - d
            p2ns = self.grid[x2n][y0]
            p3ns = self.grid[x2n][y1]
            s_count += p_count * p2ns * p3ns
            # self.grid[x1][]

        return s_count

# x
# 3 -> (3, 10), (3, 2)
# 11 -> (11, 2)

# y
# 10 -> (3, 10)
# 2 -> (11, 2), (3, 2)


# for: point p1 -> (11, 10)
# 1. I want to find out the points p1x, in p1[0]
# 2. For each p1xi in p1x, find out if point
# p1xi[1] p1[1] on either side of the query point exist?
# two equi distance points?
#

detectSquares = DetectSquares()
detectSquares.add([3, 10])
detectSquares.add([11, 2])
detectSquares.add([3, 2])

# return 1. You can choose  - The first, second, and third
print(1 == detectSquares.count([11, 10]))

# return 0. The query point cannot form a square with any points in the data structure.
print(0 == detectSquares.count([14, 8]))

# Adding duplicate points is allowed.
detectSquares.add([11, 2])

#   - The first, second, and third
#   - The first, third, and fourth points
# return 2. You can choose:
print(2 == detectSquares.count([11, 10]))
