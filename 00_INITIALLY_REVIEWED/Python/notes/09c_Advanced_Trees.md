# Advanced Tree Data Structures

<details>
<summary><strong>💡 Advanced Trees Best Practices</strong></summary>

```python
# 🚨 COMMON PITFALLS TO AVOID:
# 1. Segment Tree: Wrong tree size calculation (use 4*n for safety)
# 2. Fenwick Tree: Forgetting 1-based indexing
# 3. Lazy Propagation: Not pushing updates before querying
# 4. Range Updates: Off-by-one errors in range boundaries

# ✅ BEST PRACTICES:
# 1. Always use 1-based indexing for Fenwick Tree
# 2. Segment Tree size should be 4*n to handle all cases
# 3. Test with small examples first
# 4. Consider space vs time trade-offs

# 🎯 WHEN TO USE EACH:
# - Segment Tree: Range queries with updates, complex operations
# - Fenwick Tree: Simple range sum queries, more space efficient
# - Both: When you need O(log n) range queries and updates
```

</details>

<details>
<summary><strong>Segment Tree</strong></summary>

```python
# Time Complexity: O(log n) for query and update, O(n) for build
# Space Complexity: O(n)

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)  # 4*n is safe size for segment tree
        self.build(arr, 0, 0, self.n - 1)
    
    def build(self, arr, node, start, end):
        """Build segment tree from array"""
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2*node+1, start, mid)
            self.build(arr, 2*node+2, mid+1, end)
            self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]
    
    def update(self, node, start, end, idx, val):
        """Update single element at index idx to val"""
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
        """Query sum in range [l, r]"""
        if r < start or end < l:
            return 0  # No overlap
        if l <= start and end <= r:
            return self.tree[node]  # Complete overlap
        
        # Partial overlap
        mid = (start + end) // 2
        left_sum = self.query(2*node+1, start, mid, l, r)
        right_sum = self.query(2*node+2, mid+1, end, l, r)
        return left_sum + right_sum
    
    # Public interface methods
    def update_value(self, idx, val):
        self.update(0, 0, self.n-1, idx, val)
    
    def range_sum(self, l, r):
        return self.query(0, 0, self.n-1, l, r)

# Segment Tree with Lazy Propagation (for range updates)
class SegmentTreeLazy:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)  # Lazy propagation array
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
        """Push lazy updates down the tree"""
        if self.lazy[node] != 0:
            self.tree[node] += self.lazy[node] * (end - start + 1)
            
            if start != end:  # Not a leaf
                self.lazy[2*node+1] += self.lazy[node]
                self.lazy[2*node+2] += self.lazy[node]
            
            self.lazy[node] = 0
    
    def update_range(self, node, start, end, l, r, val):
        """Add val to all elements in range [l, r]"""
        self.push(node, start, end)
        
        if start > r or end < l:
            return  # No overlap
        
        if start >= l and end <= r:
            # Complete overlap
            self.lazy[node] += val
            self.push(node, start, end)
            return
        
        # Partial overlap
        mid = (start + end) // 2
        self.update_range(2*node+1, start, mid, l, r, val)
        self.update_range(2*node+2, mid+1, end, l, r, val)
        
        self.push(2*node+1, start, mid)
        self.push(2*node+2, mid+1, end)
        self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]
    
    def query_range(self, node, start, end, l, r):
        """Query sum in range [l, r]"""
        if start > r or end < l:
            return 0
        
        self.push(node, start, end)
        
        if start >= l and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_sum = self.query_range(2*node+1, start, mid, l, r)
        right_sum = self.query_range(2*node+2, mid+1, end, l, r)
        return left_sum + right_sum
    
    # Public interface
    def range_update(self, l, r, val):
        self.update_range(0, 0, self.n-1, l, r, val)
    
    def range_sum(self, l, r):
        return self.query_range(0, 0, self.n-1, l, r)

# Min/Max Segment Tree
class MinSegmentTree:
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
    
    def range_min(self, l, r):
        return self.query(0, 0, self.n-1, l, r)
    
    def update_value(self, idx, val):
        self.update(0, 0, self.n-1, idx, val)

# Example usage and applications
def range_sum_query_mutable(nums):
    """LeetCode 307: Range Sum Query - Mutable"""
    class NumArray:
        def __init__(self, nums):
            self.seg_tree = SegmentTree(nums)
        
        def update(self, index, val):
            self.seg_tree.update_value(index, val)
        
        def sumRange(self, left, right):
            return self.seg_tree.range_sum(left, right)
    
    return NumArray(nums)

# Count of Range Sum
def count_range_sum(nums, lower, upper):
    """Count number of range sums that lie in [lower, upper]"""
    # This is a complex problem that uses coordinate compression + segment tree
    # or merge sort with segment tree
    
    def merge_sort_count(prefix_sums, start, end):
        if start >= end:
            return 0
        
        mid = (start + end) // 2
        count = merge_sort_count(prefix_sums, start, mid) + \
                merge_sort_count(prefix_sums, mid + 1, end)
        
        # Count cross-boundary range sums
        j = k = mid + 1
        for i in range(start, mid + 1):
            # Find range [j, k) where prefix_sums[j] - prefix_sums[i] is in [lower, upper]
            while j <= end and prefix_sums[j] - prefix_sums[i] < lower:
                j += 1
            while k <= end and prefix_sums[k] - prefix_sums[i] <= upper:
                k += 1
            count += k - j
        
        # Merge step
        prefix_sums[start:end+1] = sorted(prefix_sums[start:end+1])
        return count
    
    # Calculate prefix sums
    prefix_sums = [0]
    for num in nums:
        prefix_sums.append(prefix_sums[-1] + num)
    
    return merge_sort_count(prefix_sums, 0, len(prefix_sums) - 1)
```

</details>

<details>
<summary><strong>Fenwick Tree (Binary Indexed Tree)</strong></summary>

```python
# Time Complexity: O(log n) for query and update, O(n log n) for build
# Space Complexity: O(n)

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)  # 1-indexed
    
    def update(self, i, delta):
        """Add delta to element at index i (1-indexed)"""
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)  # Add last set bit
    
    def query(self, i):
        """Get prefix sum from 1 to i (1-indexed)"""
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= i & (-i)  # Remove last set bit
        return result
    
    def range_query(self, l, r):
        """Get sum from l to r (1-indexed, inclusive)"""
        return self.query(r) - self.query(l - 1)

# Fenwick Tree with 0-based indexing (more intuitive for arrays)
class FenwickTreeZeroBased:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (self.n + 1)
        
        # Build tree
        for i, val in enumerate(arr):
            self.update(i, val)
    
    def update(self, i, delta):
        """Add delta to element at index i (0-indexed)"""
        i += 1  # Convert to 1-indexed
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)
    
    def prefix_sum(self, i):
        """Get sum from 0 to i (0-indexed, inclusive)"""
        i += 1  # Convert to 1-indexed
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= i & (-i)
        return result
    
    def range_sum(self, l, r):
        """Get sum from l to r (0-indexed, inclusive)"""
        if l == 0:
            return self.prefix_sum(r)
        return self.prefix_sum(r) - self.prefix_sum(l - 1)

# 2D Fenwick Tree (for 2D range sum queries)
class FenwickTree2D:
    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            return
        
        self.m, self.n = len(matrix), len(matrix[0])
        self.tree = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        
        # Build tree
        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])
    
    def update(self, row, col, delta):
        """Add delta to element at (row, col)"""
        i = row + 1  # Convert to 1-indexed
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.tree[i][j] += delta
                j += j & (-j)
            i += i & (-i)
    
    def query(self, row, col):
        """Get sum of rectangle from (0,0) to (row, col)"""
        result = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                result += self.tree[i][j]
                j -= j & (-j)
            i -= i & (-i)
        return result
    
    def range_sum(self, row1, col1, row2, col2):
        """Get sum of rectangle from (row1,col1) to (row2,col2)"""
        return (self.query(row2, col2) - 
                (self.query(row1-1, col2) if row1 > 0 else 0) -
                (self.query(row2, col1-1) if col1 > 0 else 0) +
                (self.query(row1-1, col1-1) if row1 > 0 and col1 > 0 else 0))

# Applications and Examples

# Count Inversions using Fenwick Tree
def count_inversions(arr):
    """Count number of inversions in array using coordinate compression + Fenwick Tree"""
    # Coordinate compression
    sorted_vals = sorted(set(arr))
    coord_map = {val: i+1 for i, val in enumerate(sorted_vals)}
    
    fenwick = FenwickTree(len(sorted_vals))
    inversions = 0
    
    for num in arr:
        compressed = coord_map[num]
        # Count elements greater than current element that appeared before
        inversions += fenwick.query(len(sorted_vals)) - fenwick.query(compressed)
        fenwick.update(compressed, 1)
    
    return inversions

# Range Sum Query - Mutable (LeetCode 307)
class NumArrayFenwick:
    def __init__(self, nums):
        self.nums = nums[:]
        self.fenwick = FenwickTreeZeroBased(nums)
    
    def update(self, index, val):
        delta = val - self.nums[index]
        self.nums[index] = val
        self.fenwick.update(index, delta)
    
    def sumRange(self, left, right):
        return self.fenwick.range_sum(left, right)

# Count of Smaller Numbers After Self
def count_smaller(nums):
    """For each element, count how many smaller elements appear after it"""
    # Coordinate compression
    sorted_vals = sorted(set(nums))
    coord_map = {val: i+1 for i, val in enumerate(sorted_vals)}
    
    fenwick = FenwickTree(len(sorted_vals))
    result = []
    
    # Process from right to left
    for i in range(len(nums) - 1, -1, -1):
        compressed = coord_map[nums[i]]
        # Count elements smaller than current element
        count = fenwick.query(compressed - 1)
        result.append(count)
        fenwick.update(compressed, 1)
    
    return result[::-1]

# Example usage
arr = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]

# Using Fenwick Tree
fenwick = FenwickTreeZeroBased(arr)
print(f"Sum from index 2 to 5: {fenwick.range_sum(2, 5)}")
fenwick.update(3, 10)  # Add 10 to element at index 3
print(f"Sum from index 2 to 5 after update: {fenwick.range_sum(2, 5)}")

# Count inversions
inversions = count_inversions([2, 3, 8, 6, 1])
print(f"Number of inversions: {inversions}")
```

</details> 