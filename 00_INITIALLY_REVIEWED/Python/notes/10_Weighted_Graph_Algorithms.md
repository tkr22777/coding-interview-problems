# Weighted Graph Algorithms

<details>
<summary><strong>💡 Weighted Graph Best Practices</strong></summary>

```python
# 🚨 COMMON PITFALLS TO AVOID:
# 1. Dijkstra: Using with negative weights (use Bellman-Ford instead)
# 2. Bellman-Ford: Not detecting negative cycles properly
# 3. Floyd-Warshall: Forgetting to initialize diagonal to 0
# 4. MST: Not sorting edges properly for Kruskal's algorithm
# 5. All algorithms: Off-by-one errors in adjacency matrix indexing

# ✅ BEST PRACTICES:
# 1. Always check for negative weights before choosing algorithm
# 2. Use appropriate data structures (min-heap for Dijkstra)
# 3. Handle disconnected graphs properly
# 4. Consider space vs time trade-offs (adjacency list vs matrix)
# 5. Test with edge cases: single node, no edges, negative cycles

# 🎯 ALGORITHM SELECTION GUIDE:
# - Single source shortest path (no negative weights): Dijkstra's
# - Single source shortest path (with negative weights): Bellman-Ford
# - All pairs shortest path: Floyd-Warshall
# - Minimum Spanning Tree: Kruskal's or Prim's
# - Detect negative cycles: Bellman-Ford
```

</details>

<details>
<summary><strong>Dijkstra's Algorithm</strong></summary>

```python
# Time Complexity: O((V + E) log V) with min-heap
# Space Complexity: O(V)
# Use case: Single-source shortest path with non-negative weights

import heapq
from collections import defaultdict

def dijkstra(graph, start):
    """
    Find shortest paths from start to all other vertices
    graph: adjacency list {node: [(neighbor, weight), ...]}
    Returns: {node: distance} dictionary
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Min-heap: (distance, node)
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        if current in visited:
            continue
        
        visited.add(current)
        
        # Explore neighbors
        for neighbor, weight in graph[current]:
            if neighbor in visited:
                continue
                
            new_dist = current_dist + weight
            
            # Relaxation step
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))
    
    return distances

# With path reconstruction
def dijkstra_with_path(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous = {}
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        if current == end:
            break
        if current in visited:
            continue
        visited.add(current)
        
        for neighbor, weight in graph[current]:
            if neighbor not in visited:
                new_dist = current_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    previous[neighbor] = current
                    heapq.heappush(pq, (new_dist, neighbor))
    
    # Reconstruct path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous.get(current)
    path.reverse()
    
    return distances[end], path if path[0] == start else []
```

</details>

<details>
<summary><strong>Bellman-Ford Algorithm</strong></summary>

```python
# Time Complexity: O(V * E)
# Space Complexity: O(V)
# Use case: Single-source shortest path with negative weights, detect negative cycles

def bellman_ford(graph, start):
    """
    Find shortest paths from start, can handle negative weights
    graph: list of edges [(source, destination, weight), ...]
    Returns: (distances, has_negative_cycle)
    """
    # Get all vertices
    vertices = set()
    for src, dest, weight in graph:
        vertices.add(src)
        vertices.add(dest)
    
    # Initialize distances
    distances = {v: float('inf') for v in vertices}
    distances[start] = 0
    
    # Relax edges V-1 times
    for _ in range(len(vertices) - 1):
        for src, dest, weight in graph:
            if distances[src] != float('inf') and distances[src] + weight < distances[dest]:
                distances[dest] = distances[src] + weight
    
    # Check for negative cycles
    has_negative_cycle = False
    for src, dest, weight in graph:
        if distances[src] != float('inf') and distances[src] + weight < distances[dest]:
            has_negative_cycle = True
            break
    
    return distances, has_negative_cycle

# With negative cycle detection
def detect_negative_cycle(graph):
    """Returns True if graph has negative cycle"""
    vertices = set()
    for src, dest, weight in graph:
        vertices.add(src)
        vertices.add(dest)
    
    if not vertices:
        return False
    
    distances = {v: float('inf') for v in vertices}
    distances[next(iter(vertices))] = 0
    
    # Relax V-1 times
    for _ in range(len(vertices) - 1):
        for src, dest, weight in graph:
            if distances[src] != float('inf') and distances[src] + weight < distances[dest]:
                distances[dest] = distances[src] + weight
    
    # Check for negative cycle
    for src, dest, weight in graph:
        if distances[src] != float('inf') and distances[src] + weight < distances[dest]:
            return True
    
    return False
```

</details>

<details>
<summary><strong>Floyd-Warshall Algorithm</strong></summary>

```python
# Time Complexity: O(V³)
# Space Complexity: O(V²)
# Use case: All-pairs shortest path

def floyd_warshall(graph):
    """
    Find shortest paths between all pairs of vertices
    graph: adjacency matrix (2D list) where graph[i][j] is weight from i to j
    Use float('inf') for no edge, 0 for same vertex
    Returns: distance matrix and next vertex matrix for path reconstruction
    """
    n = len(graph)
    
    # Initialize distance matrix
    dist = [[float('inf')] * n for _ in range(n)]
    next_vertex = [[None] * n for _ in range(n)]
    
    # Copy graph and initialize next matrix
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif graph[i][j] != float('inf'):
                dist[i][j] = graph[i][j]
                next_vertex[i][j] = j
    
    # Floyd-Warshall main algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_vertex[i][j] = next_vertex[i][k]
    
    return dist, next_vertex

def reconstruct_path(next_vertex, start, end):
    """Reconstruct path using next_vertex matrix"""
    if next_vertex[start][end] is None:
        return []
    
    path = [start]
    current = start
    while current != end:
        current = next_vertex[current][end]
        path.append(current)
    
    return path
```

</details>

<details>
<summary><strong>Minimum Spanning Tree (MST)</strong></summary>

```python
# Kruskal's Algorithm
# Time Complexity: O(E log E)
# Space Complexity: O(V)

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True

def kruskal_mst(vertices, edges):
    """
    Find Minimum Spanning Tree using Kruskal's algorithm
    vertices: number of vertices (0 to vertices-1)
    edges: list of (weight, u, v) tuples
    Returns: (mst_weight, mst_edges)
    """
    # Sort edges by weight
    edges.sort()
    
    uf = UnionFind(vertices)
    mst_edges = []
    mst_weight = 0
    
    for weight, u, v in edges:
        if uf.union(u, v):
            mst_edges.append((u, v, weight))
            mst_weight += weight
            
            # MST complete when we have V-1 edges
            if len(mst_edges) == vertices - 1:
                break
    
    return mst_weight, mst_edges

# Prim's Algorithm
# Time Complexity: O(E log V) with min-heap
# Space Complexity: O(V)

def prim_mst(graph, start=0):
    """
    Find MST using Prim's algorithm
    graph: adjacency list {node: [(neighbor, weight), ...]}
    Returns: (mst_weight, mst_edges)
    """
    import heapq
    
    visited = set()
    mst_edges = []
    mst_weight = 0
    
    # Start with arbitrary vertex
    visited.add(start)
    
    # Add all edges from start vertex to heap
    edges = [(weight, start, neighbor) for neighbor, weight in graph[start]]
    heapq.heapify(edges)
    
    while edges and len(visited) < len(graph):
        weight, u, v = heapq.heappop(edges)
        
        if v in visited:
            continue
        
        # Add vertex to MST
        visited.add(v)
        mst_edges.append((u, v, weight))
        mst_weight += weight
        
        # Add new edges to heap
        for neighbor, edge_weight in graph[v]:
            if neighbor not in visited:
                heapq.heappush(edges, (edge_weight, v, neighbor))
    
    return mst_weight, mst_edges

# Usage: Both algorithms find MST, choose based on graph density
# Kruskal's: Better for sparse graphs (fewer edges)
# Prim's: Better for dense graphs (many edges)
```

</details>

<details>
<summary><strong>Topological Sort (DAG)</strong></summary>

```python
# Time Complexity: O(V + E)
# Space Complexity: O(V)
# Use case: Ordering vertices in Directed Acyclic Graph

from collections import defaultdict, deque

def topological_sort_kahn(graph, vertices):
    """
    Topological sort using Kahn's algorithm (BFS-based)
    graph: adjacency list {node: [neighbors]}
    vertices: list of all vertices
    Returns: topologically sorted list or None if cycle exists
    """
    # Calculate in-degrees
    in_degree = {v: 0 for v in vertices}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
    
    # Find vertices with no incoming edges
    queue = deque([v for v in vertices if in_degree[v] == 0])
    result = []
    
    while queue:
        u = queue.popleft()
        result.append(u)
        
        # Remove u and update in-degrees
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
    
    # Check for cycle
    if len(result) != len(vertices):
        return None  # Cycle detected
    
    return result

def topological_sort_dfs(graph, vertices):
    """
    Topological sort using DFS
    Returns: topologically sorted list or None if cycle exists
    """
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {v: WHITE for v in vertices}
    result = []
    
    def dfs(u):
        if color[u] == GRAY:
            return False  # Back edge found (cycle)
        if color[u] == BLACK:
            return True   # Already processed
        
        color[u] = GRAY
        
        for v in graph[u]:
            if not dfs(v):
                return False
        
        color[u] = BLACK
        result.append(u)
        return True
    
    # Process all vertices
    for v in vertices:
        if color[v] == WHITE:
            if not dfs(v):
                return None  # Cycle detected
    
    result.reverse()  # Reverse to get correct order
    return result

# Application: Course scheduling
def can_finish_courses(num_courses, prerequisites):
    """Check if all courses can be finished (no cycles)"""
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    
    vertices = list(range(num_courses))
    return topological_sort_kahn(graph, vertices) is not None
```

</details> 