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
vals = [4, 2, 0, 3, 1]
vals.sort()                                     # [0, 1, 2, 3, 4] mutates vals in-place

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
arr_copy = arr.copy()
bisect.insort(arr_copy, 3)                     # [1, 2, 3, 4, 4, 5, 6, 8] inserts in correct position

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
ss = SortedSet([3, 1, 4, 1, 5])               # SortedSet([1, 3, 4, 5]) - duplicates removed
ss.add(2)                                      # SortedSet([1, 2, 3, 4, 5])
ss.remove(3)                                   # SortedSet([1, 2, 4, 5])

# Range operations and element finding
ss = SortedSet([10, 20, 30, 40, 50])

# Find closest elements
def find_floor(sorted_set, query):
    """Find largest element <= query"""
    idx = sorted_set.bisect_right(query) - 1
    return sorted_set[idx] if idx >= 0 else None

# Bisect operations - find insertion positions and ranks
# Using ss = SortedSet([10, 20, 30, 40, 50])
ss.bisect_left(35)                             # 3 (insertion position, rank of 35)
ss.bisect_right(35)                            # 3 (position after 35 if it exists)
ss.bisect_left(25)                             # 2 (elements < 25)
ss.bisect_right(50)                            # 5 (total elements <= 50)

# Calculate rank of element (0-indexed position)
def get_rank(sorted_set, element):
    return sorted_set.bisect_left(element)      # O(log n)

# Check if element exists and get its rank
def find_element_rank(sorted_set, element):
    rank = sorted_set.bisect_left(element)
    if rank < len(sorted_set) and sorted_set[rank] == element:
        return rank  # Element exists at this rank
    return -1        # Element doesn't exist

# Range queries and iteration
list(ss.irange(25, 45))                        # [30, 40] - elements in range [25, 45]
ss[0], ss[-1]                                  # (10, 50) - first, last elements

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

# Bisect operations on keys - find insertion positions and ranks
# Using sd after updates: SortedDict({20: 'Dave', 25: 'Eve', 30: 'Alice', 35: 'Charlie'})
sd.bisect_left(25)                             # 1 (insertion position for key 25)
sd.bisect_right(30)                            # 3 (position after key 30)
sd.bisect_left(15)                             # 0 (keys < 15)

# Get rank of key in dictionary
def get_key_rank(sorted_dict, key):
    return sorted_dict.bisect_left(key)         # O(log n)

# Find key rank and check existence
def find_key_rank(sorted_dict, key):
    rank = sorted_dict.bisect_left(key)
    keys = list(sorted_dict.keys())
    if rank < len(keys) and keys[rank] == key:
        return rank  # Key exists at this rank
    return -1        # Key doesn't exist

# Range operations and iteration
sd = SortedDict({10: "A", 20: "B", 30: "C", 40: "D", 50: "E"})
list(sd.irange(20, 40))                        # [20, 30, 40] - keys only!

# Iterate through key-value pairs
for key, value in sd.items():                  # Iterate all items in key order
    print(f"{key}: {value}")

# Iterate through range
for key in sd.irange(20, 40):                 # Iterate keys in range [20, 40]
    value = sd[key]                              # Access value separately
    print(f"{key}: {value}")

# Iterate keys only
for key in sd:                                 # Iterate keys in sorted order
    print(key)

# Get range as list for processing
keys_in_range = list(sd.irange(20, 40))        # [20, 30, 40] - keys only!
items_in_range = [(k, sd[k]) for k in sd.irange(20, 40)]  # Get key-value pairs

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

# Bisect operations - find insertion positions and ranks (allows duplicates)
sl = SortedList([10, 20, 20, 30, 40, 50, 60])  # [10, 20, 20, 30, 40, 50, 60]
sl.bisect_left(20)                             # 1 (first position of 20)
sl.bisect_right(20)                            # 3 (position after last 20)
sl.bisect_left(25)                             # 3 (insertion point, rank if inserted)
sl.bisect_right(35)                            # 4 (elements <= 35)

# Calculate rank with duplicates
def get_element_rank(sorted_list, element):
    return sorted_list.bisect_left(element)     # O(log n) - rank of first occurrence

# Count elements in range [a, b]
def count_in_range(sorted_list, a, b):
    return sorted_list.bisect_right(b) - sorted_list.bisect_left(a)  # O(log n)

# Range operations and iteration
# Using same data: sl = SortedList([10, 20, 20, 30, 40, 50, 60])
list(sl.irange(15, 35))                        # [20, 20, 30]

# Iterate through elements
for element in sl:                             # Iterate all elements in sorted order
    print(element)

# Iterate through range
for element in sl.irange(15, 35):              # Iterate elements in range [15, 35]
    print(element)                             # Prints: 20, 20, 30

# Access by index (unlike SortedSet)
for i in range(len(sl)):                       # Access by index
    print(f"Index {i}: {sl[i]}")              # Index 0: 10, Index 1: 20, etc.

# Get range as list for processing
elements_in_range = list(sl.irange(15, 35))    # [20, 20, 30]

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