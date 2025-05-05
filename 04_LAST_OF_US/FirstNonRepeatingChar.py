"""
Problem Statement:
------------------
First Non-Repeating Character

Given a string s consisting of lowercase English letters, find the first non-repeating character
in the string and return its index. If it does not exist, return -1.

A non-repeating character is one that appears exactly once in the string.

Examples:
- Input: s = "leetcode"
  Output: 0
  Explanation: The first non-repeating character is 'l', which appears at index 0.

- Input: s = "loveleetcode"
  Output: 2
  Explanation: The first non-repeating character is 'v', which appears at index 2.

- Input: s = "aabb"
  Output: -1
  Explanation: There are no non-repeating characters, so return -1.

Constraints:
- 1 <= s.length <= 10^5
- s consists of only lowercase English letters.
"""

from collections import Counter

def first_non_repeating_char(text: str) -> int:
    """
    Find the first non-repeating character in the given string and return its index.
    If there is no non-repeating character, return -1.
    
    Args:
        s: A string consisting of lowercase English letters
        
    Returns:
        The index of the first non-repeating character, or -1 if none exists
    """

    char_count = Counter(text)

    for i, char in enumerate(text):
        if char_count[char] == 1:
            return i

    return -1

# Test cases
def run_tests():
    test_cases = [
        {"input": "leetcode", "expected": 0, "explanation": "The first non-repeating character is 'l'"},
        {"input": "loveleetcode", "expected": 2, "explanation": "The first non-repeating character is 'v'"},
        {"input": "aabb", "expected": -1, "explanation": "There are no non-repeating characters"},
        {"input": "z", "expected": 0, "explanation": "Single character 'z' appears only once"},
        {"input": "aabcbd", "expected": 3, "explanation": "Character 'c' is the first non-repeating character"},
        {"input": "ababcdefd", "expected": 4, "explanation": "Character 'c' is the first non-repeating character"}
    ]
    
    passed = 0
    for i, test in enumerate(test_cases):
        result = first_non_repeating_char(test["input"])
        if result == test["expected"]:
            print(f"Test {i+1} PASSED: {test['input']} → {result}")
            passed += 1
        else:
            print(f"Test {i+1} FAILED: {test['input']} → Got {result}, Expected {test['expected']}")
            print(f"Explanation: {test['explanation']}")
    
    print(f"\n{passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()
