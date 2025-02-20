from collections import defaultdict

# https://leetcode.com/problems/equal-row-and-column-pairs/

class Solution(object):

    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        value_count = defaultdict(lambda: defaultdict(int))

        for row in grid:
            value_count[tuple(row)]["rows"] += 1
        
        for i in range(len(grid)):
            the_col = [grid[j][i] for j in range(len(grid))]
            value_count[tuple(the_col)]["cols"] += 1

        total = 0
        for value_tuple, counts in value_count.items():
            if len(counts) > 1:
                total += counts["rows"] * counts["cols"]

        return total

print(Solution().equalPairs(
    [
        [3, 2, 1],
        [1, 7, 6],
        [2, 7, 7]
    ]
) == 1)


print(Solution().equalPairs([
    [3, 1, 2, 2],
    [1, 4, 4, 5],
    [2, 4, 2, 2],
    [2, 4, 2, 2]
]) == 3)

print(Solution().equalPairs([
    [11, 1],
    [1, 11]
]) == 2)

print(Solution().equalPairs([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]) == 9)