# https://leetcode.com/problems/count-binary-substrings/
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return 0
    
        prev = s[0]
        if prev == '1':
            one_candidate = 1
            zero_candidate = 0
        else:
            one_candidate = 0
            zero_candidate = 1

        total = 0
        for bin in s[1:]:
            if bin == '1':
                if prev == '0':
                    total += min(zero_candidate, one_candidate)
                    one_candidate = 1
                else:
                    one_candidate += 1
            else:
                if prev == '1':
                    total += min(zero_candidate, one_candidate)
                    zero_candidate = 1
                else:
                    zero_candidate += 1
            prev = bin
        total += min(zero_candidate, one_candidate)
        return total

# Test cases
s = Solution()
print(s.countBinarySubstrings("00110011"))
print(s.countBinarySubstrings("00110011"))
print(s.countBinarySubstrings("11000"))
print(s.countBinarySubstrings("0011"))
print(s.countBinarySubstrings("001110000"))
print(s.countBinarySubstrings("001101"))
print(s.countBinarySubstrings("101")) 