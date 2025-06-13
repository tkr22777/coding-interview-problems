# Basic Collections

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

# List operations
arr.append(6)                                   # [1, 2, 3, 4, 5, 6]
arr.insert(0, 0)                                # [0, 1, 2, 3, 4, 5, 6] - O(n)
arr.extend([7, 8])                              # [0, 1, 2, 3, 4, 5, 6, 7, 8]
arr.remove(3)                                   # [0, 1, 2, 4, 5, 6, 7, 8] - O(n)
popped = arr.pop()                              # 8, arr becomes [0, 1, 2, 4, 5, 6, 7]
popped_index = arr.pop(2)                       # 2, arr becomes [0, 1, 4, 5, 6, 7] - O(n)

# List comprehensions
squares = [x**2 for x in range(5)]             # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]   # [0, 2, 4, 6, 8]
matrix = [[i*j for j in range(3)] for i in range(3)]  # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]

# Slicing - O(k) where k is slice length
arr = [0, 1, 2, 3, 4, 5]
sub_arr = arr[1:4]                              # [1, 2, 3]
reversed_arr = arr[::-1]                        # [5, 4, 3, 2, 1, 0]
every_second = arr[::2]                         # [0, 2, 4]

# Searching and sorting
arr = [3, 1, 4, 1, 5]
arr.index(4)                                    # 2 - O(n)
arr.count(1)                                    # 2 - O(n)
arr.sort()                                      # [1, 1, 3, 4, 5] - O(n log n)
sorted_arr = sorted(arr, reverse=True)          # [5, 4, 3, 1, 1] - O(n log n)

# Other operations
arr.reverse()                                   # [5, 1, 4, 1, 3] - O(n)
arr.clear()                                     # []

# List as different data structures
# Stack (LIFO)
stack = []
stack.append('a')                               # Stack is now ['a']
stack.append('b')                               # Stack is now ['a', 'b']
stack.append('c')                               # Stack is now ['a', 'b', 'c']
top = stack.pop()                               # 'c', stack is now ['a', 'b']
peek = stack[-1] if stack else None             # 'b' (peek without removing)

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

# With custom default
dd_custom = defaultdict(lambda: 100)
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

# Transpose a matrix
def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

# Alternative using zip
def transpose_zip(matrix):
    return list(map(list, zip(*matrix)))
```

</details> 