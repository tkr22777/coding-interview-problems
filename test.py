import heapq
import random


print('test')

heap = []
for i in range(10):
    heapq.heappush(heap, [random.randint(0, 100), str(i)])

print("heap in list:")
for i in range(len(heap)):
    print(heap[i])

print("heap ordered:")
for i in range(len(heap)):
    val = heapq.heappop(heap)
    print(val)
