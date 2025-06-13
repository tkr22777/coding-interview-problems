# Union Find & Monotonic Patterns

<details>
<summary><strong>💡 Pattern Best Practices</strong></summary>

```python
# 🚨 COMMON PITFALLS TO AVOID:
# 1. Union-Find: Forgetting path compression or union by rank
# 2. Monotonic Stack: Not understanding when to use increasing vs decreasing
# 3. Fast/Slow Pointers: Off-by-one errors in cycle detection

# ✅ BEST PRACTICES:
# 1. Union-Find: Always implement both optimizations (path compression + union by rank)
# 2. Monotonic Stack: Think about what you're trying to find (next greater/smaller)
# 3. Pattern Recognition: Many problems have multiple solution approaches

# 🎯 WHEN TO USE EACH PATTERN:
# - Union-Find: Connected components, cycle detection in undirected graphs
# - Monotonic Stack: Next greater/smaller element problems
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

# Graph Valid Tree
def valid_tree(n, edges):
    """Check if edges form a valid tree with n nodes"""
    if len(edges) != n - 1:  # Tree must have exactly n-1 edges
        return False
    
    uf = UnionFind(n)
    for u, v in edges:
        if not uf.union(u, v):  # Cycle detected
            return False
    
    return uf.get_components() == 1  # Must be connected

# Accounts Merge
def accounts_merge(accounts):
    """Merge accounts that belong to same person based on common emails"""
    from collections import defaultdict
    
    email_to_name = {}
    email_to_id = {}
    
    # Assign unique ID to each email
    email_id = 0
    for account in accounts:
        name = account[0]
        for email in account[1:]:
            if email not in email_to_id:
                email_to_id[email] = email_id
                email_to_name[email] = name
                email_id += 1
    
    uf = UnionFind(email_id)
    
    # Union emails within same account
    for account in accounts:
        first_email = account[1]
        first_id = email_to_id[first_email]
        
        for email in account[2:]:
            uf.union(first_id, email_to_id[email])
    
    # Group emails by root parent
    groups = defaultdict(list)
    for email, email_id in email_to_id.items():
        root = uf.find(email_id)
        groups[root].append(email)
    
    # Format result
    result = []
    for emails in groups.values():
        emails.sort()
        name = email_to_name[emails[0]]
        result.append([name] + emails)
    
    return result
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
def sliding_window_maximum(nums, k):
    from collections import deque
    
    dq = deque()  # store indices, maintain decreasing order of values
    result = []
    
    for i, num in enumerate(nums):
        # Remove indices outside current window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Remove smaller elements from back (they can't be maximum)
        while dq and nums[dq[-1]] < num:
            dq.pop()
        
        dq.append(i)
        
        # Add maximum to result (front of deque)
        if i >= k - 1:
            result.append(nums[dq[0]])
    
    return result

# 💡 INSIGHT: Deque maintains potential maximums in decreasing order
# Front of deque is always the maximum of current window

# 🚀 ALTERNATIVE: Using monotonic stack for preprocessing
def sliding_window_maximum_preprocess(nums, k):
    """Alternative approach using monotonic stack preprocessing"""
    n = len(nums)
    
    # Precompute next greater element for each position
    next_greater = [n] * n
    stack = []
    
    for i in range(n):
        while stack and nums[stack[-1]] < nums[i]:
            next_greater[stack.pop()] = i
        stack.append(i)
    
    result = []
    for i in range(n - k + 1):
        # Find maximum in window [i, i+k-1]
        max_val = nums[i]
        j = i
        while j < i + k:
            max_val = max(max_val, nums[j])
            # Jump to next potentially larger element
            if next_greater[j] < i + k:
                j = next_greater[j]
            else:
                break
        result.append(max_val)
    
    return result

# Remove K Digits
# Problem: Remove k digits from number to make smallest possible number
def remove_k_digits(num, k):
    stack = []  # increasing stack
    
    for digit in num:
        # Remove larger digits from stack
        while stack and stack[-1] > digit and k > 0:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    # Remove remaining digits from end if k > 0
    while k > 0:
        stack.pop()
        k -= 1
    
    # Handle edge cases
    result = ''.join(stack).lstrip('0')
    return result if result else '0'

# Trapping Rain Water
# Problem: Calculate trapped rainwater in elevation map
def trap_water(height):
    if not height:
        return 0
    
    stack = []  # increasing stack (store indices)
    water = 0
    
    for i, h in enumerate(height):
        while stack and height[stack[-1]] < h:
            bottom = stack.pop()
            if not stack:
                break
            
            # Calculate trapped water
            width = i - stack[-1] - 1
            trapped_height = min(height[stack[-1]], h) - height[bottom]
            water += width * trapped_height
        
        stack.append(i)
    
    return water
```

</details> 