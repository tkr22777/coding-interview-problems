# Advanced Patterns

<details>
<summary><strong>💡 Advanced Patterns Best Practices & Common Pitfalls</strong></summary>

```python
# 🚨 COMMON PITFALLS TO AVOID:
# 1. Union-Find: Forgetting path compression or union by rank
# 2. Monotonic Stack: Not understanding when to use increasing vs decreasing
# 3. Intervals: Not sorting by the right criteria (start vs end time)
# 4. Fast/Slow Pointers: Off-by-one errors in cycle detection
# 5. Sliding Window: Not handling edge cases (empty arrays, k > n)

# ✅ BEST PRACTICES:
# 1. Union-Find: Always implement both optimizations (path compression + union by rank)
# 2. Monotonic Stack: Think about what you're trying to find (next greater/smaller)
# 3. Intervals: Draw timeline diagrams to visualize overlaps
# 4. Two Pointers: Consider if array needs to be sorted first
# 5. Pattern Recognition: Many problems have multiple solution approaches

# 🎯 WHEN TO USE EACH PATTERN:
# - Union-Find: Connected components, cycle detection in undirected graphs
# - Monotonic Stack: Next greater/smaller element problems
# - Intervals: Scheduling, merging, overlapping problems
# - Fast/Slow Pointers: Cycle detection, finding middle element
# - Sliding Window: Subarray/substring problems with constraints
```

</details>

<details>
<summary><strong>Union Find (Disjoint Set)</strong></summary>

```python
# Time Complexity: O(α(n)) per operation where α is inverse Ackermann function (practically O(1))
# Space Complexity: O(n)

class UnionFind:
    # Problem: Efficiently track connected components and perform union/find operations
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n  # 🚀 OPTIMIZATION: Track number of components
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # Already connected
        
        # Union by rank - 🚨 CRITICAL for efficiency
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        
        self.components -= 1  # 🚀 OPTIMIZATION: Update component count
        return True
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def get_components(self):
        return self.components

# 🚨 COMMON MISTAKE: Basic Union-Find without optimizations
class UnionFindBasic:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        # ❌ NO PATH COMPRESSION - O(n) worst case
        while self.parent[x] != x:
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            # ❌ NO UNION BY RANK - can create long chains
            self.parent[px] = py

# Number of Islands (Union-Find approach)
# Problem: Count number of separate islands in 2D grid of 1s and 0s
def num_islands_uf(grid):
    if not grid:
        return 0
    
    m, n = len(grid), len(grid[0])
    uf = UnionFind(m * n)
    
    def get_index(i, j):
        return i * n + j
    
    # Count initial islands (all '1' cells are separate components)
    islands = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                islands += 1
    
    # Union adjacent '1' cells
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                for di, dj in [(0, 1), (1, 0)]:  # Only check right and down
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == '1':
                        if uf.union(get_index(i, j), get_index(ni, nj)):
                            islands -= 1  # Two islands merged into one
    
    return islands

# 💡 INSIGHT: Union-Find vs DFS for islands
# - DFS: O(m*n) time, O(m*n) space (recursion stack)
# - Union-Find: O(m*n*α(m*n)) time, O(m*n) space
# - DFS is usually simpler and faster for this specific problem
```

</details>

<details>
<summary><strong>Monotonic Stack/Queue</strong></summary>

```python
# Time Complexity: O(n) for most monotonic stack problems
# Space Complexity: O(n) for the stack

# 🧠 KEY INSIGHT: Monotonic stack helps find "next greater/smaller" efficiently
# - Increasing stack: Find next smaller element
# - Decreasing stack: Find next greater element

# Daily Temperatures
# Problem: For each day, find how many days until a warmer temperature
def daily_temperatures(temperatures):
    result = [0] * len(temperatures)
    stack = []  # store indices, maintain decreasing order of temperatures
    
    for i, temp in enumerate(temperatures):
        # While current temp is warmer than stack top
        while stack and temperatures[stack[-1]] < temp:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        stack.append(i)
    
    return result

# 💡 INSIGHT: We use decreasing stack because we want "next greater"
# Stack stores indices of temperatures in decreasing order

# Next Greater Element
# Problem: Find next greater element for each element in array
def next_greater_elements(nums):
    n = len(nums)
    result = [-1] * n
    stack = []  # decreasing stack
    
    # 🚀 TRICK: Process array twice for circular array
    for i in range(2 * n):
        while stack and nums[stack[-1]] < nums[i % n]:
            result[stack.pop()] = nums[i % n]
        if i < n:  # Only add indices in first pass
            stack.append(i)
    
    return result

# Largest Rectangle in Histogram
# Problem: Find area of largest rectangle that can be formed in histogram
def largest_rectangle_area(heights):
    stack = []  # increasing stack (store indices)
    result = 0
    
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            # Width calculation is tricky - be careful!
            width = i if not stack else i - stack[-1] - 1
            result = max(result, height * width)
        stack.append(i)
    
    # Process remaining elements in stack
    while stack:
        height = heights[stack.pop()]
        width = len(heights) if not stack else len(heights) - stack[-1] - 1
        result = max(result, height * width)
    
    return result

# 🚨 COMMON MISTAKE: Wrong width calculation
# Correct width = right_boundary - left_boundary - 1
# When stack is empty, left_boundary = -1 (implicit)

# Sliding Window Maximum
# Problem: Find maximum element in each sliding window of size k
from collections import deque

def max_sliding_window(nums, k):
    result = []
    dq = deque()  # store indices in decreasing order of values
    
    for i, num in enumerate(nums):
        # Remove indices outside current window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove smaller elements (they can never be maximum)
        while dq and nums[dq[-1]] < num:
            dq.pop()
        
        dq.append(i)
        
        # Add to result when window is complete
        if i >= k - 1:
            result.append(nums[dq[0]])  # Front of deque is maximum
    
    return result

# 💡 INSIGHT: Deque maintains potential maximums in decreasing order
# Front of deque is always the maximum of current window

# 🚀 ALTERNATIVE: Using monotonic stack for preprocessing
def max_sliding_window_preprocess(nums, k):
    n = len(nums)
    left = [0] * n   # left[i] = max in block ending at i
    right = [0] * n  # right[i] = max in block starting at i
    
    # Divide array into blocks of size k
    for i in range(n):
        if i % k == 0:
            left[i] = nums[i]
        else:
            left[i] = max(left[i-1], nums[i])
    
    for i in range(n-1, -1, -1):
        if i == n-1 or (i+1) % k == 0:
            right[i] = nums[i]
        else:
            right[i] = max(right[i+1], nums[i])
    
    result = []
    for i in range(n-k+1):
        # Maximum in window [i, i+k-1] is max(right[i], left[i+k-1])
        result.append(max(right[i], left[i+k-1]))
    
    return result
```

</details>

<details>
<summary><strong>Interval Problems</strong></summary>

```python
# Time Complexity: O(n log n) for sorting + O(n) for processing
# Space Complexity: O(n) for result

# 🎯 INTERVAL PROBLEM PATTERNS:
# 1. Merge overlapping intervals
# 2. Insert new interval
# 3. Remove minimum intervals to make non-overlapping
# 4. Find maximum non-overlapping intervals

# Merge Intervals
# Problem: Merge overlapping intervals in a list of intervals
def merge(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])  # Sort by start time
    merged = [intervals[0]]
    
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:  # Overlapping
            merged[-1][1] = max(merged[-1][1], end)  # Merge
        else:
            merged.append([start, end])  # Non-overlapping
    
    return merged

# 💡 INSIGHT: Always sort by start time for merging problems
# Key condition: start <= last_end means overlapping

# Insert Interval
# Problem: Insert new interval into sorted non-overlapping intervals list
def insert(intervals, newInterval):
    result = []
    i = 0
    
    # Add all intervals that end before newInterval starts
    while i < len(intervals) and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1
    
    # Merge all overlapping intervals with newInterval
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

# 🚨 COMMON MISTAKE: Wrong overlap condition
# Correct: intervals[i][0] <= newInterval[1] (start <= end)
# Wrong: intervals[i][0] < newInterval[1] (misses touching intervals)

# Non-overlapping Intervals
# Problem: Find minimum number of intervals to remove to make rest non-overlapping
def erase_overlap_intervals(intervals):
    if not intervals:
        return 0
    
    # 🚀 KEY INSIGHT: Sort by END time, not start time!
    intervals.sort(key=lambda x: x[1])
    end = intervals[0][1]
    count = 0
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < end:  # Overlapping
            count += 1  # Remove current interval
        else:
            end = intervals[i][1]  # Update end time
    
    return count

# 💡 INSIGHT: Greedy approach - always keep interval with earliest end time
# This leaves maximum room for future intervals

# Meeting Rooms II
# Problem: Find minimum number of meeting rooms required
def min_meeting_rooms(intervals):
    if not intervals:
        return 0
    
    # Separate start and end times
    starts = sorted([interval[0] for interval in intervals])
    ends = sorted([interval[1] for interval in intervals])
    
    rooms = 0
    end_ptr = 0
    
    for start in starts:
        if start >= ends[end_ptr]:
            end_ptr += 1  # A meeting ended, room available
        else:
            rooms += 1    # Need new room
    
    return rooms

# 🚀 ALTERNATIVE: Using heap (more intuitive)
import heapq

def min_meeting_rooms_heap(intervals):
    if not intervals:
        return 0
    
    intervals.sort(key=lambda x: x[0])  # Sort by start time
    heap = []  # Min heap of end times
    
    for start, end in intervals:
        if heap and start >= heap[0]:
            heapq.heappop(heap)  # Room becomes available
        heapq.heappush(heap, end)
    
    return len(heap)  # Number of rooms needed

# 💡 INSIGHT: Two approaches for meeting rooms:
# 1. Two pointers on sorted start/end times (more efficient)
# 2. Heap to track end times (more intuitive)
```

</details>

<details>
<summary><strong>Fast & Slow Pointers</strong></summary>

```python
# Time Complexity: O(n) for most two-pointer problems
# Space Complexity: O(1)

# 🧠 KEY INSIGHT: Fast/slow pointers detect cycles and find middle elements
# Fast moves 2 steps, slow moves 1 step - they meet if there's a cycle

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

# 💡 INSIGHT: If there's a cycle, fast will eventually catch up to slow
# Think of it as two runners on a circular track

# Find Cycle Start
# Problem: Find the node where cycle begins
def detect_cycle(head):
    if not head or not head.next:
        return None
    
    # Phase 1: Detect if cycle exists
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # No cycle
    
    # Phase 2: Find cycle start
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next  # Move fast by 1 step now!
    
    return slow

# 🧠 MATHEMATICAL INSIGHT: Why does this work?
# If cycle starts at distance 'a' from head and has length 'c':
# When they meet, slow traveled 'a + b', fast traveled 'a + b + c'
# Since fast = 2 * slow: a + b + c = 2(a + b) → c = a + b
# So distance from head to cycle start = distance from meeting point to cycle start

# Find Duplicate Number
# Problem: Find duplicate number in array containing n+1 integers from 1 to n
def find_duplicate(nums):
    # 🚀 INSIGHT: Treat array as linked list where nums[i] points to nums[nums[i]]
    slow = fast = nums[0]
    
    # Phase 1: Find intersection point in cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # Phase 2: Find entrance to cycle (duplicate number)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow

# 💡 INSIGHT: This is Floyd's cycle detection applied to arrays!
# The duplicate number is the "cycle start" in the implicit linked list

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
        if slow == fast:  # Cycle detected, not happy
            return False

# 🚨 ALTERNATIVE: Using set (sometimes clearer)
def is_happy_set(n):
    def get_sum_of_squares(num):
        total = 0
        while num:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total
    
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_sum_of_squares(n)
    
    return n == 1

# Find Middle of Linked List
# Problem: Find middle node of linked list
def find_middle(head):
    if not head:
        return None
    
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow  # slow is at middle when fast reaches end

# 💡 INSIGHT: When fast reaches end, slow is at middle
# For even length: returns second middle node
# For odd length: returns exact middle node

# 🚀 VARIATION: Find middle and split list
def split_list(head):
    if not head or not head.next:
        return head, None
    
    slow = fast = head
    prev = None
    
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    prev.next = None  # Split the list
    return head, slow  # Return both halves
```

</details>

<details>
<summary><strong>Segment Tree</strong></summary>

```python
# Time Complexity:
# - Build: O(n)
# - Query: O(log n)
# - Update: O(log n)
# Space Complexity: O(n)

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)  # 4*n is safe upper bound
        self.build(arr, 0, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        """Build segment tree - O(n)"""
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2*node+1, start, mid)
            self.build(arr, 2*node+2, mid+1, end)
            self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]
    
    def update(self, node, start, end, idx, val):
        """Update single element - O(log n)"""
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(2*node+1, start, mid, idx, val)
            else:
                self.update(2*node+2, mid+1, end, idx, val)
            self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]
    
    def query(self, node, start, end, l, r):
        """Range sum query - O(log n)"""
        if r < start or end < l:
            return 0  # No overlap
        if l <= start and end <= r:
            return self.tree[node]  # Complete overlap
        
        # Partial overlap
        mid = (start + end) // 2
        left_sum = self.query(2*node+1, start, mid, l, r)
        right_sum = self.query(2*node+2, mid+1, end, l, r)
        return left_sum + right_sum
    
    def update_point(self, idx, val):
        """Public interface for point update"""
        self.update(0, 0, self.n-1, idx, val)
    
    def range_sum(self, l, r):
        """Public interface for range query"""
        return self.query(0, 0, self.n-1, l, r)

# Range Minimum Query (RMQ) Segment Tree
class RMQSegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [float('inf')] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2*node+1, start, mid)
            self.build(arr, 2*node+2, mid+1, end)
            self.tree[node] = min(self.tree[2*node+1], self.tree[2*node+2])
    
    def update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(2*node+1, start, mid, idx, val)
            else:
                self.update(2*node+2, mid+1, end, idx, val)
            self.tree[node] = min(self.tree[2*node+1], self.tree[2*node+2])
    
    def query(self, node, start, end, l, r):
        if r < start or end < l:
            return float('inf')
        if l <= start and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_min = self.query(2*node+1, start, mid, l, r)
        right_min = self.query(2*node+2, mid+1, end, l, r)
        return min(left_min, right_min)
    
    def update_point(self, idx, val):
        self.update(0, 0, self.n-1, idx, val)
    
    def range_min(self, l, r):
        return self.query(0, 0, self.n-1, l, r)

# Lazy Propagation Segment Tree (for range updates)
class LazySegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2*node+1, start, mid)
            self.build(arr, 2*node+2, mid+1, end)
            self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]
    
    def push(self, node, start, end):
        """Push lazy value down"""
        if self.lazy[node] != 0:
            self.tree[node] += self.lazy[node] * (end - start + 1)
            if start != end:  # Not a leaf
                self.lazy[2*node+1] += self.lazy[node]
                self.lazy[2*node+2] += self.lazy[node]
            self.lazy[node] = 0
    
    def update_range(self, node, start, end, l, r, val):
        """Range update with lazy propagation - O(log n)"""
        self.push(node, start, end)
        if start > r or end < l:
            return
        
        if start >= l and end <= r:
            self.lazy[node] += val
            self.push(node, start, end)
            return
        
        mid = (start + end) // 2
        self.update_range(2*node+1, start, mid, l, r, val)
        self.update_range(2*node+2, mid+1, end, l, r, val)
        
        self.push(2*node+1, start, mid)
        self.push(2*node+2, mid+1, end)
        self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]
    
    def query_range(self, node, start, end, l, r):
        """Range query with lazy propagation - O(log n)"""
        if start > r or end < l:
            return 0
        
        self.push(node, start, end)
        if start >= l and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_sum = self.query_range(2*node+1, start, mid, l, r)
        right_sum = self.query_range(2*node+2, mid+1, end, l, r)
        return left_sum + right_sum
    
    def update(self, l, r, val):
        """Public interface for range update"""
        self.update_range(0, 0, self.n-1, l, r, val)
    
    def query(self, l, r):
        """Public interface for range query"""
        return self.query_range(0, 0, self.n-1, l, r)

# Examples
arr = [1, 3, 5, 7, 9, 11]
seg_tree = SegmentTree(arr)

seg_tree.range_sum(1, 3)                       # 15 (3 + 5 + 7) - O(log n)
seg_tree.update_point(1, 10)                   # Update arr[1] to 10 - O(log n)
seg_tree.range_sum(1, 3)                       # 22 (10 + 5 + 7) - O(log n)

# RMQ example
rmq_tree = RMQSegmentTree(arr)
rmq_tree.range_min(1, 4)                       # 3 (minimum in range [1,4]) - O(log n)
```

</details>

<details>
<summary><strong>Fenwick Tree (Binary Indexed Tree)</strong></summary>

```python
# Time Complexity:
# - Build: O(n log n) or O(n) with optimized construction
# - Update: O(log n)
# - Query: O(log n)
# Space Complexity: O(n)

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)  # 1-indexed for easier bit manipulation
    
    def update(self, idx, delta):
        """Add delta to element at index idx (1-indexed) - O(log n)"""
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & (-idx)  # Add last set bit
    
    def prefix_sum(self, idx):
        """Get sum of elements from 1 to idx (inclusive) - O(log n)"""
        result = 0
        while idx > 0:
            result += self.tree[idx]
            idx -= idx & (-idx)  # Remove last set bit
        return result
    
    def range_sum(self, left, right):
        """Get sum of elements from left to right (inclusive, 1-indexed) - O(log n)"""
        return self.prefix_sum(right) - self.prefix_sum(left - 1)
    
    def point_update(self, idx, new_val, old_val):
        """Update element at idx to new_val (given old_val) - O(log n)"""
        self.update(idx, new_val - old_val)

# Optimized construction from array
class FenwickTreeFromArray:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (self.n + 1)
        
        # Method 1: O(n log n) construction
        # for i, val in enumerate(arr):
        #     self.update(i + 1, val)
        
        # Method 2: O(n) construction
        for i in range(1, self.n + 1):
            self.tree[i] += arr[i - 1]
            j = i + (i & -i)
            if j <= self.n:
                self.tree[j] += self.tree[i]
    
    def update(self, idx, delta):
        """Add delta to element at index idx (1-indexed) - O(log n)"""
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & (-idx)
    
    def prefix_sum(self, idx):
        """Get sum of elements from 1 to idx (inclusive) - O(log n)"""
        result = 0
        while idx > 0:
            result += self.tree[idx]
            idx -= idx & (-idx)
        return result
    
    def range_sum(self, left, right):
        """Get sum of elements from left to right (inclusive, 1-indexed) - O(log n)"""
        return self.prefix_sum(right) - self.prefix_sum(left - 1)

# 2D Fenwick Tree for matrix range sum queries
class FenwickTree2D:
    def __init__(self, m, n):
        self.m, self.n = m, n
        self.tree = [[0] * (n + 1) for _ in range(m + 1)]
    
    def update(self, row, col, delta):
        """Add delta to element at (row, col) - O(log m * log n)"""
        i = row
        while i <= self.m:
            j = col
            while j <= self.n:
                self.tree[i][j] += delta
                j += j & (-j)
            i += i & (-i)
    
    def prefix_sum(self, row, col):
        """Get sum of rectangle from (1,1) to (row,col) - O(log m * log n)"""
        result = 0
        i = row
        while i > 0:
            j = col
            while j > 0:
                result += self.tree[i][j]
                j -= j & (-j)
            i -= i & (-i)
        return result
    
    def range_sum(self, row1, col1, row2, col2):
        """Get sum of rectangle from (row1,col1) to (row2,col2) - O(log m * log n)"""
        return (self.prefix_sum(row2, col2) 
                - self.prefix_sum(row1 - 1, col2)
                - self.prefix_sum(row2, col1 - 1)
                + self.prefix_sum(row1 - 1, col1 - 1))

# Practical applications
# 1. Count inversions in array
def count_inversions(arr):
    """Count number of inversions using Fenwick Tree - O(n log n)"""
    # Coordinate compression
    sorted_vals = sorted(set(arr))
    val_to_idx = {val: i + 1 for i, val in enumerate(sorted_vals)}
    
    ft = FenwickTree(len(sorted_vals))
    inversions = 0
    
    for i in range(len(arr) - 1, -1, -1):
        idx = val_to_idx[arr[i]]
        # Count elements smaller than current element that come after it
        inversions += ft.prefix_sum(idx - 1)
        ft.update(idx, 1)
    
    return inversions

# 2. Range sum with updates (mutable array)
class NumArray:
    def __init__(self, nums):
        self.nums = nums[:]
        self.ft = FenwickTreeFromArray(nums)
    
    def update(self, index, val):
        """Update nums[index] to val - O(log n)"""
        old_val = self.nums[index]
        self.nums[index] = val
        self.ft.update(index + 1, val - old_val)  # Convert to 1-indexed
    
    def sumRange(self, left, right):
        """Sum of elements from left to right - O(log n)"""
        return self.ft.range_sum(left + 1, right + 1)  # Convert to 1-indexed

# Examples
arr = [1, 3, 5, 7, 9, 11]
ft = FenwickTreeFromArray(arr)

ft.prefix_sum(3)                                # 9 (1 + 3 + 5) - O(log n)
ft.range_sum(2, 4)                              # 15 (3 + 5 + 7) - O(log n)
ft.update(2, 2)                                 # Add 2 to arr[1] (3 -> 5) - O(log n)
ft.range_sum(2, 4)                              # 17 (5 + 5 + 7) - O(log n)

# Count inversions example
inversions = count_inversions([2, 3, 8, 6, 1])  # 5 inversions - O(n log n)

# 💡 INSIGHT: Fenwick Tree vs Segment Tree
# Fenwick Tree:
# - Simpler implementation
# - Only supports commutative operations (sum, XOR)
# - Slightly better constants
# - Prefix queries are natural

# Segment Tree:
# - More flexible (min, max, GCD, etc.)
# - Range updates with lazy propagation
# - Can handle non-commutative operations
# - More memory usage
```

</details> 