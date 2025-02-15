from collections import defaultdict

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        dd = defaultdict(lambda: defaultdict(int))

        for row in range(len(grid)):
            row_str = str(grid[row])
            dd[row_str]["rows"] += 1
        
        for col in range(len(grid)):
            the_col = []
            for row in range(len(grid)):
                the_col.append(grid[row][col])
            col_str = str(the_col)
            dd[col_str]["cols"] += 1
        
        total = 0
        for key, value in dd.items():
            if len(value) > 1:
                total += value["rows"] * value["cols"]

        return total
