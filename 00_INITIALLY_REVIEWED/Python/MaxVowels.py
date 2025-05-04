"""
Maximum Vowels in a Substring of Given Length
Find the maximum number of vowels in any substring of the given string with length k.
Vowels are 'a', 'e', 'i', 'o', and 'u'.
Example: "abciiidef", k=3 -> 3 (substring "iii" has 3 vowels)

Time Complexity: O(n) where n is the length of the string
Space Complexity: O(1) - using only constant extra space
"""

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        Calculate the maximum number of vowels in any substring of length k.
        
        Args:
            s: Input string
            k: Length of the substring to consider
            
        Returns:
            Maximum number of vowels in any substring of length k
        """
        # Edge cases
        if not s or k <= 0 or k > len(s):
            return 0
            
        # Set of vowels for O(1) lookup
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Initialize: count vowels in the first window [0, k-1]
        current_count = 0
        for i in range(k):
            if s[i] in vowels:
                current_count += 1
                
        # The maximum starts with the count from first window
        max_vowels = current_count
        
        # Slide the window through the string
        for i in range(k, len(s)):
            # Add the new character
            if s[i] in vowels:
                current_count += 1
                
            # Remove the character that's no longer in the window
            if s[i - k] in vowels:
                current_count -= 1
                
            # Update maximum
            max_vowels = max(max_vowels, current_count)
            
        return max_vowels


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