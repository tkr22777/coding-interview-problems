import heapq
from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def count_soldiers(row):
            left = 0
            right = len(row) - 1
            while left <= right:
                mid = (left + right) // 2
                if row[mid] == 0:
                    right = mid - 1
                else:
                    left = mid + 1
            return left
            
        # using heap to keep track of the kth smallest
        pq = []
        for i in range(len(mat)):
            c = count_soldiers(mat[i])
            entry = (-1 * c, -1 * i)

            if len(pq) < k:
                heapq.heappush(pq, entry)
            else:
                kth_smallest = pq[0]
                if entry > kth_smallest:
                    heapq.heappop(pq)
                    heapq.heappush(pq, entry)
        
        ret = []
        for i in range(k):
            ret.append(-1 * heapq.heappop(pq)[1])
        # print(ret)
        ret.reverse()
        # print(ret)
        return ret
    

s = Solution()
mat = [
    [1,1,0,0,0],
    [1,1,1,1,0],
    [1,0,0,0,0],
    [1,1,0,0,0],
    [1,1,1,1,1]
]
k = 3
expected = [2, 0, 3]
print("1st case:" + str(expected == s.kWeakestRows(mat, k)))

mat = [
[1,0,0,0],
[1,1,1,1],
[1,0,0,0],
[1,0,0,0]
]
k = 2
expected = [0, 2]
print("2nd case:" + str(expected == s.kWeakestRows(mat, k)))