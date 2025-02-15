from collections import defaultdict
from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = defaultdict(int)
        for n in nums:
            data[n] += 1

        heap = []
        for key, val in data.items():
            if len(heap) >= k:
                if heap[0][0] <= val:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (val, key))
            else:
                heapq.heappush(heap, (val, key))
            # print(heap)

        return [a[1] for a in heap] 