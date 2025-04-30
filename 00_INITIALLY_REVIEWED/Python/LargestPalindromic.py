# https://leetcode.com/problems/largest-palindromic-number/description/

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
            if val % 2 == 1 and (odd_max is None or key > odd_max):
                odd_max = key

            # Since heapq in Python is a min-heap, we push the negative of the digit value.
            # This causes the largest digit to have the smallest (most negative) value,
            # ensuring it appears at the front of the heap (i.e., we effectively create a max-heap).
            if val > 1:
                heapq.heappush(even_max_heap, (-1 * int(key), val))

        # print(even_max_heap)
        prefix = []

        # Only proceed if heap is not empty and largest digit is not zero
        if even_max_heap and even_max_heap[0][0] != 0:
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
print(s.largestPalindromic("444947137") == "7449447")
print(s.largestPalindromic("00009") == "9")
print(s.largestPalindromic("0000997") == "9007009")