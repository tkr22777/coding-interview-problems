# Sorting Operations

<details>
<summary><strong>Basic Sorting</strong></summary>

```python
# Time Complexity:
# - sorted() and .sort(): O(n log n) average, O(n²) worst (Timsort)
# - Custom sorting with key: O(n log n)
# Space Complexity: O(n) for sorted(), O(1) for .sort()

# Basic operations
sorted_list = sorted([4, 2, 0, 3, 1])          # [0, 1, 2, 3, 4] (doesn't mutate)
vals.sort()                                     # mutates vals in-place

# Iterate through sorted results
for element in sorted_list:                     # Iterate through sorted elements
    print(element)

# Access by index
for i, element in enumerate(sorted_list):       # Get index and element
    print(f"Index {i}: {element}")

# Custom sorting
sorted([(1, 'b'), (2, 'a')], key=lambda x: x[1])  # [(2, 'a'), (1, 'b')]
sorted(["banana", "apple"], key=len)            # ['apple', 'banana']
```

</details>

<details>
<summary><strong>Bisect (Binary Search)</strong></summary>

```python
# Time Complexity:
# - bisect_left/right: O(log n)
# - insort: O(n) (due to shifting elements)
# Space Complexity: O(1) for operations, O(n) for array

import bisect

# Basic operations
arr = [1, 2, 4, 4, 5, 6, 8]
bisect.bisect_left(arr, 4)                     # 2 (first position where 4 can be inserted)
bisect.bisect_right(arr, 4)                    # 4 (position after existing 4s)

# Insert maintaining order
bisect.insort(sorted_list, 25)                 # Inserts 25 in correct position

# Count elements pattern
def count_elements(arr, queries):
    arr = sorted(arr)                          # O(n log n)
    results = []
    for x in queries:                          # O(m log n) where m is number of queries
        count_smaller = bisect.bisect_left(arr, x)
        count_greater = len(arr) - bisect.bisect_right(arr, x)
        results.append((count_smaller, count_greater))
    return results

# Example usage
arr = [3, 6, 1, 8, 2, 9, 4]
queries = [5, 1, 10]
count_elements(arr, queries)                    # [(4, 2), (0, 6), (7, 0)] - O(n log n + m log n)
```

</details>

<details>
<summary><strong>SortedSet</strong></summary>

```python
# Time Complexity:
# - Insert/Delete: O(log n)
# - Search: O(log n)
# - Iteration: O(n)
# Space Complexity: O(n)

# Required: pip install sortedcontainers
from sortedcontainers import SortedSet

# Basic usage
ss = SortedSet([3, 1, 4, 1, 5])               # SortedSet([1, 3, 4, 5])
ss.add(2)                                      # Adds in correct position
ss.remove(3)                                   # Removes element

# Range operations and element finding
ss = SortedSet([10, 20, 30, 40, 50])

# Find closest elements
def find_floor(sorted_set, query):
    """Find largest element <= query"""
    idx = sorted_set.bisect_right(query) - 1
    return sorted_set[idx] if idx >= 0 else None

# Range queries and iteration
list(ss.irange(25, 45))                        # [30, 40]
ss.bisect_left(35)                             # Count elements < 35
ss[0], ss[-1]                                  # First, last elements

# Iterate through elements
for element in ss:                              # Iterate all elements in sorted order
    print(element)

# Iterate through range
for element in ss.irange(20, 40):               # Iterate elements in [20, 40]
    print(element)

# Get elements as list for processing
elements_in_range = list(ss.irange(20, 40))    # Convert to list for indexing
```

</details>

<details>
<summary><strong>SortedDict</strong></summary>

```python
# Time Complexity:
# - Insert/Delete: O(log n)
# - Search: O(log n)
# - Iteration: O(n)
# Space Complexity: O(n)

from sortedcontainers import SortedDict

# Basic usage (sorted by keys)
sd = SortedDict({30: "Alice", 25: "Bob", 35: "Charlie"})
# SortedDict({25: 'Bob', 30: 'Alice', 35: 'Charlie'}) - O(n log n)

sd[20] = "Dave"                                # Maintains sorted order - O(log n)
sd[25] = "Eve"                                 # Updates existing key - O(log n)

# Range operations and iteration
sd = SortedDict({10: "A", 20: "B", 30: "C", 40: "D", 50: "E"})
list(sd.irange(20, 40))                        # [(20, 'B'), (30, 'C'), (40, 'D')]

# Iterate through key-value pairs
for key, value in sd.items():                  # Iterate all items in key order
    print(f"{key}: {value}")

# Iterate through range
for key, value in sd.irange(20, 40):           # Iterate items in key range [20, 40]
    print(f"{key}: {value}")

# Iterate keys only
for key in sd:                                 # Iterate keys in sorted order
    print(key)

# Get range as list for processing
items_in_range = list(sd.irange(20, 40))       # [(20, 'B'), (30, 'C'), (40, 'D')]

# Peek operations
sd.peekitem(0)                                 # (10, 'A') - first item
sd.peekitem(-1)                                # (50, 'E') - last item
```

</details>

<details>
<summary><strong>SortedList</strong></summary>

```python
# Time Complexity:
# - Insert/Delete: O(log n)
# - Search: O(log n)
# - Index access: O(log n)
# - Iteration: O(n)
# Space Complexity: O(n)

# Required: pip install sortedcontainers
from sortedcontainers import SortedList

# Basic usage - maintains sorted order automatically
sl = SortedList([3, 1, 4, 1, 5])              # SortedList([1, 1, 3, 4, 5]) - O(n log n)
sl.add(2)                                      # SortedList([1, 1, 2, 3, 4, 5]) - O(log n)
sl.remove(1)                                   # SortedList([1, 2, 3, 4, 5]) - removes first occurrence - O(log n)

# Index-based access (unlike SortedSet)
sl[0]                                          # 1 (first element) - O(log n)
sl[-1]                                         # 5 (last element) - O(log n)
sl[2]                                          # 3 (element at index 2) - O(log n)

# Allows duplicates (unlike SortedSet)
sl = SortedList([1, 2, 2, 3, 3, 3])
sl.count(2)                                    # 2 - O(log n)
sl.count(3)                                    # 3 - O(log n)

# Range operations and iteration
sl = SortedList([10, 20, 30, 40, 50, 60])
list(sl.irange(25, 45))                        # [30, 40]
sl.bisect_left(25)                             # 2 (insertion point)

# Iterate through elements
for element in sl:                             # Iterate all elements in sorted order
    print(element)

# Iterate through range
for element in sl.irange(25, 45):              # Iterate elements in range [25, 45]
    print(element)

# Access by index (unlike SortedSet)
for i in range(len(sl)):                       # Access by index
    print(f"Index {i}: {sl[i]}")

# Get range as list for processing
elements_in_range = list(sl.irange(25, 45))    # [30, 40]

# Find closest elements
def find_floor_list(sorted_list, query):
    """Find largest element <= query"""
    idx = sorted_list.bisect_right(query) - 1
    return sorted_list[idx] if idx >= 0 else None

# Practical use cases
class MedianFinder:
    def __init__(self):
        self.nums = SortedList()
    
    def add_num(self, num):
        self.nums.add(num)
    
    def find_median(self):
        n = len(self.nums)
        return self.nums[n // 2] if n % 2 == 1 else (self.nums[n // 2 - 1] + self.nums[n // 2]) / 2
```

</details>

<details>
<summary><strong>Heap/Priority Queue</strong></summary>

```python
# Time Complexity:
# - Insert: O(log n)
# - Extract min/max: O(log n)
# - Heapify: O(n)
# - nlargest/nsmallest: O(n log k) where k is number of elements
# Space Complexity: O(n)

import heapq

# Basic operations
heap = []
heapq.heappush(heap, 3)                         # heap: [3]
heapq.heappop(heap)                             # Returns and removes smallest

# Transform list to heap
heapq.heapify([5, 1, 3, 2])                    # In-place heapification

# Find largest/smallest
largest = heapq.nlargest(2, [3, 1, 4, 1, 5, 9, 2])    # [9, 5]
smallest = heapq.nsmallest(2, [3, 1, 4, 1, 5, 9, 2])  # [1, 1]

# Iterate through results
for element in largest:                         # Iterate through largest elements
    print(f"Large: {element}")

for element in smallest:                        # Iterate through smallest elements
    print(f"Small: {element}")

# Heap with objects (use tuples for priority)
heap = [(priority, item) for priority, item in [(5, "item1"), (1, "item2")]]
heapq.heapify(heap)
heapq.heappush(heap, (2, "item3"))
priority, item = heapq.heappop(heap)            # Get both priority and item

# Kth largest using min heap
def kth_largest(arr, k):
    heap = arr[:k]
    heapq.heapify(heap)
    for num in arr[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)
    return heap[0]

# Max heap simulation (negate values)
def kth_smallest(arr, k):
    heap = [-x for x in arr[:k]]
    heapq.heapify(heap)
    for num in arr[k:]:
        if num < -heap[0]:
            heapq.heapreplace(heap, -num)
    return -heap[0]
```

</details> 