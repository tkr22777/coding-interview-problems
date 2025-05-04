import heapq
from typing import List
import bisect

# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/

"""
Solution Summary:
1. For each row, count the number of soldiers (1s) using binary search (bisect_left)
   - Since rows are sorted with 1s before 0s, bisect_left(row, 0) finds first 0
   - This position equals the count of soldiers in the row
2. Use a max heap of size k to keep track of k weakest rows
   - Store (-soldiers_count, -row_index) in heap to turn min heap into max heap
   - This way, rows with more soldiers get popped first when heap exceeds size k
3. Finally, extract and reverse the indices to get k weakest rows in ascending order

Time: O(m * log(n) + m * log(k)) where m = rows, n = cols
Space: O(k) for the heap
"""

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def count_soldiers(row):
            # Create reversed copy and use bisect_left
            rev_row = list(reversed(row))
            count = bisect.bisect_left(rev_row, 1)
            return len(row) - count

        # using heap to keep track of the k weakest rows (max_heap)
        pq = []
        for i in range(len(mat)):
            # Count soldiers using binary search on original row
            strength = count_soldiers(mat[i])
            entry = (-strength, -i)
            if len(pq) < k:
                heapq.heappush(pq, entry)
            else:
                heapq.heappushpop(pq, entry)

        ret = [-1 * heapq.heappop(pq)[1] for _ in range(k)]
        ret.reverse()
        return ret


def test_k_weakest_rows():
    s = Solution()
    
    test_cases = [
        # Matrix, k, Expected result
        (
            [
                [1, 1, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [1, 1, 1, 1, 1]
            ],
            3,
            [2, 0, 3]  # Rows with fewest soldiers
        ),
        (
            [
                [1, 0, 0, 0],
                [1, 1, 1, 1],
                [1, 0, 0, 0],
                [1, 0, 0, 0]
            ],
            2,
            [0, 2]  # Two weakest rows
        ),
        (
            [
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]
            ],
            3,
            [0, 1, 2]  # All equal, return by index
        ),
        (
            [
                [1, 0],
                [0, 0]
            ],
            1,
            [1]  # Row with no soldiers
        )
    ]
    
    for mat, k, expected in test_cases:
        result = s.kWeakestRows(mat, k)
        assert result == expected, f"For matrix {mat} and k={k}: expected {expected}, got {result}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_k_weakest_rows()
