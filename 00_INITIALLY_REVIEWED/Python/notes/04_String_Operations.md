# String Operations

<details>
<summary><strong>Substring</strong></summary>

```python
# Time Complexity:
# - Slicing: O(k) where k is slice length
# - len(): O(1)
# Space Complexity: O(k) for slice where k is slice length

s = "abcd"

# Basic slicing
s[0:2]                                          # "ab"
s[1:]                                           # "bcd" (from index 1 to end)
s[:3]                                           # "abc" (from start to index 3)
s[-1]                                           # "d" (last character)
s[:-1]                                          # "abc" (all but last)
```

</details>

<details>
<summary><strong>Zip</strong></summary>

```python
# Time Complexity:
# - zip(): O(1) for creation, O(n) for iteration
# - list(zip()): O(n) where n is length of shortest sequence
# - dict(zip()): O(n) where n is length of shortest sequence
# Space Complexity: O(n) for storing results

# Basic zipping
list(zip([1, 2, 3], ['a', 'b', 'c']))          # [(1, 'a'), (2, 'b'), (3, 'c')]

# Matrix transpose
list(zip(*[(1, 2, 3), (4, 5, 6)]))             # [(1, 4), (2, 5), (3, 6)]

# Create dictionary from two lists
dict(zip(['name', 'age'], ['Alice', 30]))       # {'name': 'Alice', 'age': 30}

# Unzipping
nums, letters = zip(*[(1, 'a'), (2, 'b')])     # nums=(1,2), letters=('a','b')
```

</details> 