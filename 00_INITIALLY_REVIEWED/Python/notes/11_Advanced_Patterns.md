# Advanced Patterns

<details>
<summary><strong>Union Find (Disjoint Set)</strong></summary>

```python
class UnionFind:
    # Problem: Efficiently track connected components and perform union/find operations
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        # Union by rank
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True

# Number of Islands
# Problem: Count number of separate islands in 2D grid of 1s and 0s
def num_islands(grid):
    if not grid:
        return 0
    
    m, n = len(grid), len(grid[0])
    uf = UnionFind(m * n)
    
    def get_index(i, j):
        return i * n + j
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                for di, dj in [(0, 1), (1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == '1':
                        uf.union(get_index(i, j), get_index(ni, nj))
    
    # Count unique roots for all '1' cells
    return len(set(uf.find(get_index(i, j)) 
                  for i in range(m) for j in range(n) 
                  if grid[i][j] == '1'))
```

</details>

<details>
<summary><strong>Monotonic Stack/Queue</strong></summary>

```python
# Daily Temperatures
# Problem: For each day, find how many days until a warmer temperature
def daily_temperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []  # store indices
    
    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        stack.append(i)
    
    return result

# Largest Rectangle in Histogram
# Problem: Find area of largest rectangle that can be formed in histogram
def largest_rectangle_area(heights):
    stack = []
    result = 0
    
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            result = max(result, height * width)
        stack.append(i)
    
    while stack:
        height = heights[stack.pop()]
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        result = max(result, height * width)
    
    return result

# Sliding Window Maximum
# Problem: Find maximum element in each sliding window of size k
from collections import deque

def max_sliding_window(nums, k):
    result = []
    dq = deque()  # store indices in decreasing order of values
    
    for i, num in enumerate(nums):
        # Remove indices outside window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove smaller elements
        while dq and nums[dq[-1]] < num:
            dq.pop()
        
        dq.append(i)
        
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result
```

</details>

<details>
<summary><strong>Interval Problems</strong></summary>

```python
# Merge Intervals
# Problem: Merge overlapping intervals in a list of intervals
def merge(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    
    return merged

# Insert Interval
# Problem: Insert new interval into sorted non-overlapping intervals list
def insert(intervals, newInterval):
    result = []
    i = 0
    
    # Add all intervals before newInterval
    while i < len(intervals) and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
    
    # Merge overlapping intervals
    while i < len(intervals) and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1
    
    result.append(newInterval)
    
    # Add remaining intervals
    while i < len(intervals):
        result.append(intervals[i])
        i += 1
    
    return result

# Non-overlapping Intervals
# Problem: Find minimum number of intervals to remove to make rest non-overlapping
def erase_overlap_intervals(intervals):
    if not intervals:
        return 0
    
    intervals.sort(key=lambda x: x[1])  # sort by end time
    end = intervals[0][1]
    count = 0
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:
            count += 1
        else:
            end = intervals[i][1]
    
    return count
```

</details>

<details>
<summary><strong>Fast & Slow Pointers</strong></summary>

```python
# Linked List Cycle
# Problem: Detect if linked list has a cycle
def has_cycle(head):
    if not head or not head.next:
        return False
    
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False

# Find Duplicate Number
# Problem: Find duplicate number in array containing n+1 integers from 1 to n
def find_duplicate(nums):
    # Treat array as linked list where nums[i] points to nums[nums[i]]
    slow = fast = nums[0]
    
    # Find intersection point in cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # Find entrance to cycle (duplicate number)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow

# Happy Number
# Problem: Determine if number eventually reaches 1 when replaced by sum of squares of digits
def is_happy(n):
    def get_sum_of_squares(num):
        total = 0
        while num:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total
    
    slow = fast = n
    while True:
        slow = get_sum_of_squares(slow)
        fast = get_sum_of_squares(get_sum_of_squares(fast))
        
        if fast == 1:
            return True
        if slow == fast:
            return False
```

</details> 