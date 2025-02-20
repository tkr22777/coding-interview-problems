from typing import List

# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Such a good mid-level engineering problem.
# Good exmaple of a sliding window problem.
# Good example of converting characters to unicode/indices.
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # print(f"s len: {len(s)} p len: {len(p)}")
        if len(p) > len(s):
            return []

        indices = []
        p_rep = 26 * [0]
        for ch in p:
            p_rep[ord(ch) - ord('a')] += 1

        s_window_rep = 26 * [0]
        for i in range(len(p) - 1):
            s_window_rep[ord(s[i]) - ord('a')] += 1

        # i goes from 0 to len(s) - len(p)
        for i in range(len(s) - len(p) + 1):
            j = i + len(p) - 1
            # print(f"i: {i} j: {j} diff: {diff}")

            # Add the rightmost character to the window
            s_window_rep[ord(s[j]) - ord('a')] += 1

            # print(s_win_rep)
            if p_rep == s_window_rep:
                indices.append(i)
            
            # Remove the leftmost character from the window
            s_window_rep[ord(s[i]) - ord('a')] -= 1

        return indices 

s = Solution()
print(s.findAnagrams("cbaebabacd", "abc") == [0, 6])
print(s.findAnagrams("abab", "ab") == [0, 1, 2])