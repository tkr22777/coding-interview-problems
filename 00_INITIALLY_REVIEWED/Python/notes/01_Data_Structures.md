# Data Structures

<details>
<summary><strong>Collections Module</strong></summary>

```python
from collections import Counter, defaultdict, deque, OrderedDict

# Counter - frequency counting
# Time Complexity:
# - Creation: O(n)
# - most_common(k): O(n log k)
# - Access/Update: O(1)
# - Arithmetic ops: O(n)
nums = [1, 2, 2, 3, 3, 3]
cnt = Counter(nums)                            # {1: 1, 2: 2, 3: 3}
cnt.most_common(2)                             # [(3, 3), (2, 2)] (top 2 frequencies)
cnt[4] += 1                                    # Auto-initializes to 0, then increments
cnt.subtract([2, 2])                           # Decrements counts: {1: 1, 2: 0, 3: 3, 4: 1}

# Counter arithmetic
c1, c2 = Counter(a=3, b=1), Counter(a=1, b=2)
c1 + c2                                        # Counter({'a': 4, 'b': 3})
c1 - c2                                        # Counter({'a': 2}) (negative counts removed)

# defaultdict - auto-initializing dict
# Time Complexity: Same as dict
# - Access/Insert/Delete: O(1) average case
dd = defaultdict(list)                         # Auto-initializes to empty list
dd['key'].append(1)                            # No KeyError if 'key' doesn't exist

# OrderedDict - maintains insertion order
# Time Complexity: Same as dict
# - Access/Insert/Delete: O(1) average case
# - move_to_end: O(1)
od = OrderedDict()
od['a'] = 1; od['b'] = 2; od['c'] = 3         # Preserves order: a -> b -> c
od.move_to_end('a')                            # Moves 'a' to end: b -> c -> a

# deque - double-ended queue
# Time Complexity:
# - append/appendleft: O(1)
# - pop/popleft: O(1)
# - extend/extendleft: O(k) where k is length of iterable
# - rotate: O(k) where k is rotation amount
d = deque([1, 2, 3])
d.appendleft(0)                                # [0, 1, 2, 3]
d.extendleft([-1, -2])                         # [-2, -1, 0, 1, 2, 3]
d.rotate(2)                                    # [2, 3, -2, -1, 0, 1]
```

</details>

<details>
<summary><strong>List/Array</strong></summary>

```python
# Time Complexity:
# - Access by index: O(1)
# - Search: O(n)
# - Insert/Delete at end: O(1)
# - Insert/Delete at beginning/middle: O(n)
# - Slice: O(k) where k is slice length
# - Sort: O(n log n)
# Space Complexity: O(n)

arr = [1, 2, 3, 4, 5]

# Basic operations
arr.append(6)                                   # [1, 2, 3, 4, 5, 6] - O(1)
arr.insert(0, 0)                                # [0, 1, 2, 3, 4, 5, 6] - O(n)

# Remove operations
arr.remove(3)                                   # [0, 1, 2, 4, 5, 6] - O(n)
popped = arr.pop()                              # 6, arr becomes [0, 1, 2, 4, 5] - O(1)
popped_at = arr.pop(1)                          # 1, arr becomes [0, 2, 4, 5] - O(n)
del arr[0]                                      # [2, 4, 5] - O(n)
del arr[1:3]                                    # [2] - O(n)

# Reverse
arr.reverse()                                   # [5, 4, 2, 0] - O(n)
reversed_arr = arr[::-1]                        # [0, 2, 4, 5] - O(n)

# Slicing and copying
first_two = arr[:2]                             # [5, 4] - O(k)
last_two = arr[-2:]                             # [2, 0] - O(k)
copy_arr = arr.copy()                           # O(n)

# Find and count
index = arr.index(4)                            # 1 - O(n)
count = arr.count(2)                            # 1 - O(n)
exists = 4 in arr                               # True - O(n)

# Extend and clear
arr.extend([1, 2, 3])                           # [5, 4, 2, 0, 1, 2, 3] - O(k)
arr.clear()                                     # [] - O(1)

# Slice notation with step [start:stop:step]
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr[::-1]                                       # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (full reverse)
arr[::2]                                        # [0, 2, 4, 6, 8] (every 2nd element)
arr[1::2]                                       # [1, 3, 5, 7, 9] (every 2nd, starting at index 1)
arr[::-2]                                       # [9, 7, 5, 3, 1] (every 2nd in reverse)
arr[8:2:-1]                                     # [8, 7, 6, 5, 4, 3] (reverse from index 8 to 2)

# *** STRING ↔ LIST CONVERSIONS & REVERSAL ***
text = "hello world"
char_list = list(text)                          # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
back_to_string = ''.join(char_list)             # "hello world"

# String reversal (most efficient)
reversed_str = text[::-1]                       # "dlrow olleh" (slice notation)

# Word-level operations
words = text.split()                            # ['hello', 'world']
reversed_words = words[::-1]                    # ['world', 'hello']
reversed_sentence = ' '.join(reversed_words)    # "world hello"

# Character manipulation
char_list[0] = 'H'                              # ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
modified_string = ''.join(char_list)            # "Hello world"
```

</details>

<details>
<summary><strong>Stack</strong></summary>

```python
# Time Complexity:
# - push (append): O(1)
# - pop: O(1)
# - peek: O(1)
# - search: O(n)
# Space Complexity: O(n)

stack = []
stack.append('a')                               # Stack is now ['a'] - O(1)
stack.append('b')                               # Stack is now ['a', 'b'] - O(1)
stack.append('c')                               # Stack is now ['a', 'b', 'c'] - O(1)

is_empty = not stack                            # O(1)
size = len(stack)                               # O(1)
top_item = stack.pop()                          # O(1)
peek_item = stack[-1]                           # O(1)

# Remove all items from the stack
while stack:
    item = stack.pop()                          # O(1) per operation
```

</details>

<details>
<summary><strong>Queue/Deque</strong></summary>

```python
# Time Complexity:
# - Enqueue/Dequeue (deque): O(1)
# - Enqueue/Dequeue (list): O(n) for dequeue
# - Rotate: O(k) where k is rotation amount
# Space Complexity: O(n)

from collections import deque

# Initialize
d1 = deque([1, 2, 3, 4, 5])                    # O(n)

# Add elements
d1.append(6)                                    # O(1)
d1.appendleft(0)                                # O(1)

# Remove elements
right_item = d1.pop()                           # O(1)
left_item = d1.popleft()                        # O(1)

# Extend
d1.extend([7, 8, 9])                            # O(k)
d1.extendleft([-1, -2, -3])                     # O(k)

# Rotate
d1.rotate(2)                                    # O(k)
d1.rotate(-1)                                   # O(k)

# Clear
d1.clear()                                      # O(1)

# Additional queue patterns:

# Queue using list (not recommended for large data)
queue = []
queue.append(1)                                # Enqueue
queue.pop(0)                                   # Dequeue (O(n) operation)

# Queue using deque (recommended)
from collections import deque
queue = deque()
queue.append(1)                                # Enqueue
queue.popleft()                                # Dequeue (O(1) operation)
```

</details>

<details>
<summary><strong>OrderedDict</strong></summary>

```python
# Time Complexity:
# - Access/Insert/Delete: O(1) average case
# - move_to_end: O(1)
# - popitem: O(1)
# Space Complexity: O(n)

from collections import OrderedDict

od = OrderedDict()
od['a'] = 1                                     # O(1)
od['b'] = 2                                     # O(1)
od['c'] = 3                                     # O(1)

# Access and modify
value = od['a']                                 # O(1)
od['a'] = 4                                     # O(1)
size = len(od)                                  # O(1)

# Check membership
if 'a' in od:                                   # O(1)
    od['a'] = 6                                 # O(1)

# Move elements
od.move_to_end('a')                             # O(1)
od.move_to_end('b', last=False)                 # O(1)

# Pop operations
key, value = od.popitem()                       # O(1)
key, value = od.popitem(last=False)             # O(1)

# Peek operations
key, value = next(iter(od.items()))             # O(1)
key, value = next(reversed(od.items()))         # O(1)

# Clear
od.clear()                                      # O(1)

# LRU Cache implementation
class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

</details>

<details>
<summary><strong>Set</strong></summary>

```python
# Time Complexity:
# - Add/Remove/Contains: O(1) average case
# - Union/Intersection/Difference: O(len(s1) + len(s2))
# - issubset/issuperset: O(len(s1))
# Space Complexity: O(n)

s = {1, 2, 3}
s.add(4)                                        # O(1)
len(s)                                          # O(1)
s.discard(2)                                    # O(1)

# Set operations
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

s1.union(s2)                                    # O(len(s1) + len(s2))
s1.intersection(s2)                             # O(min(len(s1), len(s2)))
s1.difference(s2)                               # O(len(s1))
s1.symmetric_difference(s2)                     # O(len(s1) + len(s2))

# Set comparisons
s1.issubset(s2)                                 # O(len(s1))
s1.issuperset({1, 2})                           # O(len(s2))
s1.isdisjoint({7, 8})                           # O(min(len(s1), len(s2)))

# Modify in place
s1.update({5, 6})                               # O(len(s2))
s1.intersection_update(s2)                      # O(len(s1))
```

</details>

<details>
<summary><strong>DefaultDict</strong></summary>

```python
from collections import defaultdict

# With int default
dd = defaultdict(int)
dd['apple'] += 1                                # Missing key initialized to 0, then incremented
print(dd['cherry'])                             # Outputs 0 (default int())

# With list default
dd_list = defaultdict(list)
dd_list['fruits'].append('apple')
dd_list['fruits'].append('banana')
dd_list['vegetables'].append('carrot')
# Result: {'fruits': ['apple', 'banana'], 'vegetables': ['carrot']}

# With custom default
dd_custom = defaultdict(lambda: 100)
dd_custom['exists'] = 1
print(dd_custom['exists'])                      # Outputs 1 (key exists)
print(dd_custom['missing'])                     # Outputs 100 (default factory)

# With set default
dd_set = defaultdict(set)
dd_set['group1'].add('item1')
dd_set['group1'].add('item2')

# Nested defaultdict
nested_dd = defaultdict(lambda: defaultdict(set))
nested_dd['level1']['level2'].add('value')

# 2D defaultdict with boolean default (for visited tracking)
visited_2d = defaultdict(lambda: defaultdict(bool))
visited_2d[row][col] = True                     # Creates nested dict automatically

# Alternative: lambda with specific default
grid_counts = defaultdict(lambda: defaultdict(lambda: 0))
grid_counts[i][j] += 1                          # Auto-initializes to 0

# Graph adjacency with defaultdict
graph = defaultdict(list)
graph[node].append(neighbor)                    # Creates empty list if key missing
```

</details>

<details>
<summary><strong>2D Arrays/Grids</strong></summary>

```python
# Initialize 2D array with specific value
rows, cols = 3, 4
grid = [[0] * cols for _ in range(rows)]        # [[0,0,0,0], [0,0,0,0], [0,0,0,0]]

# Common mistake (creates shared references)
# grid = [[0] * cols] * rows                   # DON'T USE - all rows share same list

# Initialize with different values
grid = [[i * cols + j for j in range(cols)] for i in range(rows)]

# Boolean grid for visited tracking
visited = [[False] * cols for _ in range(rows)]

# Initialize from existing data
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Grid dimensions
rows = len(matrix)
cols = len(matrix[0]) if matrix else 0

# 4-directional movement (up, right, down, left)
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# 8-directional movement (includes diagonals)
directions_8 = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# Check if position is valid
def is_valid(row, col, rows, cols):
    return 0 <= row < rows and 0 <= col < cols

# Grid traversal with bounds checking
for dr, dc in directions:
    new_row, new_col = row + dr, col + dc
    if is_valid(new_row, new_col, rows, cols):
        # Process neighbor
        pass

# Alternative matrix initialization patterns
rows, cols = 3, 3

# Using list comprehension with function calls
import random
random_grid = [[random.randint(1, 10) for _ in range(cols)] for _ in range(rows)]

# Using numpy (if available)  
# import numpy as np
# np_grid = np.zeros((rows, cols))           # All zeros
# np_grid = np.ones((rows, cols))            # All ones  
# np_grid = np.full((rows, cols), 5)         # All fives

# Transpose a matrix
def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# Alternative using zip
def transpose_zip(matrix):
    return list(map(list, zip(*matrix)))
```

</details>

<details>
<summary><strong>LinkedList</strong></summary>

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Basic operations
def append(head, val):
    if not head:
        return ListNode(val)
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = ListNode(val)
    return head

def prepend(head, val):
    return ListNode(val, head)

def delete(head, val):
    if not head:
        return None
    if head.val == val:
        return head.next
    curr = head
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
            break
        curr = curr.next
    return head

# Common patterns
def reverse(head):
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev

def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

</details>

<details>
<summary><strong>Time Complexity Notes</strong></summary>

- **List/Array**:
  - Append: O(1) amortized
  - Insert/Delete at arbitrary index: O(n)
  - Search: O(n)
  - Slice: O(k) where k is the slice size

- **Stack**:
  - Push/Pop: O(1)
  - Peek: O(1)

- **Queue/Deque**:
  - Enqueue/Dequeue: O(1)
  - Peek: O(1)

- **OrderedDict**:
  - Insert/Delete: O(1)
  - Move to end: O(1)
  - Pop first/last: O(1)

- **Set**:
  - Add/Remove: O(1) average, O(n) worst
  - Search: O(1) average, O(n) worst

- **DefaultDict**:
  - Same as dict: O(1) average for insert/delete/search

- **2D Arrays/Grids**:
  - Access: O(1)
  - Traversal: O(rows × cols)

- **LinkedList**:
  - Append/Prepend: O(1)
  - Delete/Insert at arbitrary position: O(n)
  - Search: O(n)
  - Reverse: O(n)

- **Heap/Priority Queue**:
  - Insert: O(log n)
  - Extract min/max: O(log n)
  - Heapify: O(n)

- **SortedSet/SortedDict**:
  - Insert/Delete: O(log n)
  - Search: O(log n)

- **String Operations**:
  - Concatenation: O(n + m) where n, m are lengths
  - Substring: O(k) where k is substring length
  - Split/Join: O(n)

- **Map, Filter, Reduce**:
  - Map/Filter: O(n)
  - Reduce: O(n)

- **Dynamic Programming**:
  - 1D DP: O(n)
  - 2D DP: O(rows × cols)

- **Backtracking**:
  - Time complexity varies, often exponential O(2^n) or O(n!)

- **Advanced Patterns**:
  - Union Find: O(log n) with path compression
  - Monotonic Stack/Queue: O(n)
  - Fast/Slow Pointers: O(n)

</details> 