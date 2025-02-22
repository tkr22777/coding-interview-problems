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
            print(f"key: {key}, val: {val}")
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq.heappushpop(heap, (val, key))

        return list(reversed([a[1] for a in heap]))
    
s = Solution()
print(s.topKFrequent(nums=[1,1,1,2,2,3], k=2))
print(s.topKFrequent(nums=[1,1,1,2,2,3], k=2) == [1,2])
print(s.topKFrequent(nums=[1], k=1) == [1])
print(s.topKFrequent(nums=[1,2,2,3,3,3,4,4,4,4], k=2) == [4,3])