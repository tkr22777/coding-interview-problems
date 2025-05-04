"""
Frequency Sort
Sort a string by decreasing character frequency (most frequent first).
Example: "tree" -> "eert", "cccaaa" -> "aaaccc" or "cccaaa"
"""
from collections import Counter

# https://leetcode.com/problems/sort-characters-by-frequency/

class Solution:
    def frequencySort(self, input_str: str) -> str:
        # Count frequency of each character
        char_frequency = Counter(input_str)
        
        # Sort characters by frequency (descending) then by character (ascending)
        sorted_items = sorted(
            char_frequency.items(), 
            key=lambda item: (-item[1], item[0])
        )
        
        # Build result string by repeating each character by its frequency
        result = []
        for char, freq in sorted_items:
            result.append(char * freq)
            
        return ''.join(result)


def test_frequency_sort():
    s = Solution()
    
    test_cases = [
        ("tree", "eert"),              # Basic case
        ("cccaaa", "aaaccc"),          # Same frequencies, alphabetically
        ("Aabb", "bbAa"),              # Case sensitivity
        ("", ""),                      # Empty string
        ("a", "a"),                    # Single character
        ("aaa", "aaa"),                # All same character
        ("loveleetcode", "eeeelloocdtv") # Mixed characters
    ]
    
    for input_str, expected in test_cases:
        result = s.frequencySort(input_str)
        assert result == expected, f"For '{input_str}': got '{result}', expected '{expected}'"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_frequency_sort()
