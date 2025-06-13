# Backtracking

<details>
<summary><strong>💡 Backtracking Best Practices & Common Pitfalls</strong></summary>

```python
# 🚨 COMMON PITFALLS TO AVOID:
# 1. Forgetting to make a copy when adding to result (result.append(current[:]))
# 2. Not restoring state properly after recursive call
# 3. Wrong base case conditions
# 4. Modifying input array/grid without restoring it
# 5. Using global variables instead of passing state

# ✅ BEST PRACTICES:
# 1. Always think: "What do I choose? What do I explore? How do I unchoose?"
# 2. Use clear variable names (current, path, visited)
# 3. Handle base cases first
# 4. Make state changes before recursion, undo after
# 5. Consider iterative solutions for simple cases

# 🎯 BACKTRACKING TEMPLATE:
def backtrack(state, choices):
    if is_solution(state):
        result.append(state[:])  # Make copy!
        return
    
    for choice in choices:
        if is_valid(choice, state):
            make_choice(choice, state)
            backtrack(state, new_choices)
            undo_choice(choice, state)  # Critical!

# 🧠 KEY INSIGHT: Backtracking = DFS + State Management
```

</details>

<details>
<summary><strong>Permutations & Combinations</strong></summary>

```python
# Time Complexity: O(n! * n) for permutations, O(2^n * n) for combinations
# Space Complexity: O(n) for recursion depth

# Permutations
# Problem: Generate all possible arrangements of elements in an array
def permute(nums):
    result = []
    
    def backtrack(current):
        if len(current) == len(nums):
            result.append(current[:])  # 🚨 CRITICAL: Make copy!
            return
        
        for num in nums:
            if num not in current:  # 🚨 SLOW: O(n) lookup each time
                current.append(num)
                backtrack(current)
                current.pop()
    
    backtrack([])
    return result

# 🚀 OPTIMIZED VERSION - Use visited set for O(1) lookup
def permute_optimized(nums):
    result = []
    
    def backtrack(current, used):
        if len(current) == len(nums):
            result.append(current[:])
            return
        
        for i, num in enumerate(nums):
            if i not in used:
                current.append(num)
                used.add(i)
                backtrack(current, used)
                used.remove(i)  # 🚨 CRITICAL: Undo state change
                current.pop()
    
    backtrack([], set())
    return result

# 💡 EVEN BETTER: Swap-based approach (no extra space for tracking)
def permute_swap(nums):
    result = []
    
    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return
        
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]  # Choose
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]  # Unchoose
    
    backtrack(0)
    return result

# Combinations
# Problem: Generate all possible k-length combinations from numbers 1 to n
def combine(n, k):
    result = []
    
    def backtrack(start, current):
        if len(current) == k:
            result.append(current[:])
            return
        
        # 🚀 PRUNING: If we can't form k elements, stop early
        remaining_needed = k - len(current)
        remaining_available = n - start + 1
        if remaining_needed > remaining_available:
            return
        
        for i in range(start, n + 1):
            current.append(i)
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(1, [])
    return result

# Subsets
# Problem: Generate all possible subsets (power set) of an array
def subsets(nums):
    result = []
    
    def backtrack(start, current):
        result.append(current[:])  # Add current subset
        
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result

# 💡 ITERATIVE APPROACH - Sometimes simpler!
def subsets_iterative(nums):
    result = [[]]
    for num in nums:
        result += [subset + [num] for subset in result]
    return result

# Combination Sum
# Problem: Find all combinations that sum to target (numbers can be reused)
def combination_sum(candidates, target):
    result = []
    
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        if remaining < 0:  # 🚀 PRUNING: Early termination
            return
        
        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])  # i, not i+1 (can reuse)
            current.pop()
    
    backtrack(0, [], target)
    return result

# 🚀 OPTIMIZATION: Sort array for better pruning
def combination_sum_optimized(candidates, target):
    candidates.sort()  # Enable early termination
    result = []
    
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        
        for i in range(start, len(candidates)):
            if candidates[i] > remaining:  # 🚀 PRUNING: No point continuing
                break
            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])
            current.pop()
    
    backtrack(0, [], target)
    return result
```

</details>

<details>
<summary><strong>Grid Problems</strong></summary>

```python
# Time Complexity: Exponential in worst case, varies by problem
# Space Complexity: O(n) for recursion depth + visited tracking

# N-Queens
# Problem: Place N queens on N×N chessboard so none attack each other
def solve_n_queens(n):
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    
    def is_safe(row, col):
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check diagonal
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        # Check anti-diagonal
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i][j] == 'Q':
                return False
        
        return True
    
    def backtrack(row):
        if row == n:
            result.append([''.join(row) for row in board])
            return
        
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'  # 🚨 CRITICAL: Restore state
    
    backtrack(0)
    return result

# 🚀 OPTIMIZED VERSION - Use sets for O(1) conflict checking
def solve_n_queens_optimized(n):
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col
    
    def backtrack(row):
        if row == n:
            result.append([''.join(row) for row in board])
            return
        
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            
            # Make choice
            board[row][col] = 'Q'
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            
            backtrack(row + 1)
            
            # Undo choice
            board[row][col] = '.'
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
    
    backtrack(0)
    return result

# Word Search
# Problem: Find if word exists in 2D grid by connecting adjacent letters
def exist(board, word):
    if not board:
        return False
    
    m, n = len(board), len(board[0])
    
    def backtrack(i, j, index):
        if index == len(word):
            return True
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[index]:
            return False
        
        temp = board[i][j]
        board[i][j] = '#'  # 🚨 CRITICAL: Mark as visited
        
        found = (backtrack(i + 1, j, index + 1) or
                backtrack(i - 1, j, index + 1) or
                backtrack(i, j + 1, index + 1) or
                backtrack(i, j - 1, index + 1))
        
        board[i][j] = temp  # 🚨 CRITICAL: Restore original value
        return found
    
    for i in range(m):
        for j in range(n):
            if backtrack(i, j, 0):
                return True
    return False

# 💡 ALTERNATIVE: Use visited set instead of modifying board
def exist_with_visited_set(board, word):
    if not board:
        return False
    
    m, n = len(board), len(board[0])
    
    def backtrack(i, j, index, visited):
        if index == len(word):
            return True
        if (i < 0 or i >= m or j < 0 or j >= n or 
            board[i][j] != word[index] or (i, j) in visited):
            return False
        
        visited.add((i, j))
        found = (backtrack(i + 1, j, index + 1, visited) or
                backtrack(i - 1, j, index + 1, visited) or
                backtrack(i, j + 1, index + 1, visited) or
                backtrack(i, j - 1, index + 1, visited))
        visited.remove((i, j))  # 🚨 CRITICAL: Undo state change
        
        return found
    
    for i in range(m):
        for j in range(n):
            if backtrack(i, j, 0, set()):
                return True
    return False
```

</details>

<details>
<summary><strong>String Problems</strong></summary>

```python
# Generate Parentheses
# Problem: Generate all combinations of well-formed parentheses with n pairs
def generate_parentheses(n):
    result = []
    
    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return
        
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)
        if close_count < open_count:  # 🚨 CRITICAL: Can only close if we have open
            backtrack(current + ')', open_count, close_count + 1)
    
    backtrack('', 0, 0)
    return result

# 💡 INSIGHT: The key constraint is close_count < open_count
# This ensures we never have more closing than opening brackets

# Letter Combinations of Phone Number
# Problem: Generate all possible letter combinations from phone number digits
def letter_combinations(digits):
    if not digits:
        return []
    
    phone = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    result = []
    
    def backtrack(index, current):
        if index == len(digits):
            result.append(current)
            return
        
        for letter in phone[digits[index]]:
            backtrack(index + 1, current + letter)
    
    backtrack(0, '')
    return result

# 🚀 ITERATIVE APPROACH - Sometimes cleaner for this problem
def letter_combinations_iterative(digits):
    if not digits:
        return []
    
    phone = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    
    result = ['']
    for digit in digits:
        result = [combo + letter 
                 for combo in result 
                 for letter in phone[digit]]
    
    return result

# Palindrome Partitioning
# Problem: Partition string so every substring is a palindrome
def partition(s):
    result = []
    
    def is_palindrome(string):
        return string == string[::-1]
    
    def backtrack(start, current):
        if start == len(s):
            result.append(current[:])
            return
        
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                current.append(substring)
                backtrack(end, current)
                current.pop()
    
    backtrack(0, [])
    return result

# 🚀 OPTIMIZED VERSION - Precompute palindrome checks
def partition_optimized(s):
    n = len(s)
    # Precompute palindrome matrix
    is_pal = [[False] * n for _ in range(n)]
    
    # Every single character is palindrome
    for i in range(n):
        is_pal[i][i] = True
    
    # Check for palindromes of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            is_pal[i][i + 1] = True
    
    # Check for palindromes of length 3 and more
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and is_pal[i + 1][j - 1]:
                is_pal[i][j] = True
    
    result = []
    
    def backtrack(start, current):
        if start == n:
            result.append(current[:])
            return
        
        for end in range(start, n):
            if is_pal[start][end]:
                current.append(s[start:end + 1])
                backtrack(end + 1, current)
                current.pop()
    
    backtrack(0, [])
    return result
```

</details>