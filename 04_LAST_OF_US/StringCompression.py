from typing import List

# https://leetcode.com/problems/string-compression/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def compress(self, chars: List[str]) -> int:
        j = 1
        count = 1
        for i in range(1, len(chars)):
            if chars[i] != chars[i - 1]:
                if count > 1:
                    c_str = str(count)
                    for c in c_str:
                        chars[j] = c
                        j += 1
                chars[j] = chars[i]
                count = 1
                j += 1
            else:
                count += 1

        if count > 1:
            c_str = str(count)
            for c in c_str:
                chars[j] = c
                j += 1

        return j

# Test cases can be added here 