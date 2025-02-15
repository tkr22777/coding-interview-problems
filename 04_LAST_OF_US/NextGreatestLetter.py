from typing import List

# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters) - 1

        while l <= r:
            mid = (l + r) // 2
            if ord(target) >= ord(letters[mid]):
                l = mid + 1
            else:
                r = mid - 1

        if l >= len(letters):
            return letters[0]
        else:
            return letters[l]


s = Solution()
print(s.nextGreatestLetter(letters=["c", "f", "j"], target="a") == "c")
print(s.nextGreatestLetter(letters=["c", "f", "j"], target="c") == "f")
print(s.nextGreatestLetter(letters=["c", "f", "j"], target="d") == "f")
