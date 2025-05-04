"""
Maximum Vowels in a Substring of Given Length
Find the maximum number of vowels in any substring of the given string with length k.
Vowels are 'a', 'e', 'i', 'o', and 'u'.
Example: "abciiidef", k=3 -> 3 (substring "iii" has 3 vowels)

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(1) - using only constant extra space
"""

class Solution:
    def maxVowels(self, input_string: str, window_size: int) -> int:
        """
        Calculate the maximum number of vowels in any substring of length k.
        
        Args:
            input_string: Input string to analyze
            window_size: Length of the substring to consider
            
        Returns:
            Maximum number of vowels in any substring of the given length
        """
        # Edge cases
        if not input_string or window_size <= 0 or window_size > len(input_string):
            return 0
            
        # Set of vowels for O(1) lookup
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Initialize: count vowels in the first window [0, window_size-1]
        vowel_count = 0
        for char_index in range(window_size):
            if input_string[char_index] in vowels:
                vowel_count += 1
                
        # The maximum starts with the count from first window
        max_vowel_count = vowel_count
        
        # Slide the window through the string
        for window_end in range(window_size, len(input_string)):
            # Add the new character at the end of the window
            if input_string[window_end] in vowels:
                vowel_count += 1
                
            # Remove the character that's sliding out of the window
            window_start = window_end - window_size
            if input_string[window_start] in vowels:
                vowel_count -= 1
                
            # Update maximum count seen so far
            max_vowel_count = max(max_vowel_count, vowel_count)
            
        return max_vowel_count


def test_max_vowels():
    """Test the maxVowels function with various test cases."""
    solution = Solution()
    
    # Test case 1: String with consecutive vowels
    assert solution.maxVowels("abciiidef", 3) == 3, "Test case 1 failed: should return 3 for 'iii'"
    
    # Test case 2: Short window
    assert solution.maxVowels("aeiou", 2) == 2, "Test case 2 failed: should return 2 for 'ae'"
    
    # Test case 3: No vowels
    assert solution.maxVowels("bcdfg", 3) == 0, "Test case 3 failed: should return 0 for no vowels"
    
    # Test case 4: Window size equal to string length
    assert solution.maxVowels("aeiou", 5) == 5, "Test case 4 failed: should return 5 for full string"
    
    # Test case 5: Empty string or invalid k
    assert solution.maxVowels("", 3) == 0, "Test case 5 failed: should return 0 for empty string"
    assert solution.maxVowels("hello", 0) == 0, "Test case 6 failed: should return 0 for k=0"
    
    print("All maximum vowels tests passed!")


if __name__ == "__main__":
    test_max_vowels()