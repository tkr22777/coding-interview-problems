# Map, Filter & Reduce

## Core Concepts
- **map()**: Transform each element in a sequence (built-in)
- **filter()**: Select elements that meet a condition (built-in)
- **reduce()**: Aggregate sequence into a single value (requires import)

```python
from functools import reduce  # Only reduce() needs import

# Shared data for examples
numbers = [1, 2, 3, 4, 5, 6]
strings = ["python", "is", "awesome"]
mixed_data = ['x', 'y', '2', '3', 'z']
```

<details>
<summary><strong>Map Examples</strong></summary>

```python
# Time Complexity:
# - map(): O(n) where n is length of sequence
# - list(map()): O(n) for conversion
# Space Complexity: O(n) for storing results

# Basic transformations
list(map(lambda x: x * 2, numbers))           # [2, 4, 6, 8, 10, 12] - O(n)
list(map(lambda x: x ** 2, numbers))          # [1, 4, 9, 16, 25, 36] - O(n)
list(map(str.upper, strings))                 # ['PYTHON', 'IS', 'AWESOME'] - O(n)

# Multiple sequences
list1, list2 = [1, 2, 3], [4, 5, 6]
list(map(lambda x, y: x + y, list1, list2))   # [5, 7, 9] - O(n)

# Type conversions
str_numbers = ["1", "2", "3", "4"]
list(map(int, str_numbers))                   # [1, 2, 3, 4] - O(n)
list(map(str.title, ["alice", "bob"]))        # ['Alice', 'Bob'] - O(n)
```

</details>

<details>
<summary><strong>Filter Examples</strong></summary>

```python
# Time Complexity:
# - filter(): O(n) where n is length of sequence
# - list(filter()): O(n) for conversion
# Space Complexity: O(n) for storing results

# Basic filtering
list(filter(lambda x: x % 2 == 0, numbers))   # [2, 4, 6] (even numbers) - O(n)
list(filter(lambda x: x > 3, numbers))        # [4, 5, 6] - O(n)
list(filter(str.isalpha, mixed_data))          # ['x', 'y', 'z'] - O(n)

# Class filtering
class Pet:
    def __init__(self, type, name):
        self.type, self.name = type, name

pets = [Pet('dog', 'Rover'), Pet('cat', 'Whiskers'), Pet('dog', 'Fido')]
dogs = list(filter(lambda pet: pet.type == 'dog', pets))  # O(n)
[dog.name for dog in dogs]                    # ['Rover', 'Fido'] - O(n)

# Non-negative numbers
integers = [-10, -7, 1, 2, -3, 0, 4]
list(filter(lambda x: x >= 0, integers))      # [1, 2, 0, 4] - O(n)
```

</details>

<details>
<summary><strong>Reduce Examples</strong></summary>

```python
# Time Complexity:
# - reduce(): O(n) where n is length of sequence
# Space Complexity: O(1) for most operations

# Basic aggregations
reduce(lambda x, y: x + y, numbers)           # 21 (sum) - O(n)
reduce(lambda x, y: x * y, numbers)           # 720 (product) - O(n)
reduce(lambda x, y: x if x > y else y, numbers) # 6 (max) - O(n)

# String operations
reduce(lambda x, y: x + " " + y, strings)     # "python is awesome" - O(n)
chars = ["h", "e", "l", "l", "o"]
reduce(lambda x, y: y + x, chars)             # "olleh" (reverse) - O(n)

# Set operations
sets = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]
reduce(lambda s1, s2: s1 & s2, sets)          # {3} (intersection) - O(n * m) where m is average set size
```

</details>

 