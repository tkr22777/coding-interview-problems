# Dynamic Programming

<details>
<summary><strong>💡 DP Best Practices & Common Pitfalls</strong></summary>

```python
# 🚨 COMMON PITFALLS TO AVOID:
# 1. Off-by-one errors in array indexing
# 2. Not handling edge cases (empty arrays, n=0, n=1)
# 3. Using wrong loop direction in space-optimized solutions
# 4. Forgetting to initialize base cases properly
# 5. Not considering negative numbers in problems

# ✅ BEST PRACTICES:
# 1. Always draw the recurrence relation first
# 2. Start with recursive solution, then memoize, then tabulate
# 3. Consider space optimization after getting correct solution
# 4. Use meaningful variable names (prev, curr instead of dp[i-1], dp[i])
# 5. Handle edge cases explicitly at the beginning

# 🎯 SPACE OPTIMIZATION PATTERN:
# Most 1D DP can be optimized from O(n) to O(1)
# Most 2D DP can be optimized from O(m*n) to O(min(m,n))
```

</details>

<details>
<summary><strong>1D DP</strong></summary>

```python
# Time Complexity: O(n) for all 1D DP problems
# Space Complexity: O(n) basic, O(1) optimized

# Fibonacci (classic example)
# Problem: Find the nth number in Fibonacci sequence (0, 1, 1, 2, 3, 5, 8...)
def fibonacci(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# 🚀 SPACE OPTIMIZED VERSION - O(1) space
def fibonacci_optimized(n):
    if n <= 1:
        return n
    prev2, prev1 = 0, 1
    for i in range(2, n + 1):
        curr = prev1 + prev2
        prev2, prev1 = prev1, curr
    return prev1

# House Robber
# Problem: Rob houses to get max money, but can't rob adjacent houses
def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    
    return dp[-1]

# 🚀 SPACE OPTIMIZED VERSION - O(1) space
def rob_optimized(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    prev2, prev1 = nums[0], max(nums[0], nums[1])
    for i in range(2, len(nums)):
        curr = max(prev1, prev2 + nums[i])
        prev2, prev1 = prev1, curr
    
    return prev1

# Climbing Stairs
# Problem: How many ways to climb n stairs if you can take 1 or 2 steps at a time
def climb_stairs(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# 💡 INSIGHT: This is actually Fibonacci in disguise!
def climb_stairs_insight(n):
    # Ways to reach step n = ways to reach (n-1) + ways to reach (n-2)
    # This is exactly Fibonacci sequence starting from fib(1)=1, fib(2)=2
    return fibonacci_optimized(n + 1)

# Coin Change (minimum coins)
# Problem: Find minimum number of coins needed to make given amount
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

# 🚨 COMMON MISTAKE: Wrong loop order
def coin_change_wrong(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    # ❌ WRONG: This allows using same coin multiple times in one iteration
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1
```

</details>

<details>
<summary><strong>2D DP</strong></summary>

```python
# Time Complexity: O(m*n) for most 2D DP problems
# Space Complexity: O(m*n) basic, O(min(m,n)) optimized

# Unique Paths
# Problem: How many ways to reach bottom-right from top-left in m×n grid (only right/down moves)
def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]

# 🚀 SPACE OPTIMIZED VERSION - O(min(m,n)) space
def unique_paths_optimized(m, n):
    # Use smaller dimension for space optimization
    if m > n:
        m, n = n, m
    
    dp = [1] * m
    for j in range(1, n):
        for i in range(1, m):
            dp[i] += dp[i - 1]
    return dp[m - 1]

# Longest Common Subsequence
# Problem: Find length of longest subsequence common to both strings
def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

# 🚀 SPACE OPTIMIZED VERSION - O(min(m,n)) space
def lcs_optimized(text1, text2):
    # Make text1 the shorter string
    if len(text1) > len(text2):
        text1, text2 = text2, text1
    
    m, n = len(text1), len(text2)
    prev = [0] * (m + 1)
    curr = [0] * (m + 1)
    
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if text1[i - 1] == text2[j - 1]:
                curr[i] = prev[i - 1] + 1
            else:
                curr[i] = max(prev[i], curr[i - 1])
        prev, curr = curr, prev
    
    return prev[m]

# Edit Distance
# Problem: Minimum operations (insert/delete/replace) to transform word1 into word2
def min_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,      # delete
                    dp[i][j - 1] + 1,      # insert
                    dp[i - 1][j - 1] + 1   # replace
                )
    
    return dp[m][n]

# 💡 INSIGHT: Remember the operations clearly
# dp[i-1][j] + 1     -> delete from word1
# dp[i][j-1] + 1     -> insert into word1  
# dp[i-1][j-1] + 1   -> replace in word1

# Maximum Square
# Problem: Find area of largest square containing only 1s in binary matrix
def maximal_square(matrix):
    if not matrix:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    dp = [[0] * n for _ in range(m)]
    max_side = 0
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                max_side = max(max_side, dp[i][j])
    
    return max_side * max_side

# 💡 INSIGHT: The key insight is that a square's size is limited by its smallest neighbor
# Think of it as: "How big of a square can I form with current cell as bottom-right corner?"
```

</details>

<details>
<summary><strong>Knapsack Patterns</strong></summary>

```python
# 🎯 KNAPSACK PATTERN RECOGNITION:
# - 0/1 Knapsack: Each item used once, maximize value
# - Unbounded Knapsack: Items can be reused, maximize value  
# - Subset Sum: Can we achieve target sum? (boolean)
# - Partition: Can we split into equal sum subsets?
# - Target Sum: How many ways to achieve target?

# 0/1 Knapsack
# Problem: Given items with weights/values, maximize value within weight capacity (each item used once)
def knapsack_01(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    dp[i - 1][w],  # don't take
                    dp[i - 1][w - weights[i - 1]] + values[i - 1]  # take
                )
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

# 🚀 SPACE OPTIMIZED VERSION - O(capacity) space
def knapsack_01_optimized(weights, values, capacity):
    dp = [0] * (capacity + 1)
    
    for i in range(len(weights)):
        # 🚨 CRITICAL: Iterate backwards to avoid using updated values
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[capacity]

# Subset Sum (Partition Equal Subset Sum)
# Problem: Can array be partitioned into two subsets with equal sum?
def can_partition(nums):
    total = sum(nums)
    if total % 2:
        return False
    
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    
    for num in nums:
        # 🚨 CRITICAL: Iterate backwards for 0/1 knapsack pattern
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    
    return dp[target]

# 💡 INSIGHT: This is 0/1 knapsack in disguise!
# We're asking: "Can we pick items (numbers) to fill exactly half the total weight?"

# Target Sum
# Problem: How many ways to assign +/- signs to numbers to reach target sum?
def find_target_sum_ways(nums, target):
    total = sum(nums)
    if target > total or target < -total or (target + total) % 2:
        return 0
    
    # 🧠 KEY INSIGHT: This transforms into subset sum problem!
    # If P = positive subset, N = negative subset
    # P + N = total, P - N = target
    # Solving: P = (target + total) / 2
    s = (target + total) // 2
    dp = [0] * (s + 1)
    dp[0] = 1
    
    for num in nums:
        for i in range(s, num - 1, -1):
            dp[i] += dp[i - num]
    
    return dp[s]

# 🚨 COMMON MISTAKE: Not checking if (target + total) is even
# The transformation only works when (target + total) is divisible by 2
```

</details> 