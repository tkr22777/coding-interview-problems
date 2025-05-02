# https://leetcode.com/problems/find-and-replace-in-string/description/
"""
Problem Summary:
Given a string, perform multiple find-and-replace operations simultaneously. 
Each operation consists of:
- Index: Starting position in the string
- Source: Substring to find at that position
- Target: Replacement string
Only replace if the source exactly matches at the given index.
Operations are independent and don't affect each other.
"""
from typing import List

class Solution:
    def findReplaceString(
        self,
        input: str,
        indices: List[int],
        sources: List[str],
        targets: List[str]
    ) -> str:
        # Create a mapping of index to (source, target) 
        # This helps when indices are not in order
        operations = {}
        for i, s, t in zip(indices, sources, targets):
            operations[i] = (s, t)
        
        # Build result by processing the string from left to right
        result = []
        i = 0
        while i < len(input):
            if i in operations and input[i:i+len(operations[i][0])] == operations[i][0]:
                # Match found - add replacement and skip source length
                result.append(operations[i][1])
                i += len(operations[i][0])
            else:
                # No match - keep original character
                result.append(input[i])
                i += 1
                
        return ''.join(result)


# Test cases
s = Solution()

input = "abcd"
indices = [0, 2]
sources = ["a", "cd"]
targets = ["eee", "ffff"]
print("1st case:", "eeebffff" == s.findReplaceString(input, indices, sources, targets))

input = "abcd"
indices = [0, 2]
sources = ["ab", "ec"]
targets = ["eee", "ffff"]
print("2nd case:", "eeecd" == s.findReplaceString(input, indices, sources, targets))

input = "vmokgggqzp"
indices = [3, 5, 1]
sources = ["kg", "ggq", "mo"]
targets = ["s", "so", "bfr"]
print("3rd case:", "vbfrssozp" == s.findReplaceString(input, indices, sources, targets))
