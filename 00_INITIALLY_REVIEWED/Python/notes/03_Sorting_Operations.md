# Sorting Operations

<details>
<summary><strong>Basic Sorting</strong></summary>

```python
# Basic operations
vals = [4, 2, 0, 3, 1], vals1 = [5, 6, 7, 8, 9]
sorted(vals)                                    # [0, 1, 2, 3, 4] (doesn't mutate)
vals.sort()                                     # mutates vals to [0, 1, 2, 3, 4]
sorted(vals) + vals1                            # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Examples
numbers = [5, 2, 9, 1, 5, 6]
sorted(numbers)                                 # [1, 2, 5, 5, 6, 9]
sorted(numbers, reverse=True)                   # [9, 6, 5, 5, 2, 1]

strings = ["banana", "apple", "cherry"]
sorted(strings)                                 # ['apple', 'banana', 'cherry']
sorted(strings, key=str.lower)                  # Case-insensitive

# Custom sorting
tuples = [(1, 'b'), (2, 'a'), (3, 'c')]
sorted(tuples, key=lambda x: x[1])              # [(2, 'a'), (1, 'b'), (3, 'c')]

words = ["banana", "apple", "cherry", "date"]
sorted(words, key=len)                          # ['date', 'apple', 'banana', 'cherry']

# Zip and sort
difficulty = [3, 1, 2]
profit = [30, 10, 20]
sorted(list(zip(difficulty, profit)), key=lambda x: x[0])  # [(1, 10), (2, 20), (3, 30)]
```

</details>

<details>
<summary><strong>Bisect (Binary Search)</strong></summary>

```python
import bisect

# Basic operations
arr = [1, 2, 4, 4, 5, 6, 8]
bisect.bisect_left(arr, 4)                     # 2 (first position where 4 can be inserted)
bisect.bisect_right(arr, 4)                    # 4 (position after existing 4s)
bisect.bisect_left(arr, 3)                     # 2 (value not in array)
bisect.bisect_right(arr, 7)                    # 6 (value not in array)

# Insert maintaining order
sorted_list = [10, 20, 30, 40, 50]
bisect.insort(sorted_list, 25)                 # [10, 20, 25, 30, 40, 50]

# Count elements pattern
def count_elements(arr, queries):
    arr = sorted(arr)
    results = []
    for x in queries:
        count_smaller = bisect.bisect_left(arr, x)
        count_greater = len(arr) - bisect.bisect_right(arr, x)
        results.append((count_smaller, count_greater))
    return results

# Example usage
arr = [3, 6, 1, 8, 2, 9, 4]
queries = [5, 1, 10]
count_elements(arr, queries)                    # [(4, 2), (0, 6), (7, 0)]
```

</details>

<details>
<summary><strong>SortedSet</strong></summary>

```python
# Required: pip install sortedcontainers
from sortedcontainers import SortedSet

# Basic usage
ss = SortedSet([3, 1, 4, 1, 5])               # SortedSet([1, 3, 4, 5])
ss.add(2)                                      # SortedSet([1, 2, 3, 4, 5])
ss.remove(3)                                   # SortedSet([1, 2, 4, 5])

# Custom sorting with objects
class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age
    
    def __repr__(self):
        return f"{self.name} ({self.age})"
    
    def __lt__(self, other):
        return self.age < other.age

people = SortedSet([Person("Alice", 30), Person("Bob", 25), Person("Charlie", 35)])
# Output: [Bob (25), Alice (30), Charlie (35)]
people.add(Person("Dave", 20))
# Output: [Dave (20), Bob (25), Alice (30), Charlie (35)]
```

</details>

<details>
<summary><strong>SortedDict</strong></summary>

```python
from sortedcontainers import SortedDict

# Basic usage (sorted by keys)
sd = SortedDict({30: "Alice", 25: "Bob", 35: "Charlie"})
# SortedDict({25: 'Bob', 30: 'Alice', 35: 'Charlie'})

sd[20] = "Dave"                                # Maintains sorted order
sd[25] = "Eve"                                 # Updates existing key

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
# Keys remain sorted: {25: Person(Bob, 25), 30: Person(Alice, 30), 35: Person(Charlie, 35)}
```

</details>

<details>
<summary><strong>Heap/Priority Queue</strong></summary>

```python
import heapq

# Basic operations
heap = []
heapq.heappush(heap, 3)                         # heap: [3]
heapq.heappush(heap, 1)                         # heap: [1, 3]
heapq.heappush(heap, 2)                         # heap: [1, 2, 3]

smallest = heapq.heappop(heap)                  # smallest: 1, heap: [2, 3]

# Combined push and pop
next_smallest = heapq.heappushpop(heap, 4)      # push 4, pop smallest: 2, heap: [3, 4]
replaced = heapq.heapreplace(heap, 6)           # pop 3, push 6: heap: [4, 6]

# Transform list to heap
list_to_heap = [5, 1, 3, 2]
heapq.heapify(list_to_heap)                     # [1, 2, 3, 5] in-place

# Find largest/smallest
data = [3, 1, 4, 1, 5, 9, 2]
heapq.nlargest(2, data)                         # [9, 5]
heapq.nsmallest(2, data)                        # [1, 1]

# Heap with objects
class Item:
    def __init__(self, name, priority):
        self.name, self.priority = name, priority
    
    def __repr__(self):
        return f"Item({self.name}, {self.priority})"

items = [Item("item1", 5), Item("item2", 1), Item("item3", 3)]
heap = [(item.priority, item) for item in items]
heapq.heapify(heap)

new_item = Item("item4", 2)
heapq.heappush(heap, (new_item.priority, new_item))
popped_item = heapq.heappop(heap)[1]            # Get the item, not the priority

# Max heap of size k (for k largest elements)
def maintain_k_largest(arr, k):
    heap = []
    for num in arr:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)                 # Remove smallest
    return heap                                 # heap[0] is kth largest

# Nth largest element O(N log k)
def nth_largest(arr, n):
    heap = arr[:n]
    heapq.heapify(heap)                         # Min heap of size n
    for num in arr[n:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)
    return heap[0]                              # nth largest

# Nth smallest element O(N log k) 
def nth_smallest(arr, n):
    heap = [-x for x in arr[:n]]                # Max heap (negate values)
    heapq.heapify(heap)
    for num in arr[n:]:
        if num < -heap[0]:
            heapq.heapreplace(heap, -num)
    return -heap[0]                             # nth smallest

# Examples
arr = [3, 1, 4, 1, 5, 9, 2, 6]
maintain_k_largest(arr, 3)                      # [4, 5, 9] (3 largest)
nth_largest(arr, 3)                             # 5 (3rd largest)
nth_smallest(arr, 3)                            # 2 (3rd smallest)

# Heap indexing (array-based tree)
# Parent of i: (i-1)//2, Left child: 2*i+1, Right child: 2*i+2
arr = [5, 1, 3, 2]
heapq.heapify(arr)                              # [1, 2, 3, 5] - rearranges to satisfy heap property
# Index:  0  1  2  3  (parent of 3 is (3-1)//2 = 1)
# Tree:      1
#           / \
#          2   3
#         /
#        5
```

</details> 