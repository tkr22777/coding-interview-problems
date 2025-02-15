# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/
class Solution4:
    def minimumLength(self, s: str) -> int:
        i = 0
        j = len(s) - 1
        while i < len(s) - 1 and j >= 0 and s[i] == s[j]:
            while i < len(s) - 1 and s[i] == s[i + 1] and i + 1 < j:
                i += 1

            while j >= 0 and s[j] == s[j - 1] and i < j - 1:
                j -= 1

            i += 1
            j -= 1
            if i == j:
                return 1
            if i > j:
                return 0

        return j - i + 1


s = Solution4()
print(2 == s.minimumLength("ca"))
print(1 == s.minimumLength("cac"))
print(0 == s.minimumLength("cabaabac"))
print(3 == s.minimumLength("aabccabba"))
print(1 == s.minimumLength("c"))