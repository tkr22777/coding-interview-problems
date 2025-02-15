from collections import defaultdict
import heapq

class Solution:
    def largestPalindromic(self, num: str) -> str:
        char_freq = defaultdict(int)

        for digit in num:
            char_freq[digit] += 1

        # print(char_freq)
        even_max_heap = []
        odd_max = None
        for key, val in char_freq.items():
            # print(f"key: {key}, val:{val}")
            if val % 2 == 1 and (odd_max == None or key > odd_max):
                odd_max = key

            if val > 1:
                heapq.heappush(even_max_heap, (-1 * int(key), val))

        # print(even_max_heap)
        prefix = []

        if even_max_heap[0][0] != 0:
            while len(even_max_heap) > 0:
                key, val = heapq.heappop(even_max_heap)
                key = -1 * key
                val = val // 2
                for _ in range(val):
                    prefix.append(str(key))

        # print(prefix)
        post_fix = reversed(prefix)
        if odd_max:
            prefix.append(odd_max)

        prefix.extend(post_fix)
        return "".join(prefix)


s = Solution()
print(s.largestPalindromic("444947137"))
print(s.largestPalindromic("00009"))
print(s.largestPalindromic("0000997")) 