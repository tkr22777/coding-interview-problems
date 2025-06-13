# Dynamic Programming

<details>
<summary><strong>1D DP</strong></summary>

```python
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

# Coin Change (minimum coins)
# Problem: Find minimum number of coins needed to make given amount
def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1
```

</details>

<details>
<summary><strong>2D DP</strong></summary>

```python
# Unique Paths
# Problem: How many ways to reach bottom-right from top-left in m×n grid (only right/down moves)
def unique_paths(m, n):
    dp = [[1] * n for _ in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    return dp[m - 1][n - 1]

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
```

</details>

<details>
<summary><strong>Knapsack Patterns</strong></summary>

```python
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
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
    
    return dp[target]

# Target Sum
# Problem: How many ways to assign +/- signs to numbers to reach target sum?
def find_target_sum_ways(nums, target):
    total = sum(nums)
    if target > total or target < -total or (target + total) % 2:
        return 0
    
    s = (target + total) // 2
    dp = [0] * (s + 1)
    dp[0] = 1
    
    for num in nums:
        for i in range(s, num - 1, -1):
            dp[i] += dp[i - num]
    
    return dp[s]
```

</details> 