import heapq

class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        max_hl = len(self.max_heap)
        min_hl = len(self.min_heap)
        if max_hl == min_hl:
            if min_hl == 0:  # max_hl is 0 as well
                heapq.heappush(self.max_heap, -1 * num)
                return

            min_heap_v = self.min_heap[0]
            if num <= min_heap_v:
                heapq.heappush(self.max_heap, -1 * num)
            else:
                heapq.heappop(self.min_heap)
                heapq.heappush(self.min_heap, num)
                heapq.heappush(self.max_heap, -1 * min_heap_v)
        else:
            max_heap_v = -1 * self.max_heap[0]
            if num >= max_heap_v:
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappop(self.max_heap)
                heapq.heappush(self.max_heap, -1 * num)
                heapq.heappush(self.min_heap, max_heap_v)

    def findMedian(self) -> float:
        max_heap_v = -1 * self.max_heap[0]
        if len(self.min_heap) == len(self.max_heap):
            min_heap_v = self.min_heap[0]
            return (max_heap_v + min_heap_v) / 2
        else:
            return max_heap_v 