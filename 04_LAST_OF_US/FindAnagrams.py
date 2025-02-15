from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        indices = []
        p_rep = 26 * [0]
        for ch in p:
            p_rep[ord(ch) - ord('a')] += 1
        # print(p_rep)

        s_win_rep = 26 * [0]
        for i in range(len(p) - 1):
            s_win_rep[ord(s[i]) - ord('a')] += 1

        for i in range(len(s) - len(p) + 1):
            j = i + len(p) - 1
            # print(f"i: {i} j: {j} diff: {diff}")
            s_win_rep[ord(s[j]) - ord('a')] += 1
            # print(s_win_rep)
            if p_rep == s_win_rep:
                indices.append(i)
            s_win_rep[ord(s[i]) - ord('a')] -= 1

        return indices 