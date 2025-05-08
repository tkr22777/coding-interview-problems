import java.util.*;

/**
 * LeetCode: Decode String
 * Given an encoded string, return its decoded string.
 * The encoding rule is: k[encoded_string], where encoded_string inside the brackets is repeated k times.
 */
class DecodeString {
    
    /**
     * Core algorithm to decode the string - simplified into a single method
     * Time Complexity: O(n), where n is the length of the string
     * Space Complexity: O(n) for the stack
     */
    public String decodeString(String s) {
        Deque<Object> stack = new ArrayDeque<>();
        int index = 0;
        
        while (index < s.length()) {
            char currentChar = s.charAt(index);
            
            if (Character.isDigit(currentChar)) {
                // Process number (inline)
                int num = 0;
                while (index < s.length() && Character.isDigit(s.charAt(index))) {
                    num = num * 10 + (s.charAt(index) - '0');
                    index++;
                }
                stack.push(num);
            } else if (currentChar == '[') {
                stack.push('[');
                index++;
            } else if (currentChar == ']') {
                // Process closing bracket (inline)
                StringBuilder decodedString = new StringBuilder();
                
                // Pop strings until we reach '['
                while (!stack.isEmpty() && !(stack.peek() instanceof Character)) {
                    decodedString.append(stack.pop());
                }
                
                // Since we built the string in reverse order, reverse it
                decodedString.reverse();
                
                // Remove the '[' marker
                if (!stack.isEmpty()) {
                    stack.pop(); // Pop '['
                }
                
                // Get repetition count
                int repetitions = stack.isEmpty() ? 1 : 
                                 (stack.peek() instanceof Integer) ? (Integer) stack.pop() : 1;
                
                // Repeat the string (inline)
                StringBuilder repeatedString = new StringBuilder();
                String strToRepeat = decodedString.toString();
                for (int i = 0; i < repetitions; i++) {
                    repeatedString.append(strToRepeat);
                }
                
                stack.push(repeatedString.toString());
                index++;
            } else {
                // Process letters (inline)
                int start = index;
                while (index < s.length() && Character.isLetter(s.charAt(index))) {
                    index++;
                }
                stack.push(s.substring(start, index));
            }
        }
        
        // Combine remaining strings (inline)
        StringBuilder result = new StringBuilder();
        Object[] remainingItems = stack.toArray();
        
        // Process in reverse order since we're using a stack
        for (int i = remainingItems.length - 1; i >= 0; i--) {
            result.append(remainingItems[i]);
        }
        
        return result.toString();
    }
    
    //=========================================================================================
    //=========================== Test Driver Code Below ======================================
    //=========================================================================================

    public static void main(String[] args) {
        runAllTests();
        System.out.println("All tests passed!");
    }
    
    private static void runAllTests() {
        DecodeString solution = new DecodeString();
        
        // Basic nested encoding
        assertEquals("accaccacc", solution.decodeString("3[a2[c]]"));
        
        // Multiple encodings in sequence
        assertEquals("abcabccdcdcdef", solution.decodeString("2[abc]3[cd]ef"));
        
        // Text before and after encoding
        assertEquals("abccdcdcdxyz", solution.decodeString("abc3[cd]xyz"));
        
        // Empty string
        assertEquals("", solution.decodeString(""));
        
        // No encoding, just plain text
        assertEquals("abcdefg", solution.decodeString("abcdefg"));
        
        // Multiple nested encodings
        assertEquals("aaabaaab", solution.decodeString("2[3[a]b]"));
        
        // Large numbers
        assertEquals("aaaaaaaaaa", solution.decodeString("10[a]"));
        
        // Complex nesting
        assertEquals("bbaббаbba", solution.decodeString("3[2[b]1[a]]"));
        
        // Consecutive numbers as single number
        assertEquals("aaaaaaaaaaaaaaaaaaaa", solution.decodeString("20[a]"));
        
        // Extreme nesting
        assertEquals("aaaa", solution.decodeString("2[2[2[a]]]"));
    }
    
    /**
     * Simple assertion utility for string equality
     */
    private static void assertEquals(String expected, String actual) {
        assert expected.equals(actual) : 
            "Strings differ: expected \"" + expected + "\", got \"" + actual + "\"";
    }
}

