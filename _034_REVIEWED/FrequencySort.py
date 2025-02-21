from collections import defaultdict, Counter

# https://leetcode.com/problems/sort-characters-by-frequency/

class Solution:
    def frequencySort(self, input: str) -> str:
        # Alternative solution using Counter
        char_freq = Counter(input)
        sorted_chars = sorted(char_freq.items(), key=lambda x: (-x[1], x[0]))
        return ''.join(char * freq for char, freq in sorted_chars)

s = Solution()
print(s.frequencySort("tree") == "eert")
print(s.frequencySort("cccaaa") == "aaaccc")
print(s.frequencySort("Aabb") == "bbAa")
