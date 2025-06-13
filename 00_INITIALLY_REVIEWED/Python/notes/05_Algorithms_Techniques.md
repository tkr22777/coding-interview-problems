# Algorithms & Techniques

<details>
<summary><strong>Two Pointers</strong></summary>

```python
# Time Complexity:
# - Two Sum: O(n) where n is array length
# - Remove Duplicates: O(n) where n is array length
# - Palindrome Check: O(n) where n is string length
# Space Complexity: O(1) for all operations

# Two Sum in sorted array
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:                         # O(n)
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

# Remove duplicates from sorted array
def remove_duplicates(nums):
    if not nums:
        return 0
    write_idx = 1
    for read_idx in range(1, len(nums)):       # O(n)
        if nums[read_idx] != nums[read_idx - 1]:
            nums[write_idx] = nums[read_idx]
            write_idx += 1
    return write_idx

# Palindrome check
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:                         # O(n)
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

</details>

<details>
<summary><strong>Sliding Window</strong></summary>

```python
# Time Complexity:
# - Max Sum Subarray: O(n) where n is array length
# - Longest Unique Substring: O(n) where n is string length
# Space Complexity: O(1) for max sum, O(min(m,n)) for unique substring where m is charset size

# Maximum sum subarray of size k (fixed window)
def max_sum_subarray(arr, k):
    if len(arr) < k:
        return -1
    
    # Calculate sum of first window
    window_sum = sum(arr[:k])                   # O(k)
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(arr)):               # O(n-k)
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Longest substring without repeating characters (variable window)
def longest_unique_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):                # O(n)
        while s[right] in char_set:            # O(n) amortized
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length
```

</details>

<details>
<summary><strong>Tree Traversals</strong></summary>

```python
# Time Complexity:
# - Inorder Traversal: O(n) where n is number of nodes
# - Level Order Traversal: O(n) where n is number of nodes
# Space Complexity: O(h) for inorder where h is tree height, O(w) for level order where w is max width

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Iterative inorder (most efficient)
def inorder_iterative(root):
    result = []
    stack = []
    current = root
    
    while stack or current:                     # O(n)
        while current:                          # O(h) where h is tree height
            stack.append(current)
            current = current.left
        
        current = stack.pop()
        result.append(current.val)
        current = current.right
    
    return result

# Level order traversal (BFS)
from collections import deque
def level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:                                # O(n)
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):            # O(w) where w is max width
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result
```

</details>

<details>
<summary><strong>Graph Algorithms</strong></summary>

```python
# Time Complexity:
# - BFS Shortest Path: O(V + E) where V is vertices and E is edges
# - DFS Path Finding: O(V + E)
# - Cycle Detection: O(V + E)
# - Build Graph: O(E) where E is number of edges
# Space Complexity: O(V) for all operations

from collections import deque, defaultdict

# BFS for shortest path (unweighted)
def bfs_shortest_path(graph, start, end):
    if start == end:
        return [start]
    
    queue = deque([(start, [start])])
    visited = {start}
    
    while queue:                                # O(V)
        node, path = queue.popleft()
        
        for neighbor in graph[node]:            # O(E) total
            if neighbor == end:
                return path + [neighbor]
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return []

# DFS for path finding
def dfs_find_path(graph, start, end, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    
    if start == end:
        return [start]
    
    for neighbor in graph[start]:               # O(V + E)
        if neighbor not in visited:
            path = dfs_find_path(graph, neighbor, end, visited)
            if path:
                return [start] + path
    
    return []

# Check if graph has cycle (undirected)
def has_cycle_undirected(graph):
    visited = set()
    
    def dfs(node, parent):                      # O(V + E)
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if neighbor in visited or dfs(neighbor, node):
                return True
        return False
    
    for node in graph:                          # O(V)
        if node not in visited:
            if dfs(node, None):
                return True
    return False

# Build adjacency list from edges
def build_graph(edges):
    graph = defaultdict(list)
    for u, v in edges:                          # O(E)
        graph[u].append(v)
        graph[v].append(u)  # For undirected graph
    return graph
```

</details>

<details>
<summary><strong>Grid Traversal</strong></summary>

```python
# Time Complexity:
# - DFS Grid: O(R*C) where R is rows and C is columns
# - BFS Grid: O(R*C) for shortest path
# Space Complexity: O(R*C) for visited array/matrix

from collections import deque

# DFS on grid (find connected components)
def dfs_grid(grid, row, col, visited):
    if (row < 0 or row >= len(grid) or 
        col < 0 or col >= len(grid[0]) or 
        visited[row][col] or grid[row][col] == 0):
        return 0
    
    visited[row][col] = True
    size = 1
    
    # Explore 4 directions
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:                   # O(4) = O(1)
        size += dfs_grid(grid, row + dr, col + dc, visited)
    
    return size

# BFS on grid (shortest path)
def bfs_grid_shortest_path(grid, start, end):
    if not grid or grid[start[0]][start[1]] == 0:
        return -1
    
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start[0], start[1], 0)])  # (row, col, distance)
    visited = set([start])
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:                                # O(R*C)
        row, col, dist = queue.popleft()
        
        if (row, col) == end:
            return dist
        
        for dr, dc in directions:              # O(4) = O(1)
            new_row, new_col = row + dr, col + dc
            if (0 <= new_row < rows and 
                0 <= new_col < cols and 
                grid[new_row][new_col] == 1 and 
                (new_row, new_col) not in visited):
                visited.add((new_row, new_col))
                queue.append((new_row, new_col, dist + 1))
    
    return -1

# Number of Islands
# Problem: Count number of islands in 2D grid (1s surrounded by 0s)
def numIslands(self, grid: List[List[str]]) -> int:
    if not grid:
        return 0
        
    moves = [
        (-1,0),  # up
        (1,0),   # down
        (0,1),   # right
        (0,-1),  # left
    ]
    
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    visited = set()

    def dfs(r: int, c: int) -> None:
        if (r < 0 or r >= rows or 
            c < 0 or c >= cols or 
            grid[r][c] == '0' or 
            (r,c) in visited):
            return
            
        visited.add((r,c))
        for dr, dc in moves:
            dfs(r + dr, c + dc)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r,c) not in visited:
                count += 1
                dfs(r, c)
                
    return count
```

</details> 