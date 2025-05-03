from typing import List

"""
# Such a good mid-level engineering problem.

Problem: Given two strings 's' and 'p', find all start indices of p's anagrams in s.
Approach: Sliding window with character frequency counting.
Time: O(n) where n is length of string s
Space: O(1) - fixed size array for character frequencies
"""

class Solution:
    LOWERCASE_LETTERS_COUNT = 26

    def findAnagrams(self, text: str, pattern: str) -> List[int]:
        if len(pattern) > len(text):
            return []

        anagram_indices = []
        pattern_freq = [0] * self.LOWERCASE_LETTERS_COUNT
        window_freq = [0] * self.LOWERCASE_LETTERS_COUNT
        
        # Initialize frequency arrays for first window
        for i in range(len(pattern)):
            pattern_freq[ord(pattern[i]) - ord('a')] += 1
            window_freq[ord(text[i]) - ord('a')] += 1

        # Check if first window is an anagram
        if pattern_freq == window_freq:
            anagram_indices.append(0)
            
        # Slide window: remove leftmost character, add rightmost character
        for i in range(len(text) - len(pattern)):
            window_freq[ord(text[i]) - ord('a')] -= 1
            window_freq[ord(text[i + len(pattern)]) - ord('a')] += 1
            
            if pattern_freq == window_freq:
                anagram_indices.append(i + 1)

        return anagram_indices


def test_find_anagrams():
    solution = Solution()
    assert solution.findAnagrams("cbaebabacd", "abc") == [0, 6], "Test case 1 failed"
    assert solution.findAnagrams("abab", "ab") == [0, 1, 2], "Test case 2 failed"
    print("All test cases passed!")


if __name__ == "__main__":
    test_find_anagrams()