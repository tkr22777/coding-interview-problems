# Problem Classification Guide

<details>
<summary><strong>🎯 Quick Pattern Recognition</strong></summary>

```python
# 🚀 DECISION FLOWCHART:
# 1. Read constraints → Identify data structure needs
# 2. Analyze input/output → Recognize algorithmic family
# 3. Check edge cases → Confirm approach
# 4. Estimate complexity → Validate solution

# ⏱️ CONSTRAINT-BASED CLASSIFICATION:
# n ≤ 20          → Backtracking, Bit manipulation, Brute force
# n ≤ 100         → O(n³) DP, Floyd-Warshall
# n ≤ 1,000       → O(n²) DP, Nested loops
# n ≤ 100,000     → O(n log n) sorting, Heaps, Binary search
# n ≤ 1,000,000   → O(n) linear scan, Hash maps, Two pointers
# n > 1,000,000   → O(log n) binary search, O(1) math formulas
```

</details>

<details>
<summary><strong>Data Structure Indicators</strong></summary>

```python
# 🔍 PROBLEM STATEMENT → DATA STRUCTURE

# ARRAYS/LISTS:
"subarray", "contiguous", "sliding window" → Array manipulation
"maximum/minimum in range" → Segment tree, Monotonic stack
"k-th largest/smallest" → Heap, QuickSelect

# HASH TABLES:
"count frequency", "find duplicates" → Counter, Set
"two sum", "complement" → Hash map
"group by key" → defaultdict

# TREES:
"binary tree", "ancestor", "path" → Tree traversal
"range queries", "point updates" → Segment tree
"predecessor/successor" → BST, Balanced trees

# GRAPHS:
"connected components", "path finding" → BFS/DFS
"shortest path", "minimum cost" → Dijkstra, BFS
"dependencies", "ordering" → Topological sort

# HEAPS:
"k largest/smallest", "merge streams" → Min/Max heap
"running median" → Two heaps
"schedule tasks" → Priority queue

# LINKED LISTS:
"cycle detection", "middle element" → Fast/slow pointers
"reverse", "merge" → Pointer manipulation
```

</details>

<details>
<summary><strong>Algorithm Family Classification</strong></summary>

```python
# 📊 PROBLEM TYPE → ALGORITHM FAMILY

# OPTIMIZATION PROBLEMS:
"maximum/minimum", "best/optimal" → DP, Greedy
"partition", "subset" → DP
"scheduling", "interval" → Greedy

# SEARCH PROBLEMS:
"find element", "exists" → Binary search, Hash lookup
"all permutations", "all combinations" → Backtracking
"shortest path" → BFS, Dijkstra

# COUNTING PROBLEMS:
"how many ways", "number of paths" → DP
"combinations", "arrangements" → Math, DP

# SORTING/ORDERING:
"sorted order", "rank", "kth element" → Sorting algorithms
"merge", "union" → Merge operations

# PATTERN MATCHING:
"substring", "sequence" → String algorithms
"cycle", "duplicate" → Floyd's algorithm
"anagram", "permutation" → Hash map, sorting

# GEOMETRIC/MATH:
"area", "distance", "coordinates" → Computational geometry
"modular arithmetic", "prime" → Number theory
"probability", "expected value" → Mathematical analysis
```

</details>

<details>
<summary><strong>Quick Decision Rules</strong></summary>

```python
# ⚡ INSTANT ELIMINATIONS:

# NOT GREEDY IF:
- "All possible ways" (→ DP/Backtracking)
- "Optimal substructure" breaks (→ DP)
- Local optimum ≠ global optimum

# NOT DP IF:
- No overlapping subproblems
- Greedy works (interval scheduling)
- Simple linear scan suffices

# NOT BACKTRACKING IF:
- n > 20 (too slow)
- No pruning possible
- DP/Greedy applies

# NOT BFS/DFS IF:
- No graph structure
- Weighted edges (→ Dijkstra)
- Need optimal path count (→ DP)

# STREAMING/WINDOWS IF:
- "Process as data arrives"
- "Sliding window of size k"
- "Running aggregation"
- "Real-time processing"

# INTERVALS IF:
- "Overlapping periods"
- "Merge time ranges"
- "Schedule meetings"
- "Booking conflicts"
```

</details>

<details>
<summary><strong>Problem Statement Patterns</strong></summary>

```python
# 🎪 COMMON PROBLEM FORMATS → SOLUTIONS

# ARRAY PROBLEMS:
"Subarray with sum k" → Prefix sum + Hash map
"Maximum subarray" → Kadane's algorithm
"Rotate array" → Reverse technique
"Two sum" → Hash map, Two pointers

# STRING PROBLEMS:
"Longest substring without repeating" → Sliding window
"Valid parentheses" → Stack
"Anagram groups" → Hash map (sorted chars)
"Palindrome" → Two pointers, DP

# TREE PROBLEMS:
"Lowest common ancestor" → Tree traversal
"Serialize/deserialize" → BFS/DFS
"Path sum" → DFS, Backtracking
"Level order traversal" → BFS

# GRAPH PROBLEMS:
"Number of islands" → DFS/Union-Find
"Word ladder" → BFS
"Course schedule" → Topological sort
"Clone graph" → DFS/BFS

# DYNAMIC PROGRAMMING:
"Climbing stairs" → 1D DP
"Unique paths" → 2D DP
"Coin change" → 1D DP
"Edit distance" → 2D DP

# BACKTRACKING:
"Generate all permutations" → Backtracking
"N-Queens" → Backtracking
"Word search" → DFS + Backtracking
"Sudoku solver" → Constraint satisfaction
```

</details>

<details>
<summary><strong>Advanced Pattern Recognition</strong></summary>

```python
# 🧠 SUBTLE INDICATORS:

# HIDDEN GRAPH PROBLEMS:
"Dependencies between tasks" → Topological sort
"Transform one thing to another" → BFS (shortest path)
"Group similar items" → Union-Find

# DISGUISED DP:
"Minimum operations to reach target" → DP
"Number of ways to decode" → DP
"Maximum profit" → DP

# TWO POINTERS VARIANTS:
"Remove duplicates" → Slow/fast pointers
"Container with most water" → Left/right pointers
"3Sum" → Fixed + two pointers

# STACK/QUEUE USAGE:
"Next greater element" → Monotonic stack
"Valid expression" → Stack matching
"First unique in stream" → Queue + Hash map

# BINARY SEARCH EXTENSIONS:
"Search in rotated array" → Modified binary search
"Find peak element" → Binary search on unimodal
"Minimum in sorted" → Binary search variant

# HEAP APPLICATIONS:
"Merge k sorted lists" → Min heap
"Top k frequent" → Max heap (or min heap of k)
"Meeting rooms" → Min heap (end times)
```

</details>

<details>
<summary><strong>Complexity-Driven Decisions</strong></summary>

```python
# ⚖️ TIME/SPACE TRADE-OFFS:

# WHEN TO USE EXTRA SPACE:
- Hash map for O(1) lookup vs O(n) search
- Memoization for overlapping subproblems
- Auxiliary array for two-pass algorithms

# WHEN TO OPTIMIZE SPACE:
- Input constraints are huge
- Space complexity matters in problem
- In-place modification possible

# ALGORITHM SELECTION BY COMPLEXITY:
# O(1)     → Hash map access, Array index, Math formula
# O(log n) → Binary search, Heap operations, Tree height
# O(n)     → Linear scan, Hash map build, BFS/DFS
# O(n log n) → Sorting, Heap sort, Divide & conquer
# O(n²)    → Nested loops, 2D DP, Graph algorithms
# O(2ⁿ)    → Backtracking, Subset generation

# RED FLAGS FOR OPTIMIZATION:
- Nested loops with independent iterations → Can parallelize
- Repeated calculations → Memoization
- Sorting when only k elements needed → Partial sort/heap
- Full graph traversal when early termination possible → Pruning
```

</details> 