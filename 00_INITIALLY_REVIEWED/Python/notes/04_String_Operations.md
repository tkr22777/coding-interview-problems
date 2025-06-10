# String Operations

<details>
<summary><strong>Substring</strong></summary>

```python
s = "abcd"

# Basic slicing
print(s[0:0])                                   # "" (empty)
print(s[0:2])                                   # "ab"
print(s[1:2])                                   # "b"
print(s[3:3])                                   # "" (empty)
print(len(s))                                   # 4

# Common patterns
print(s[:])                                     # "abcd" (whole string)
print(s[1:])                                    # "bcd" (from index 1 to end)
print(s[:3])                                    # "abc" (from start to index 3)

# Negative indexing
print(s[-1:])                                   # "d" (last character)
print(s[:-1])                                   # "abc" (all but the last character)
print(s[-2:])                                   # "cd" (last two characters)
print(s[:-2])                                   # "ab" (all but the last two characters)
```

</details>

<details>
<summary><strong>Zip</strong></summary>

```python
# Basic zipping
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))                # [(1, 'a'), (2, 'b'), (3, 'c')]

# Matrix transpose
matrix = [(1, 2, 3), (4, 5, 6)]
transposed = list(zip(*matrix))                 # [(1, 4), (2, 5), (3, 6)]

# Different lengths (stops at shortest)
numbers = [1, 2, 3]
colors = ['red', 'blue']
zipped_short = list(zip(numbers, colors))       # [(1, 'red'), (2, 'blue')]

# Iterating simultaneously
for number, color in zip(numbers, colors):
    print(f'{number} is {color}')               # "1 is red", then "2 is blue"

# Create dictionary from two lists
keys = ['name', 'age']
values = ['Alice', 30]
dictionary = dict(zip(keys, values))           # {'name': 'Alice', 'age': 30}

# Unzipping
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
nums, letters = zip(*pairs)                     # nums=(1,2,3), letters=('a','b','c')
```

</details> 