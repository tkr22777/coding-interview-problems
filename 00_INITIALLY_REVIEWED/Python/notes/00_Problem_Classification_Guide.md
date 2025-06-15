# Problem Classification Guide

<details>
<summary><strong>🎯 Step-by-Step Problem Identification</strong></summary>

```python
# 🚀 4-STEP DECISION PROCESS:
# Step 1: Read constraints → Rule out slow approaches
# Step 2: Identify keywords → Match to algorithm families  
# Step 3: Check problem structure → Confirm approach
# Step 4: Look for edge cases → Validate choice

# ⏱️ CONSTRAINT-BASED ELIMINATION:
# n ≤ 20          → Backtracking, Bit manipulation OK
# n ≤ 1,000       → Nested loops, DP OK
# n ≤ 100,000     → Sorting, Heaps, Binary search OK
# n ≤ 1,000,000   → Hash maps, Two pointers OK
# n > 1,000,000   → Only very efficient algorithms

# 🔍 STEP 1: QUICK SIZE CHECK
# Small n (≤20) → Try everything approaches work
# Medium n (≤100K) → Standard algorithms work  
# Large n (>100K) → Need very efficient approaches
```

</details>

<details>
<summary><strong>STEP 2: Keyword → Algorithm Mapping</strong></summary>

```python
# 🔍 KEYWORD DETECTION → ALGORITHM CHOICE

# ARRAYS/LISTS KEYWORDS:
"subarray", "contiguous" → Sliding window, Prefix sum
"maximum/minimum in range" → Monotonic stack/queue
"k-th largest/smallest" → Heap, QuickSelect
"rotate", "reverse" → Array manipulation

# HASH TABLE KEYWORDS:
"count frequency", "find duplicates" → Counter, Set
"two sum", "complement", "pair" → Hash map
"group by", "anagram" → defaultdict, grouping

# TREE KEYWORDS:
"binary tree", "ancestor", "path" → Tree traversal (DFS/BFS)
"level order", "breadth first" → BFS
"depth first", "pre/in/post order" → DFS

# GRAPH KEYWORDS:
"connected components", "islands" → DFS/Union-Find
"shortest path", "minimum steps" → BFS, Dijkstra
"dependencies", "prerequisites" → Topological sort
"clone", "copy" → Graph traversal

# SPECIAL PATTERNS:
"running median", "data stream" → Two heaps
"merge k sorted" → Min heap
"cycle detection" → Fast/slow pointers
"valid parentheses" → Stack
```

</details>

<details>
<summary><strong>STEP 3: Problem Structure Recognition</strong></summary>

```python
# 📊 PROBLEM STRUCTURE → ALGORITHM FAMILY

# OPTIMIZATION PROBLEMS:
"maximum/minimum", "best/optimal" → DP or Greedy
"partition", "subset" → DP
"scheduling", "interval merging" → Greedy

# SEARCH PROBLEMS:
"find element", "exists" → Binary search, Hash lookup
"all permutations", "all combinations" → Backtracking
"shortest path", "minimum steps" → BFS, Dijkstra

# COUNTING PROBLEMS:
"how many ways", "number of paths" → DP
"combinations", "arrangements" → Math or DP

# EXPLORATION PROBLEMS:
"connected components", "islands", "regions" → DFS/BFS
"flood fill", "paint bucket" → DFS
"shortest path in grid" → BFS

# PATTERN MATCHING:
"substring", "sequence" → String algorithms
"anagram", "permutation" → Hash map, sorting
"cycle", "duplicate" → Floyd's algorithm

# CONSTRUCTION PROBLEMS:
"build tree from traversal" → Tree construction
"serialize/deserialize" → Encoding/decoding
"merge data structures" → Merge algorithms
```

</details>

<details>
<summary><strong>STEP 4: Quick Elimination Rules</strong></summary>

```python
# ⚡ RULE OUT WRONG APPROACHES:

# DON'T USE GREEDY IF:
- Problem asks "all possible ways" → Use DP/Backtracking instead
- Local optimal ≠ global optimal → Use DP instead
- Need to consider all combinations → Use Backtracking instead

# DON'T USE DP IF:
- Simple linear scan works → Use straightforward approach
- Greedy clearly works → Use Greedy (interval scheduling)
- No repeated subproblems → Use direct algorithm

# DON'T USE BACKTRACKING IF:
- n > 20 (too slow) → Use DP or other approach
- No pruning possible → Will timeout
- Pattern fits DP/Greedy → Use those instead

# USE STREAMING/WINDOWS IF:
- "Process as data arrives"
- "Sliding window of size k"  
- "Running aggregation"
- "Online algorithm"

# USE GRID EXPLORATION IF:
- "2D matrix", "grid", "board"
- "Connected regions", "islands"
- "Flood fill", "paint bucket"
- "Shortest path in maze"
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
<summary><strong>Tricky Pattern Recognition</strong></summary>

```python
# 🧠 DISGUISED PROBLEMS:

# HIDDEN GRAPH PROBLEMS:
"Dependencies between tasks" → Topological sort
"Transform one thing to another" → BFS (shortest path)
"Group similar items" → Union-Find
"Word ladder", "gene mutation" → BFS on state space

# DISGUISED DP:
"Minimum operations to reach target" → DP
"Number of ways to decode/arrange" → DP
"Maximum profit with constraints" → DP
"Optimal strategy games" → DP

# TWO POINTERS VARIANTS:
"Remove duplicates" → Slow/fast pointers
"Container with most water" → Left/right pointers
"3Sum, 4Sum" → Fixed + two pointers
"Merge sorted arrays" → Two pointers

# STACK/QUEUE PATTERNS:
"Next greater/smaller element" → Monotonic stack
"Valid expression matching" → Stack
"First unique in stream" → Queue + Hash map
"Sliding window maximum" → Deque

# BINARY SEARCH EXTENSIONS:
"Search in rotated array" → Modified binary search
"Find peak element" → Binary search on unimodal
"Square root, power" → Binary search on answer
"Minimum in sorted" → Binary search variant
```

</details> 