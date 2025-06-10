# Python Data Structures & Libraries - Quick Reference

## Overview
Organized quick reference notes for Python data structures and libraries commonly used in problem-solving interviews. Simple bullet point-based notes designed for software engineers.

## Quick Reference Example
```python
vals = [4, 2, 0, 3, 1]
vals1 = [5, 6, 7, 8, 9]
- sorted(vals) -> [0, 1, 2, 3, 4] (doesn't mutate)
- vals.sort() -> mutates vals to [0, 1, 2, 3, 4]
- sorted(vals) + vals1 -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] (doesn't mutate)
- sorted(vals) == [i - 5 for i in vals1]
```

## Contents

### Data Structures & Libraries
1. **[Data Structures](01_Data_Structures.md)** - List/Array, Stack, Queue, OrderedDict, Set, DefaultDict
2. **[Sorting Operations](02_Sorting_Operations.md)** - Sorting, bisect, sorted containers, heap/priority queue
3. **[Map, Filter & Reduce](03_Map_Filter_Reduce.md)** - Functional programming with shared examples
4. **[String Operations](04_String_Operations.md)** - Substring slicing and zip operations
6. **[LinkedList APIs](06_LinkedList_APIs.md)** - Common LinkedList operations
7. **[Utilities](07_Utilities.md)** - Functions, random, regex, datetime
8. **[Beautiful Soup](08_BeautifulSoup.md)** - HTML parsing and web scraping

### Algorithm Patterns
5. **[Basic Algorithms & Techniques](05_Algorithms_Techniques.md)** - Two pointers, sliding window, tree/graph traversals
9. **[Dynamic Programming](09_Dynamic_Programming.md)** - 1D/2D DP, knapsack patterns
10. **[Backtracking](10_Backtracking.md)** - Permutations, combinations, subsets, grid problems
11. **[Advanced Patterns](11_Advanced_Patterns.md)** - Union Find, monotonic stack/queue, intervals, fast/slow pointers

## Usage
Each file contains practical examples and common patterns for the respective data structure or algorithm. Perfect for quick reference before coding interviews or problem-solving practice.