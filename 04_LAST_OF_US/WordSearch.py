"""
Word Search

Problem Statement:
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells 
are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Examples:
- Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
  Output: true
  Explanation: The word "ABCCED" can be found by starting at the top-left 'A' and moving
  right, right, down, left, down.

- Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
  Output: true
  Explanation: The word "SEE" can be found starting at the middle 'S' and moving 
  down, then right.

- Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
  Output: false
  Explanation: The word "ABCB" cannot be formed because we can't reuse the 'B' at (0,1).

Constraints:
- m == board.length
- n = board[i].length
- 1 <= m, n <= 6
- 1 <= word.length <= 15
- board and word consists of only lowercase and uppercase English letters.
"""

from typing import List, Set, Tuple

def word_exists_in_board(board: List[List[str]], word: str) -> bool:
    """
    Determine if the word exists in the board.
    
    Args:
        board: The 2D grid of characters
        word: The word to search for
        
    Returns:
        True if the word can be found in the board, False otherwise
    
    Approach hints:
    - Use backtracking to explore possible paths
    - Start the search from each cell in the board
    - Keep track of visited cells to prevent reusing the same cell
    - Consider optimizations like checking if characters exist in the board before searching
    """
    # TODO: Implement your solution here
    pass


# Helper function for backtracking
def backtrack(board: List[List[str]], word: str, index: int, row: int, col: int, visited: Set[Tuple[int, int]]) -> bool:
    """
    Helper function to perform backtracking search from a position.
    
    Args:
        board: The 2D grid of characters
        word: The word to search for
        index: Current index in the word being matched
        row: Current row position in the board
        col: Current column position in the board
        visited: Set of already visited cell coordinates (row, col)
        
    Returns:
        True if the remaining part of the word can be found from this position, False otherwise
    """
    # TODO: Implement backtracking search
    pass


# Test cases
def test_word_exists_in_board():
    test_cases = [
        {
            "board": [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
            "word": "ABCCED", 
            "expected": True
        },
        {
            "board": [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
            "word": "SEE", 
            "expected": True
        },
        {
            "board": [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
            "word": "ABCB", 
            "expected": False
        },
        {
            "board": [["a"]], 
            "word": "a", 
            "expected": True
        },
        {
            "board": [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], 
            "word": "ABCESEEEFS", 
            "expected": True
        }
    ]
    
    for i, test_case in enumerate(test_cases):
        board = test_case["board"]
        word = test_case["word"]
        expected = test_case["expected"]
        result = word_exists_in_board(board, word)
        status = "PASSED" if result == expected else f"FAILED (got {result}, expected {expected})"
        print(f"Test case {i+1}: {status}")


if __name__ == "__main__":
    # Uncomment the line below to run tests when you're ready
    # test_word_exists_in_board()
    
    # Example usage
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    print(f"Does '{word}' exist in the board? {word_exists_in_board(board, word)}") 