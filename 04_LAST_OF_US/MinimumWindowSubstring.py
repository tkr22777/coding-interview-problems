"""
Minimum Window Substring

Problem Statement:
Given two strings s and t, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

Examples:
- Input: s = "ADOBECODEBANC", t = "ABC"
  Output: "BANC"
  Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

- Input: s = "a", t = "a"
  Output: "a"
  Explanation: The entire string s is the minimum window.

- Input: s = "a", t = "aa"
  Output: ""
  Explanation: Both 'a's from t must be included in the window. Since s only has one 'a', return empty string.

Constraints:
- 1 <= s.length, t.length <= 10^5
- s and t consist of uppercase and lowercase English letters.
"""

from collections import Counter
def minimum_window_substring(s: str, t: str) -> str:
    """
    Find the minimum window substring of s that contains all characters of t.
    
    Args:
        s: The source string
        t: The target string
        
    Returns:
        The minimum window substring that contains all characters of t, or "" if no such substring exists
    
    Approach hints:
    - Use a sliding window with two pointers
    - Use a counter to track required characters from t
    - Expand window until all characters are found, then contract to find minimum
    """
    # Create a counter for characters in target string t
    char_count = Counter(t)
    
    # This implementation uses a brute force approach with optimizations:
    # 1. Try each possible starting position i
    # 2. For each i, find the shortest ending position j that contains all required characters
    # 3. Keep track of the shortest valid window found
    
    min_window = None  # Track the minimum valid window found
    
    # Outer loop: try each possible starting position
    for i in range(len(s)):
        # Optimization: skip starting positions with characters not in target t
        if s[i] not in char_count:
            continue
            
        # Reset the counter for each starting position
        range_count = Counter()
        
        # Inner loop: find the shortest ending position that creates a valid window
        for j in range(i + 1, len(s) + 1):
            # Optimization: only update counter for characters we care about
            if s[j - 1] not in char_count:
                continue
                
            # Add the current character to our running count
            range_count[s[j - 1]] += 1
            
            # Optimization: skip if we haven't seen enough unique characters yet
            if len(range_count) < len(char_count):
                continue
                
            # Check if current window contains all required characters
            if all(range_count[char] >= char_count[char] for char in char_count):
                # Found valid window, update minimum if it's shorter
                if min_window is None or j - i < len(min_window):
                    min_window = s[i:j]
                # Optimization: once we find a valid window for this starting position,
                # we don't need to expand further as it would only make the window larger
                break
    
    # Return empty string if no valid window found
    if min_window is None:
        return ""
        
    return min_window


def efficient_minimum_window_substring(s: str, t: str) -> str:
    """
    Find the minimum window substring of s that contains all characters of t.
    Efficient O(n) implementation using sliding window technique.
    
    Args:
        s: The source string
        t: The target string
        
    Returns:
        The minimum window substring that contains all characters of t, or "" if no such substring exists
    """
    # Edge cases
    if not s or not t:
        return ""
    if len(t) > len(s):
        return ""
    
    # Create a counter for characters in target string t
    target_char_map = Counter(t)
    
    # Initialize variables
    required_chars = len(target_char_map)  # Number of unique characters needed
    formed_chars = 0  # Number of unique characters currently satisfied
    window_char_map = Counter()  # Counts characters in current window
    
    # Variables for result
    min_len = float('inf')
    min_start = 0
    
    # Two pointers for sliding window
    left = 0
    right = 0
    
    # Expand the window by moving right pointer
    while right < len(s):
        # Add current character to window count
        char = s[right]
        window_char_map[char] += 1
        
        # Check if this character satisfies a requirement
        if char in target_char_map and window_char_map[char] == target_char_map[char]:
            formed_chars += 1
        
        # Try to contract the window from the left
        while left <= right and formed_chars == required_chars:
            char = s[left]
            
            # Update result if current window is smaller
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_start = left
            
            # Remove leftmost character from window
            window_char_map[char] -= 1
            
            # Check if removing this character breaks a requirement
            if char in target_char_map and window_char_map[char] < target_char_map[char]:
                formed_chars -= 1
            
            # Contract window from the left
            left += 1
        
        # Expand window to the right
        right += 1
    
    # Return result
    return s[min_start:min_start + min_len] if min_len != float('inf') else ""


# Test cases
def test_minimum_window_substring():
    test_cases = [
        {"s": "ADOBECODEBANC", "t": "ABC", "expected": "BANC"},
        {"s": "a", "t": "a", "expected": "a"},
        {"s": "a", "t": "aa", "expected": ""},
        {"s": "aa", "t": "aa", "expected": "aa"},
        {"s": "bba", "t": "ab", "expected": "ba"},
        {"s": "cabwefgewcwaefgcf", "t": "cae", "expected": "cwae"},
        {"s": "abcdcfmqwes", "t": "ccfba", "expected": "abcdcf"}
    ]
    
    print("Testing original implementation:")
    for i, test_case in enumerate(test_cases):
        s = test_case["s"]
        t = test_case["t"]
        expected = test_case["expected"]
        result = minimum_window_substring(s, t)
        status = "PASSED" if result == expected else f"FAILED (got '{result}', expected '{expected}')"
        print(f"Test case {i+1}: {status}")
    
    print("\nTesting efficient implementation:")
    for i, test_case in enumerate(test_cases):
        s = test_case["s"]
        t = test_case["t"]
        expected = test_case["expected"]
        result = efficient_minimum_window_substring(s, t)
        status = "PASSED" if result == expected else f"FAILED (got '{result}', expected '{expected}')"
        print(f"Test case {i+1}: {status}")


if __name__ == "__main__":
    # Uncomment the line below to run tests when you're ready
    test_minimum_window_substring()
    
    # Example usage
    s = "ADOBECODEBANC"
    t = "ABC"
    print(f"\nOriginal solution result: {minimum_window_substring(s, t)}")
    print(f"Efficient solution result: {efficient_minimum_window_substring(s, t)}") 