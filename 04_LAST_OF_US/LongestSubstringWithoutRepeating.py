"""
Longest Substring Without Repeating Characters

Problem Statement:
Given a string s, find the length of the longest substring without repeating characters.

Examples:
- Input: s = "abcabcbb"
  Output: 3
  Explanation: The answer is "abc", with the length of 3.

- Input: s = "bbbbb"
  Output: 1
  Explanation: The answer is "b", with the length of 1.

- Input: s = "pwwkew"
  Output: 3
  Explanation: The answer is "wke", with the length of 3.
  Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces.
"""


def length_of_longest_substring(s: str) -> int:
    """
    Find the length of the longest substring without repeating characters.
    
    Args:
        s: A string
        
    Returns:
        The length of the longest substring without repeating characters
    
    Approach hints:
    - Consider using a sliding window approach
    - You'll need to track characters you've seen
    - Think about how to efficiently update your window when you encounter a repeat
    """
    # Set to store characters in the current window
    char_set = set()
    longest_substring = 0

    # Handle empty string case
    if len(s) == 0:
        return longest_substring

    # Sliding window approach with two pointers:
    # i = left pointer (start of window)
    # j = right pointer (end of window)
    i = 0
    for j, char in enumerate(s):
        # If we find a duplicate character
        if char in char_set:
            # Update the longest substring found so far
            longest_substring = max(longest_substring, j - i)
            
            # Shrink the window from the left until we remove the duplicate character
            # This removes all characters up to and including the first occurrence of the duplicate
            while s[i] != char:
                char_set.remove(s[i])
                i += 1
                
            # Move past the duplicate character
            i += 1
            
            # Note: We don't need to remove the character from the set here
            # since we'll add it back immediately after
        
        # Add current character to the set
        char_set.add(char)

    # Consider the final window length before returning
    return max(longest_substring, len(s) - i)


# Test cases
def test_length_of_longest_substring():
    test_cases = [
        {"input": "abcabcbb", "expected": 3},
        {"input": "bbbbb", "expected": 1},
        {"input": "pwwkew", "expected": 3},
        {"input": "", "expected": 0},
        {"input": "au", "expected": 2},
        {"input": "dvdf", "expected": 3},
        {"input": "anviaj", "expected": 5},
        {"input": "aab", "expected": 2},
        {"input": "tmmzuxt", "expected": 5}
    ]
    
    for i, test_case in enumerate(test_cases):
        s = test_case["input"]
        expected = test_case["expected"]
        result = length_of_longest_substring(s)
        status = "PASSED" if result == expected else f"FAILED (got {result}, expected {expected})"
        print(f"Test case {i+1}: {status}")


if __name__ == "__main__":
    # Uncomment the line below to run tests when you're ready
    test_length_of_longest_substring()
    
    # Alternatively, you can test with your own examples
    s = "abcabcbb"
    print(f"Length of longest substring without repeating characters in '{s}': {length_of_longest_substring(s)}")
