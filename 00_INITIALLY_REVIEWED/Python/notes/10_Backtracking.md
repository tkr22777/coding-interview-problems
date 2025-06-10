# Backtracking

<details>
<summary><strong>Permutations & Combinations</strong></summary>

```python
# Permutations
# Problem: Generate all possible arrangements of elements in an array
def permute(nums):
    result = []
    
    def backtrack(current):
        if len(current) == len(nums):
            result.append(current[:])
            return
        
        for num in nums:
            if num not in current:
                current.append(num)
                backtrack(current)
                current.pop()
    
    backtrack([])
    return result

# Combinations
# Problem: Generate all possible k-length combinations from numbers 1 to n
def combine(n, k):
    result = []
    
    def backtrack(start, current):
        if len(current) == k:
            result.append(current[:])
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
        result.append(current[:])
        
        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result

# Combination Sum
# Problem: Find all combinations that sum to target (numbers can be reused)
def combination_sum(candidates, target):
    result = []
    
    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        if remaining < 0:
            return
        
        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])  # i, not i+1 (can reuse)
            current.pop()
    
    backtrack(0, [], target)
    return result
```

</details>

<details>
<summary><strong>Grid Problems</strong></summary>

```python
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
                board[row][col] = '.'
    
    backtrack(0)
    return result

# Sudoku Solver
# Problem: Fill 9×9 Sudoku grid following standard rules (1-9 in each row/column/box)
def solve_sudoku(board):
    def is_valid(row, col, num):
        # Check row
        for j in range(9):
            if board[row][j] == num:
                return False
        
        # Check column
        for i in range(9):
            if board[i][col] == num:
                return False
        
        # Check 3x3 box
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        
        return True
    
    def backtrack():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for num in '123456789':
                        if is_valid(i, j, num):
                            board[i][j] = num
                            if backtrack():
                                return True
                            board[i][j] = '.'
                    return False
        return True
    
    backtrack()

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
        board[i][j] = '#'  # mark as visited
        
        found = (backtrack(i + 1, j, index + 1) or
                backtrack(i - 1, j, index + 1) or
                backtrack(i, j + 1, index + 1) or
                backtrack(i, j - 1, index + 1))
        
        board[i][j] = temp  # restore
        return found
    
    for i in range(m):
        for j in range(n):
            if backtrack(i, j, 0):
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
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)
    
    backtrack('', 0, 0)
    return result

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

# Palindrome Partitioning
# Problem: Partition string so every substring is a palindrome
def partition(s):
    result = []
    
    def is_palindrome(string):
        return string == string[::-1]
    
    def backtrack(start, current):
        if start >= len(s):
            result.append(current[:])
            return
        
        for end in range(start, len(s)):
            if is_palindrome(s[start:end + 1]):
                current.append(s[start:end + 1])
                backtrack(end + 1, current)
                current.pop()
    
    backtrack(0, [])
    return result
```

</details>