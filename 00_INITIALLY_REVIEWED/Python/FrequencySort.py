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


    s = Solution()
print(s.frequencySort("tree") == "eert")
print(s.frequencySort("cccaaa") == "aaaccc")
print(s.frequencySort("Aabb") == "bbAa")
