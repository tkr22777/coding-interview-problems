from sortedcontainers import SortedDict
from collections import defaultdict

class Solution:
    def frequencySort(self, s: str) -> str:
        char_freq = defaultdict(int)
        sorted_dict = SortedDict()
        sorted_dict[1] = set()
        for ch in s:
            char_freq[ch] += 1
            freq_val = char_freq[ch]
            if char_freq[ch] > 1:
                if freq_val not in sorted_dict:
                    sorted_dict[freq_val] = set()
                sorted_dict[freq_val].add(ch)
                sorted_dict[freq_val - 1].remove(ch)
            else:
                sorted_dict[1].add(ch)
        # print(char_freq)
        # print(sorted_dict)
        out_chars = []
        for k, v in sorted_dict.items():
            for a_char in v:
                out_chars += k * [a_char]

        return "".join(reversed(out_chars))
        # return out_str


s = Solution()
print(s.frequencySort("tree")) 