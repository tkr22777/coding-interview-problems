from typing import List

"""
# Such a good mid-level engineering problem.

Problem: Given two strings 's' and 'p', find all start indices of p's anagrams in s.
Approach: Sliding window with character frequency counting.
Time: O(n) where n is length of string s
Space: O(1) - fixed size array for character frequencies
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        indices = []
        # Count frequencies of characters in pattern p
        p_freq = [0] * 26
        s_freq = [0] * 26
        
        # Initialize both frequency arrays for first window
        for i in range(len(p)):
            s_freq[ord(s[i]) - ord('a')] += 1
            p_freq[ord(p[i]) - ord('a')] += 1

        # Check if first window is an anagram
        if p_freq == s_freq:
            indices.append(0)
            
        # Slide window: remove leftmost character, add rightmost character
        for i in range(len(s) - len(p)):
            s_freq[ord(s[i]) - ord('a')] -= 1
            s_freq[ord(s[i + len(p)]) - ord('a')] += 1
            if p_freq == s_freq:
                indices.append(i + 1)

        return indices 

s = Solution()
print(s.findAnagrams("cbaebabacd", "abc") == [0, 6])
print(s.findAnagrams("abab", "ab") == [0, 1, 2])