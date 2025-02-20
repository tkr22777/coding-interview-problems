# https://leetcode.com/problems/find-and-replace-in-string/description/
from typing import List

class Solution:
    def findReplaceString(
        self,
        input: str,
        indices: List[int],
        sources: List[str],
        targets: List[str]
    ) -> str:
        # Sort replacements by index to process them from left to right
        replacements = sorted(zip(indices, sources, targets))
        
        parts = []
        last_pos = 0
        
        # Process each replacement in order
        for index, source, target in replacements:
            parts.append(input[last_pos:index])
            
            if input[index:index + len(source)] == source:
                parts.append(target)
            else:
                parts.append(input[index:index + len(source)])

            last_pos = index + len(source)
        
        # Add any remaining characters after the last replacement
        parts.append(input[last_pos:])
        
        return ''.join(parts)


s = Solution()

input = "abcd"
indices = [0, 2]
sources = ["a", "cd"]
targets = ["eee", "ffff"]

print("1st case:" + str("eeebffff" == s.findReplaceString(input, indices, sources, targets)))

input = "abcd"
indices = [0, 2]
sources = ["ab", "ec"]
targets = ["eee", "ffff"]
print("2nd case:" + str("eeecd" == s.findReplaceString(input, indices, sources, targets)))

input = "vmokgggqzp"
indices = [3, 5, 1]
sources = ["kg", "ggq", "mo"]
targets = ["s", "so", "bfr"]
print("3rd case:" + str("vbfrssozp" == s.findReplaceString(input, indices, sources, targets)))
