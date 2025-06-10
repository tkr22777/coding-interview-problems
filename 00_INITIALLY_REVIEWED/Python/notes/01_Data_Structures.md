# Data Structures

<details>
<summary><strong>List/Array</strong></summary>

```python
arr = [1, 2, 3, 4, 5]

# Basic operations
arr.append(6)                                   # [1, 2, 3, 4, 5, 6]
arr.insert(0, 0)                                # [0, 1, 2, 3, 4, 5, 6]

# Remove operations
arr.remove(3)                                   # [0, 1, 2, 4, 5, 6] (removes first occurrence by value)
popped = arr.pop()                              # 6, arr becomes [0, 1, 2, 4, 5] (removes last)
popped_at = arr.pop(1)                          # 1, arr becomes [0, 2, 4, 5] (removes at index)
del arr[0]                                      # [2, 4, 5] (removes at index, no return)
del arr[1:3]                                    # [2] (removes slice)

# Reverse
arr.reverse()                                   # [5, 4, 2, 0] (in-place)
reversed_arr = arr[::-1]                        # [0, 2, 4, 5] (new list)

# Slicing and copying
first_two = arr[:2]                             # [5, 4]
last_two = arr[-2:]                             # [2, 0]
copy_arr = arr.copy()                           # Shallow copy

# Find and count
index = arr.index(4)                            # 1 (first occurrence)
count = arr.count(2)                            # 1
exists = 4 in arr                               # True

# Extend and clear
arr.extend([1, 2, 3])                           # [5, 4, 2, 0, 1, 2, 3]
arr.clear()                                     # []

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
stack = []
stack.append('a')                               # Stack is now ['a']
stack.append('b')                               # Stack is now ['a', 'b']
stack.append('c')                               # Stack is now ['a', 'b', 'c']

is_empty = not stack                            # Returns False as the stack has elements
size = len(stack)                               # Returns 3
top_item = stack.pop()                          # top_item is 'c', stack is now ['a', 'b']
peek_item = stack[-1]                           # peek_item is 'b' (without removing)

# Remove all items from the stack
while stack:
    item = stack.pop()                          # Removes 'b', then 'a'
```

</details>

<details>
<summary><strong>Queue/Deque</strong></summary>

```python
from collections import deque

# Initialize
d1 = deque([1, 2, 3, 4, 5])

# Add elements
d1.append(6)                                    # Add to right: [1, 2, 3, 4, 5, 6]
d1.appendleft(0)                                # Add to left: [0, 1, 2, 3, 4, 5, 6]

# Remove elements
right_item = d1.pop()                           # Remove from right: 6
left_item = d1.popleft()                        # Remove from left: 0

# Extend
d1.extend([7, 8, 9])                            # Extend right
d1.extendleft([-1, -2, -3])                     # Extend left (order reversed)

# Rotate
d1.rotate(2)                                    # Rotate right by 2 positions
d1.rotate(-1)                                   # Rotate left by 1 position

# Clear
d1.clear()                                      # Remove all elements
```

</details>

<details>
<summary><strong>OrderedDict</strong></summary>

```python
from collections import OrderedDict

od = OrderedDict()
od['a'] = 1                                     # OrderedDict([('a', 1)])
od['b'] = 2                                     # OrderedDict([('a', 1), ('b', 2)])
od['c'] = 3                                     # OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# Access and modify
value = od['a']                                 # value is 1
od['a'] = 4                                     # OrderedDict([('a', 4), ('b', 2), ('c', 3)])
size = len(od)                                  # size = 3

# Check membership
if 'a' in od:
    od['a'] = 6                                 # OrderedDict([('a', 6), ('b', 2), ('c', 3)])

# Move elements
od.move_to_end('a')                             # OrderedDict([('b', 2), ('c', 3), ('a', 6)])
od.move_to_end('b', last=False)                 # OrderedDict([('b', 2), ('c', 3), ('a', 6)])

# Pop operations
key, value = od.popitem()                       # ('a', 6), od becomes [('b', 2), ('c', 3)]
key, value = od.popitem(last=False)             # ('b', 2), od becomes [('c', 3)]

# Peek operations (rebuild for demo)
od = OrderedDict([('x', 10), ('y', 20), ('z', 30)])
key, value = next(iter(od.items()))             # ('x', 10) - peek first
key, value = next(reversed(od.items()))         # ('z', 30) - peek last

# Clear
od.clear()                                      # OrderedDict([])
```

</details>

<details>
<summary><strong>Set</strong></summary>

```python
s = {1, 2, 3}
s.add(4)                                        # s becomes {1, 2, 3, 4}
len(s)                                          # Returns 4
s.discard(2)                                    # Remove element (no error if missing)

# Set operations
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

s1.union(s2)                                    # {1, 2, 3, 4, 5, 6}
s1.intersection(s2)                             # {3, 4}
s1.difference(s2)                               # {1, 2}
s1.symmetric_difference(s2)                     # {1, 2, 5, 6}

# Set comparisons
s1.issubset(s2)                                 # False
s1.issuperset({1, 2})                           # True
s1.isdisjoint({7, 8})                           # True

# Modify in place
s1.update({5, 6})                               # s1 becomes {1, 2, 3, 4, 5, 6}
s1.intersection_update(s2)                      # s1 becomes {3, 4, 5, 6}

# Pop and clear
popped = s1.pop()                               # Remove and return arbitrary element
s1.clear()                                      # Remove all elements
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
```

</details> 