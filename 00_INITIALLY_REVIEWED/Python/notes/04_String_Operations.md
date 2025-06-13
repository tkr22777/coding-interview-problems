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
print(s[0:0])                                   # "" (empty) - O(1)
print(s[0:2])                                   # "ab" - O(2)
print(s[1:2])                                   # "b" - O(1)
print(s[3:3])                                   # "" (empty) - O(1)
print(len(s))                                   # 4 - O(1)

# Common patterns
print(s[:])                                     # "abcd" (whole string) - O(n)
print(s[1:])                                    # "bcd" (from index 1 to end) - O(n-1)
print(s[:3])                                    # "abc" (from start to index 3) - O(3)

# Negative indexing
print(s[-1:])                                   # "d" (last character) - O(1)
print(s[:-1])                                   # "abc" (all but the last character) - O(n-1)
print(s[-2:])                                   # "cd" (last two characters) - O(2)
print(s[:-2])                                   # "ab" (all but the last two characters) - O(n-2)
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
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))                # [(1, 'a'), (2, 'b'), (3, 'c')] - O(n)

# Matrix transpose
matrix = [(1, 2, 3), (4, 5, 6)]
transposed = list(zip(*matrix))                 # [(1, 4), (2, 5), (3, 6)] - O(n)

# Different lengths (stops at shortest)
numbers = [1, 2, 3]
colors = ['red', 'blue']
zipped_short = list(zip(numbers, colors))       # [(1, 'red'), (2, 'blue')] - O(min(n,m))

# Iterating simultaneously
for number, color in zip(numbers, colors):      # O(n) where n is length of shortest sequence
    print(f'{number} is {color}')               # "1 is red", then "2 is blue"

# Create dictionary from two lists
keys = ['name', 'age']
values = ['Alice', 30]
dictionary = dict(zip(keys, values))           # {'name': 'Alice', 'age': 30} - O(n)

# Unzipping
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
nums, letters = zip(*pairs)                     # nums=(1,2,3), letters=('a','b','c') - O(n)
```

</details> 