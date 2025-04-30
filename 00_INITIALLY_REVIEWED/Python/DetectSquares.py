from typing import List, Dict, DefaultDict
from collections import defaultdict

# https://leetcode.com/problems/detect-squares/
# 
# Problem Summary:
# This problem involves implementing a class called DetectSquares with the following methods:
#   - init(): Initializes the data structure with empty points set.
#   - add(point): Adds a new point (x,y) to the data structure.
#   - count(point): Given a query point (x,y), finds the number of squares that can be formed
#     with this point as one corner, and the other three corners being points previously added
#     to the data structure.
#
# Rules for valid squares:
#   1. All four corners must be previously added points in the data structure.
#   2. The shape must be a perfect square (equal sides and right angles).
#   3. A point can be added multiple times and should be counted multiple times.
#   4. Squares can be at any angle, but sides must be parallel to the x and y axes.
#
# The solution uses a nested dictionary to efficiently track point frequencies and
# calculates potential squares by finding matching points at appropriate coordinates.

class DetectSquares:

    def __init__(self):
        self.points: DefaultDict[int, Dict[int, int]] = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        x, y = point
        self.points[x][y] += 1

    def count(self, point: List[int]) -> int:
        # Coordinate system explanation:
        #
        # y ^
        #   |
        # y2 +     +-------------+-------------+  (x3, y2)
        #   |     |             |             |
        #   |     |             |             |
        #   |     |             |             |
        #   |     |             |             |
        # y1 +     +-------------+-------------+  (x3, y1)
        #   |     ↑             ↑
        #   |     |             |
        #   |     |             |
        #   +-----+-------------+-------------+--> x
        #         |             |             |
        #        x4             x1            x3
        #
        # - (x1,y1) is the query point we're checking (point)
        # - (x1,y2) is a point with the same x-coordinate but different y-coordinate
        # - side_length = |y2 - y1| is the side length of the potential square
        # - x3 = x1 + side_length is the x-coordinate to the right
        # - x4 = x1 - side_length is the x-coordinate to the left
        
        square_count = 0
        x1, y1 = point
        
        # Early return if no points exist at the query point's x-coordinate
        if x1 not in self.points:
            return 0
            
        # Iterate over all points that share the same x-coordinate as the query point
        for y2, count1 in self.points[x1].items():
            if y1 == y2:  # Skip if same point (can't form a square)
                continue

            side_length = abs(y2 - y1)  # This is the square's side length
            
            # Check for squares to the right of the query point
            x3 = x1 + side_length
            if x3 in self.points:
                count2 = self.points[x3].get(y1, 0)  # Points at (x3, y1)
                count3 = self.points[x3].get(y2, 0)  # Points at (x3, y2)
                # Multiply all point counts to get the number of unique squares
                square_count += count1 * count2 * count3

            # Check for squares to the left of the query point
            x4 = x1 - side_length
            if x4 in self.points:
                count2 = self.points[x4].get(y1, 0)  # Points at (x4, y1)
                count3 = self.points[x4].get(y2, 0)  # Points at (x4, y2)
                # Multiply all point counts to get the number of unique squares
                square_count += count1 * count2 * count3

        return square_count


# Test cases
def run_tests():
    """Run test cases to verify the DetectSquares implementation."""
    print("Running tests...")
    
    # Test case 1: Basic square detection
    ds1 = DetectSquares()
    ds1.add([3, 10])
    ds1.add([11, 2])
    ds1.add([3, 2])
    result1 = ds1.count([11, 10])
    print(f"Test 1: {result1 == 1}, Expected: 1, Got: {result1}")
    
    # Test case 2: No square possible
    result2 = ds1.count([14, 8])
    print(f"Test 2: {result2 == 0}, Expected: 0, Got: {result2}")
    
    # Test case 3: Multiple points at same location
    ds1.add([11, 2])  # Add duplicate point
    result3 = ds1.count([11, 10])
    print(f"Test 3: {result3 == 2}, Expected: 2, Got: {result3}")
    
    # Test case 4: Custom test - square in opposite direction
    ds2 = DetectSquares()
    ds2.add([0, 0])
    ds2.add([0, 1])
    ds2.add([1, 0])
    ds2.add([1, 1])
    result4 = ds2.count([0, 0])
    print(f"Test 4: {result4 == 1}, Expected: 1, Got: {result4}")
    
    # Test case 5: Multiple squares from same point
    ds3 = DetectSquares()
    ds3.add([0, 0])
    ds3.add([0, 3])
    ds3.add([3, 0])
    ds3.add([3, 3])
    ds3.add([0, 5])
    ds3.add([5, 0])
    ds3.add([5, 5])
    result5 = ds3.count([0, 0])
    print(f"Test 5: {result5 == 2}, Expected: 2, Got: {result5}")


if __name__ == "__main__":
    run_tests()
