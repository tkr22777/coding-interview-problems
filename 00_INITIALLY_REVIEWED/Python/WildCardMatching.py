from functools import lru_cache

class Solution(object):
    def isMatch(self, text, pattern):
        """
        Determines if the input text matches the given pattern with wildcards.
        """
        # Use functools.lru_cache for automatic memoization
        @lru_cache(maxsize=None)
        def match(text_idx, pattern_idx):
            """
            Recursively checks if the text matches the pattern starting from the given indices.
            """
            # Base case: both text and pattern are exhausted
            if text_idx == len(text) and pattern_idx == len(pattern):
                return True
                
            # If pattern is exhausted but text hasn't, no match
            if pattern_idx >= len(pattern):
                return False
                
            # If text is exhausted, the only way to match is if all remaining pattern chars are *
            if text_idx >= len(text):
                return all(char == '*' for char in pattern[pattern_idx:])
                
            # Current characters to compare
            current_pattern = pattern[pattern_idx]
            
            # Handle wildcard character *
            if current_pattern == '*':
                # Try three cases:
                # 1. Skip the * (don't use it)
                # 2. Use * to match exactly one character
                # 3. Use * to match one or more characters
                return (match(text_idx, pattern_idx + 1) or 
                        match(text_idx + 1, pattern_idx + 1) or 
                        match(text_idx + 1, pattern_idx))
                        
            # Handle ? wildcard or exact character match
            if current_pattern == '?' or current_pattern == text[text_idx]:
                return match(text_idx + 1, pattern_idx + 1)
                
            # No match found
            return False
            
        # Start the matching from the beginning of both strings
        return match(0, 0)

