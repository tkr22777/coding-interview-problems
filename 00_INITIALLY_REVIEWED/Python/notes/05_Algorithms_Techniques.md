# Algorithms & Techniques

<details>
<summary><strong>Two Pointers</strong></summary>

```python
# Two Sum in sorted array
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
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
    for read_idx in range(1, len(nums)):
        if nums[read_idx] != nums[read_idx - 1]:
            nums[write_idx] = nums[read_idx]
            write_idx += 1
    return write_idx

# Palindrome check
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
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
# Maximum sum subarray of size k (fixed window)
def max_sum_subarray(arr, k):
    if len(arr) < k:
        return -1
    
    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Longest substring without repeating characters (variable window)
def longest_unique_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
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
    
    while stack or current:
        while current:
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
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
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
from collections import deque, defaultdict

# BFS for shortest path (unweighted)
def bfs_shortest_path(graph, start, end):
    if start == end:
        return [start]
    
    queue = deque([(start, [start])])
    visited = {start}
    
    while queue:
        node, path = queue.popleft()
        
        for neighbor in graph[node]:
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
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            path = dfs_find_path(graph, neighbor, end, visited)
            if path:
                return [start] + path
    
    return []

# Check if graph has cycle (undirected)
def has_cycle_undirected(graph):
    visited = set()
    
    def dfs(node, parent):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if neighbor in visited or dfs(neighbor, node):
                return True
        return False
    
    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True
    return False

# Build adjacency list from edges
def build_graph(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # For undirected graph
    return graph
```

</details>

<details>
<summary><strong>Grid Traversal</strong></summary>

```python
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
    for dr, dc in directions:
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
    
    while queue:
        row, col, dist = queue.popleft()
        
        if (row, col) == end:
            return dist
        
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            
            if (0 <= nr < rows and 0 <= nc < cols and 
                (nr, nc) not in visited and grid[nr][nc] == 1):
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    
    return -1

# Count islands (connected components)
def count_islands(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    count = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and not visited[i][j]:
                dfs_grid(grid, i, j, visited)
                count += 1
    
    return count

# Flood fill
def flood_fill(image, sr, sc, new_color):
    original_color = image[sr][sc]
    if original_color == new_color:
        return image
    
    def dfs(row, col):
        if (row < 0 or row >= len(image) or 
            col < 0 or col >= len(image[0]) or 
            image[row][col] != original_color):
            return
        
        image[row][col] = new_color
        
        # Fill 4 directions
        dfs(row - 1, col)
        dfs(row + 1, col)
        dfs(row, col - 1)
        dfs(row, col + 1)
    
    dfs(sr, sc)
    return image
```

</details>

<details>
<summary><strong>Time Complexity Notes</strong></summary>

- **Two Pointers**:
  - Traversal: O(n)
  - Sliding Window: O(n)

- **Sliding Window**:
  - Fixed window: O(n)
  - Variable window: O(n)

- **Tree Traversals**:
  - DFS/BFS: O(n) where n is the number of nodes
  - Inorder/Preorder/Postorder: O(n)

- **Graph Traversals**:
  - DFS/BFS: O(V + E) where V is vertices and E is edges
  - Dijkstra's Algorithm: O((V + E) log V) with binary heap

- **Dynamic Programming**:
  - 1D DP: O(n)
  - 2D DP: O(rows × cols)

- **Backtracking**:
  - Time complexity varies, often exponential O(2^n) or O(n!)

- **Advanced Patterns**:
  - Union Find: O(log n) with path compression
  - Monotonic Stack/Queue: O(n)
  - Fast/Slow Pointers: O(n)

</details> 