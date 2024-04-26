# https://leetcode.com/problems/search-a-2d-matrix/
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        if target < matrix[0][0]:
            return False
        
        def bin_search_first_col(matrix: List[List[int]], target: int):
            min = 0
            rows = len(matrix) - 1
            max = rows
            while min <= max:
                mid = (min + max) // 2
                if matrix[mid][0] == target:
                    return (True, -1)
                elif matrix[mid][0] < target:
                    if mid + 1 > rows or (mid + 1 <= rows and matrix[mid + 1][0] > target):
                        return (False, mid)
                    else:
                        min = mid + 1
                else:
                    max = mid - 1

            return (False, min)

        def bin_search_row(row: List[int], target) -> bool:
            l = 0
            r = len(row) - 1
            while l <= r:
                m = (l + r) // 2
                if row[m] == target:
                    return True
                elif row[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return False
        
        (found, row_index) = bin_search_first_col(matrix, target)
        if found:
            return True
        
        if row_index > len(matrix) - 1:
            return False

        return bin_search_row(matrix[row_index], target)


s = Solution()
matrix = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
]
print("1st case:" + str(True == s.searchMatrix(matrix, 34)))
print("2nd case:" + str(False == s.searchMatrix(matrix, 19)))
print("3rd case:" + str(True == s.searchMatrix(matrix, 60)))
print("4th case:" + str(False == s.searchMatrix(matrix, 61)))

print("5th case:" + str(True == s.searchMatrix(matrix, 30)))
print("6th case:" + str(True == s.searchMatrix(matrix, 5)))
print("7th case:" + str(True == s.searchMatrix(matrix, 16)))
print("8th case:" + str(False == s.searchMatrix(matrix, -11)))


matrix = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
]
print("9th case:" + str(False == s.searchMatrix(matrix, 13)))
print("10th case:" + str(True == s.searchMatrix(matrix, 30)))
print("11th case:" + str(True == s.searchMatrix(matrix, 20)))
print("12th case:" + str(False == s.searchMatrix(matrix, 8)))