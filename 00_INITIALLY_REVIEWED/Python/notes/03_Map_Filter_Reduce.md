# Map, Filter & Reduce

## Core Concepts
- **map()**: Transform each element in a sequence
- **filter()**: Select elements that meet a condition  
- **reduce()**: Aggregate sequence into a single value

```python
from functools import reduce

# Shared data for examples
numbers = [1, 2, 3, 4, 5, 6]
strings = ["python", "is", "awesome"]
mixed_data = ['x', 'y', '2', '3', 'z']
```

<details>
<summary><strong>Map Examples</strong></summary>

```python
# Basic transformations
list(map(lambda x: x * 2, numbers))           # [2, 4, 6, 8, 10, 12]
list(map(lambda x: x ** 2, numbers))          # [1, 4, 9, 16, 25, 36]
list(map(str.upper, strings))                 # ['PYTHON', 'IS', 'AWESOME']

# Multiple sequences
list1, list2 = [1, 2, 3], [4, 5, 6]
list(map(lambda x, y: x + y, list1, list2))   # [5, 7, 9]

# Type conversions
str_numbers = ["1", "2", "3", "4"]
list(map(int, str_numbers))                   # [1, 2, 3, 4]
list(map(str.title, ["alice", "bob"]))        # ['Alice', 'Bob']
```

</details>

<details>
<summary><strong>Filter Examples</strong></summary>

```python
# Basic filtering
list(filter(lambda x: x % 2 == 0, numbers))   # [2, 4, 6] (even numbers)
list(filter(lambda x: x > 3, numbers))        # [4, 5, 6]
list(filter(str.isalpha, mixed_data))          # ['x', 'y', 'z']

# Class filtering
class Pet:
    def __init__(self, type, name):
        self.type, self.name = type, name

pets = [Pet('dog', 'Rover'), Pet('cat', 'Whiskers'), Pet('dog', 'Fido')]
dogs = list(filter(lambda pet: pet.type == 'dog', pets))
[dog.name for dog in dogs]                    # ['Rover', 'Fido']

# Non-negative numbers
integers = [-10, -7, 1, 2, -3, 0, 4]
list(filter(lambda x: x >= 0, integers))      # [1, 2, 0, 4]
```

</details>

<details>
<summary><strong>Reduce Examples</strong></summary>

```python
# Basic aggregations
reduce(lambda x, y: x + y, numbers)           # 21 (sum)
reduce(lambda x, y: x * y, numbers)           # 720 (product)
reduce(lambda x, y: x if x > y else y, numbers) # 6 (max)

# String operations
reduce(lambda x, y: x + " " + y, strings)     # "python is awesome"
chars = ["h", "e", "l", "l", "o"]
reduce(lambda x, y: y + x, chars)             # "olleh" (reverse)

# Set operations
sets = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]
reduce(lambda s1, s2: s1 & s2, sets)          # {3} (intersection)
```

</details>

 