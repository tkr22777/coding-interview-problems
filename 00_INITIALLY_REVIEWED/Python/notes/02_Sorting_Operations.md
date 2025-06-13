# Sorting Operations

<details>
<summary><strong>Basic Sorting</strong></summary>

```python
# Time Complexity:
# - sorted() and .sort(): O(n log n) average, O(n²) worst (Timsort)
# - Custom sorting with key: O(n log n)
# Space Complexity: O(n) for sorted(), O(1) for .sort()

# Basic operations
vals = [4, 2, 0, 3, 1], vals1 = [5, 6, 7, 8, 9]
sorted(vals)                                    # [0, 1, 2, 3, 4] (doesn't mutate) - O(n log n)
vals.sort()                                     # mutates vals to [0, 1, 2, 3, 4] - O(n log n)
sorted(vals) + vals1                            # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] - O(n log n + m)

# Examples
numbers = [5, 2, 9, 1, 5, 6]
sorted(numbers)                                 # [1, 2, 5, 5, 6, 9] - O(n log n)
sorted(numbers, reverse=True)                   # [9, 6, 5, 5, 2, 1] - O(n log n)

strings = ["banana", "apple", "cherry"]
sorted(strings)                                 # ['apple', 'banana', 'cherry'] - O(n log n)
sorted(strings, key=str.lower)                  # Case-insensitive - O(n log n)

# Custom sorting
tuples = [(1, 'b'), (2, 'a'), (3, 'c')]
sorted(tuples, key=lambda x: x[1])              # [(2, 'a'), (1, 'b'), (3, 'c')] - O(n log n)

words = ["banana", "apple", "cherry", "date"]
sorted(words, key=len)                          # ['date', 'apple', 'banana', 'cherry'] - O(n log n)

# Zip and sort
difficulty = [3, 1, 2]
profit = [30, 10, 20]
sorted(list(zip(difficulty, profit)), key=lambda x: x[0])  # [(1, 10), (2, 20), (3, 30)] - O(n log n)
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
bisect.bisect_left(arr, 4)                     # 2 (first position where 4 can be inserted) - O(log n)
bisect.bisect_right(arr, 4)                    # 4 (position after existing 4s) - O(log n)
bisect.bisect_left(arr, 3)                     # 2 (value not in array) - O(log n)
bisect.bisect_right(arr, 7)                    # 6 (value not in array) - O(log n)

# Insert maintaining order
sorted_list = [10, 20, 30, 40, 50]
bisect.insort(sorted_list, 25)                 # [10, 20, 25, 30, 40, 50] - O(n)

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
ss = SortedSet([3, 1, 4, 1, 5])               # SortedSet([1, 3, 4, 5]) - O(n log n)
ss.add(2)                                      # SortedSet([1, 2, 3, 4, 5]) - O(log n)
ss.remove(3)                                   # SortedSet([1, 2, 4, 5]) - O(log n)

# Custom sorting with objects
class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age
    
    def __repr__(self):
        return f"{self.name} ({self.age})"
    
    def __lt__(self, other):
        return self.age < other.age

people = SortedSet([Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)])
# Output: [Bob (25), Alice (30), Charlie (35)] - O(n log n)
people.add(Person("Dave", 20))
# Output: [Dave (20), Bob (25), Alice (30), Charlie (35)] - O(log n)

# Range operations and element finding
# IMPORTANT: Use irange() for efficient range queries - O(log n + k)
# Converting to list() first would be O(n) and defeat the purpose!
ss = SortedSet([10, 20, 30, 40, 50])

# Find closest elements to a query value
def find_floor(sorted_set, query):
    """Find largest element <= query - O(log n)"""
    idx = sorted_set.bisect_right(query) - 1
    return sorted_set[idx] if idx >= 0 else None

def find_ceiling(sorted_set, query):
    """Find smallest element >= query - O(log n)"""
    idx = sorted_set.bisect_left(query)
    return sorted_set[idx] if idx < len(sorted_set) else None

def find_predecessor(sorted_set, query):
    """Find largest element < query - O(log n)"""
    idx = sorted_set.bisect_left(query) - 1
    return sorted_set[idx] if idx >= 0 else None

def find_successor(sorted_set, query):
    """Find smallest element > query - O(log n)"""
    idx = sorted_set.bisect_right(query)
    return sorted_set[idx] if idx < len(sorted_set) else None

# Examples with ss = [10, 20, 30, 40, 50]
find_floor(ss, 25)                             # 20 (largest <= 25) - O(log n)
find_ceiling(ss, 25)                           # 30 (smallest >= 25) - O(log n)
find_predecessor(ss, 30)                       # 20 (largest < 30) - O(log n)
find_successor(ss, 30)                         # 40 (smallest > 30) - O(log n)

# Get elements in range
def get_range_set(sorted_set, min_val, max_val):
    """Get elements in [min_val, max_val] - O(log n + k) where k is result size"""
    return list(sorted_set.irange(min_val, max_val))

# Get elements >= threshold
def get_elements_gte(sorted_set, threshold):
    """Get elements >= threshold - O(log n + k) where k is result size"""
    return list(sorted_set.irange(threshold))

# Get elements <= threshold
def get_elements_lte(sorted_set, threshold):
    """Get elements <= threshold - O(log n + k) where k is result size"""
    return list(sorted_set.irange(None, threshold, (True, True)))

# Examples
get_range_set(ss, 25, 45)                      # [30, 40] - O(log n + k)
get_elements_gte(ss, 35)                       # [40, 50] - O(log n + k)
get_elements_lte(ss, 35)                       # [10, 20, 30] - O(log n + k)

# Count operations
def count_less_than(sorted_set, query):
    """Count elements < query - O(log n)"""
    return sorted_set.bisect_left(query)

def count_less_equal(sorted_set, query):
    """Count elements <= query - O(log n)"""
    return sorted_set.bisect_right(query)

def count_in_range(sorted_set, min_val, max_val):
    """Count elements in [min_val, max_val] - O(log n)"""
    return sorted_set.bisect_right(max_val) - sorted_set.bisect_left(min_val)

# Examples
count_less_than(ss, 35)                        # 3 (elements < 35: 10,20,30) - O(log n)
count_less_equal(ss, 30)                       # 3 (elements <= 30: 10,20,30) - O(log n)
count_in_range(ss, 20, 40)                     # 3 (elements in [20,40]: 20,30,40) - O(log n)

# Peek operations
first_element = ss[0]                           # 10 (smallest) - O(1)
last_element = ss[-1]                          # 50 (largest) - O(1)

# Pop operations
smallest = ss.pop(0)                           # 10 - O(log n)
largest = ss.pop(-1)                           # 50 - O(log n)
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

# With custom objects
class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age
    
    def __repr__(self):
        return f"Person({self.name}, {self.age})"

people = SortedDict({
    30: Person("Alice", 30),
    25: Person("Bob", 25),
    35: Person("Charlie", 35)
})
# Keys remain sorted: {25: Person(Bob, 25), 30: Person(Alice, 30), 35: Person(Charlie, 35)} - O(n log n)

# Range operations and subtree extraction
# IMPORTANT: Use irange() for efficient range queries - O(log n + k)
# Converting to list() first would be O(n) and defeat the purpose!
sd = SortedDict({10: "A", 20: "B", 30: "C", 40: "D", 50: "E"})

# Get all items with keys >= threshold
def get_items_gte(sorted_dict, threshold):
    """Get all items with keys >= threshold - O(log n + k) where k is result size"""
    return [(k, v) for k, v in sorted_dict.irange(threshold)]

# Get all items with keys <= threshold  
def get_items_lte(sorted_dict, threshold):
    """Get all items with keys <= threshold - O(log n + k) where k is result size"""
    return [(k, v) for k, v in sorted_dict.irange(None, threshold, (True, True))]

# Get range of items between two keys (inclusive)
def get_range(sorted_dict, min_key, max_key):
    """Get items with keys in [min_key, max_key] - O(log n + k) where k is result size"""
    return [(k, v) for k, v in sorted_dict.irange(min_key, max_key)]

# Examples
get_items_gte(sd, 25)                          # [(30, 'C'), (40, 'D'), (50, 'E')] - O(log n + k)
get_items_lte(sd, 35)                          # [(10, 'A'), (20, 'B'), (30, 'C')] - O(log n + k)
get_range(sd, 20, 40)                          # [(20, 'B'), (30, 'C'), (40, 'D')] - O(log n + k)

# Iterate from specific key onwards
def iterate_from(sorted_dict, start_key):
    """Iterate starting from start_key - O(log n) to find start, O(1) per iteration"""
    for key, value in sorted_dict.irange(start_key):
        yield key, value

# Usage: iterate from key 25 onwards
for key, value in iterate_from(sd, 25):
    print(f"{key}: {value}")                   # Prints 30:C, 40:D, 50:E

# Peek operations for first/last elements
first_key, first_value = sd.peekitem(0)        # (10, 'A') - O(1)
last_key, last_value = sd.peekitem(-1)         # (50, 'E') - O(1)

# Pop operations maintaining order
smallest = sd.popitem(0)                       # (10, 'A') - O(log n)
largest = sd.popitem(-1)                       # (50, 'E') - O(log n)
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
heapq.heappush(heap, 3)                         # heap: [3] - O(log n)
heapq.heappush(heap, 1)                         # heap: [1, 3] - O(log n)
heapq.heappush(heap, 2)                         # heap: [1, 2, 3] - O(log n)

smallest = heapq.heappop(heap)                  # smallest: 1, heap: [2, 3] - O(log n)

# Combined push and pop
next_smallest = heapq.heappushpop(heap, 4)      # push 4, pop smallest: 2, heap: [3, 4] - O(log n)
replaced = heapq.heapreplace(heap, 6)           # pop 3, push 6: heap: [4, 6] - O(log n)

# Transform list to heap
list_to_heap = [5, 1, 3, 2]
heapq.heapify(list_to_heap)                     # [1, 2, 3, 5] in-place - O(n)

# Find largest/smallest
data = [3, 1, 4, 1, 5, 9, 2]
heapq.nlargest(2, data)                         # [9, 5] - O(n log k)
heapq.nsmallest(2, data)                        # [1, 1] - O(n log k)

# Heap with objects
class Item:
    def __init__(self, name, priority):
        self.name, self.priority = name, priority
    
    def __repr__(self):
        return f"Item({self.name}, {self.priority})"

items = [Item("item1", 5), Item("item2", 1), Item("item3", 3)]
heap = [(item.priority, item) for item in items]
heapq.heapify(heap)                             # O(n)

new_item = Item("item4", 2)
heapq.heappush(heap, (new_item.priority, new_item))  # O(log n)
popped_item = heapq.heappop(heap)[1]            # Get the item, not the priority - O(log n)

# Max heap of size k (for k largest elements)
def maintain_k_largest(arr, k):
    heap = []
    for num in arr:                             # O(n log k)
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)                 # Remove smallest
    return heap                                 # heap[0] is kth largest

# Nth largest element O(N log k)
def nth_largest(arr, n):
    heap = arr[:n]
    heapq.heapify(heap)                         # O(n)
    for num in arr[n:]:                         # O((N-n) log n)
        if num > heap[0]:
            heapq.heapreplace(heap, num)
    return heap[0]                              # nth largest

# Nth smallest element O(N log k) 
def nth_smallest(arr, n):
    heap = [-x for x in arr[:n]]                # Max heap (negate values)
    heapq.heapify(heap)                         # O(n)
    for num in arr[n:]:                         # O((N-n) log n)
        if num < -heap[0]:
            heapq.heapreplace(heap, -num)
    return -heap[0]                             # nth smallest

# Examples
arr = [3, 1, 4, 1, 5, 9, 2, 6]
maintain_k_largest(arr, 3)                      # [4, 5, 9] (3 largest) - O(n log k)
nth_largest(arr, 3)                             # 5 (3rd largest) - O(n log n)
nth_smallest(arr, 3)                            # 2 (3rd smallest) - O(n log n)

# Heap indexing (array-based tree)
# Parent of i: (i-1)//2, Left child: 2*i+1, Right child: 2*i+2
arr = [5, 1, 3, 2]
heapq.heapify(arr)                              # [1, 2, 3, 5] - O(n)
# Index:  0  1  2  3  (parent of 3 is (3-1)//2 = 1)
# Tree:      1
#           / \
#          2   3
#         /
#        5
```

</details> 