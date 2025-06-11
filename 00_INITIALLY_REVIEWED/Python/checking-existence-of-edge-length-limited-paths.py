from collections import deque
from typing import List

"""An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi. Note that there may be multiple edges between two nodes.

Given an array queries, where queries[j] = [pj, qj, limitj], your task is to determine for each queries[j] whether there is a path between pj and qj such that each edge on the path has a distance strictly less than limitj .

Return a boolean array answer, where answer.length == queries.length and the jth value of answer is true if there is a path for queries[j] is true, and false otherwise.

"""

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
            return
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # OPTIMAL APPROACH: Union-Find with sorted edges and queries
        return self.unionFindSolution(n, edgeList, queries)
        
        # ALTERNATIVE: Fixed BFS approach (less efficient but educational)
        # return self.bfsSolution(n, edgeList, queries)
    
    def unionFindSolution(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Sort edges by weight
        edgeList.sort(key=lambda x: x[2])
        print(f"Sorted edges: {edgeList}")
        
        # Sort queries by limit, but keep track of original indices
        indexed_queries = [(limit, src, dest, i) for i, (src, dest, limit) in enumerate(queries)]
        indexed_queries.sort()
        print(f"Sorted queries: {indexed_queries}")
        
        result = [False] * len(queries)
        uf = UnionFind(n)
        edge_idx = 0
        
        for limit, src, dest, orig_idx in indexed_queries:
            print(f"\nProcessing query: src={src}, dest={dest}, limit={limit} (original index {orig_idx})")
            
            # Add all edges with weight < current limit
            while edge_idx < len(edgeList) and edgeList[edge_idx][2] < limit:
                u, v, w = edgeList[edge_idx]
                print(f"  Adding edge ({u}, {v}) with weight {w}")
                uf.union(u, v)
                edge_idx += 1
            
            # Check if src and dest are connected
            result[orig_idx] = uf.connected(src, dest)
            print(f"  Connected? {result[orig_idx]}")
        
        return result
    
    def bfsSolution(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adj_mat = {}
        for edge in edgeList:
            
            source, dest, dist = edge[0], edge[1], edge[2]
            # print("source:" + str(source) + " dest:" + str(dest) + " dist:" + str(dist))

            # setting a -> b
            if source not in adj_mat:
                adj_mat[source] = {}

            if dest not in adj_mat[source]:
                adj_mat[source][dest] = dist
            else:
                adj_mat[source][dest] = min(adj_mat[source][dest], dist)

            # setting b -> a
            if dest not in adj_mat:            
                adj_mat[dest] = {}

            if source not in adj_mat[dest]:
                adj_mat[dest][source] = dist
            else:
                adj_mat[dest][source] = min(adj_mat[dest][source], dist)

        # print("map:" + str(adj_mat))

        def bfs_search(src, dest, limit, adj_mat):
            if src == dest:
                return True
                
            queue = deque([src])
            visited = set([src])
            
            while queue:
                curr = queue.popleft()  # Fixed: use popleft() for proper BFS
                print(f"BFS visiting node: {curr}")
                
                if curr in adj_mat:
                    next_nodes = adj_mat[curr]
                    for next_node, dist in next_nodes.items():
                        print(f"  -> checking edge to {next_node} with distance {dist} (limit: {limit})")
                        
                        if dist >= limit:
                            print(f"    edge distance {dist} >= limit {limit}, skipping")
                            continue
                            
                        if next_node == dest:
                            print(f"    found destination {dest}!")
                            return True
                            
                        if next_node not in visited:
                            print(f"    adding {next_node} to queue")
                            visited.add(next_node)
                            queue.append(next_node)
                        else:
                            print(f"    {next_node} already visited, skipping")
            
            print(f"  no path found from {src} to {dest}")
            return False

        result = []
        for query in queries:
            source, dest, limit = query
            # print("src: " + str(source) + " dest: " + str(dest) + " limit:" + str(limit))
            result.append(bfs_search(source, dest, limit, adj_mat))
            # print("--")
        
        # print("result:"  + str(result))
        return result

# Test both approaches
if __name__ == "__main__":
    solution = Solution()
    
    # Test case from the problem
    n = 3
    edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]]
    queries = [[0,1,2],[0,2,5]]
    
    print("=== Testing Union-Find Approach ===")
    result1 = solution.unionFindSolution(n, edgeList, queries)
    print(f"Result: {result1}")
    
    print("\n=== Testing Fixed BFS Approach ===")
    result2 = solution.bfsSolution(n, edgeList, queries)
    print(f"Result: {result2}")
    
    print(f"\nBoth approaches match: {result1 == result2}")
    print(f"Expected: [False, True]")