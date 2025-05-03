"""
Group Anagrams
Group strings by their anagram status (same letters, different order).
Example: ["eat","tea","tan","ate","nat","bat"] -> [["eat","tea","ate"],["tan","nat"],["bat"]]
"""

class Solution(object):
    def groupAnagrams(self, strs):
        anagram_map = {}
        for s in strs:
            key = ''.join(sorted(s))
            anagram_map.setdefault(key, []).append(s)
        return list(anagram_map.values())


def test_group_anagrams():
    s = Solution()
    
    test_cases = [
        # Basic cases
        (["eat", "tea", "tan", "ate", "nat", "bat"], 3),  # 3 groups
        ([], 0),  # Empty
        (["a", "b", "c"], 3),  # No anagrams
        (["abc", "cba", "bca"], 1),  # All same anagram
        (["Abc", "abc"], 2)  # Case-sensitive
    ]
    
    for input_strs, expected_count in test_cases:
        result = s.groupAnagrams(input_strs)
        assert len(result) == expected_count, f"Expected {expected_count} groups, got {len(result)}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_group_anagrams()
