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
from typing import List, Tuple, Dict

class Solution:
    def findReplaceString(
        self,
        text: str,
        indices: List[int],
        sources: List[str],
        targets: List[str]
    ) -> str:
        # Map each index to its corresponding (source, target) pair
        replacements: Dict[int, Tuple[str, str]] = {
            idx: (src, tgt) 
            for idx, src, tgt in zip(indices, sources, targets)
        }
        
        # Process string left to right, applying replacements when matches found
        result = []
        pos = 0
        while pos < len(text):
            if pos in replacements:
                source, target = replacements[pos]
                if text[pos:pos + len(source)] == source:
                    result.append(target)
                    pos += len(source)
                    continue
            result.append(text[pos])
            pos += 1
                
        return ''.join(result)


def test_find_replace_string():
    solution = Solution()
    
    # Test case 1: Multiple successful replacements
    assert solution.findReplaceString(
        "abcd", [0, 2], ["a", "cd"], ["eee", "ffff"]
    ) == "eeebffff", "Test case 1 failed"
    
    # Test case 2: One failed replacement
    assert solution.findReplaceString(
        "abcd", [0, 2], ["ab", "ec"], ["eee", "ffff"]
    ) == "eeecd", "Test case 2 failed"
    
    # Test case 3: Out of order indices
    assert solution.findReplaceString(
        "vmokgggqzp", [3, 5, 1], ["kg", "ggq", "mo"], ["s", "so", "bfr"]
    ) == "vbfrssozp", "Test case 3 failed"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_find_replace_string()
