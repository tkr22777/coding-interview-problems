import java.util.*;
/*
    https://leetcode.com/problems/decode-string/
    Input: s = "3[a2[c]]"
    Output: "accaccacc"
    Input: s = "2[abc]3[cd]ef"
    Output: "abcabccdcdcdef"
    Input: s = "abc3[cd]xyz"
    Output: "abccdcdcdxyz"
*/

class DecodeString {

    public static void main(String[] args) {
        DecodeString solution = new DecodeString();
        System.out.println(solution.decodeString("3[a2[c]]")); // accaccacc
        System.out.println(solution.decodeString("2[abc]3[cd]ef")); // abcabccdcdcdef
        System.out.println(solution.decodeString("abc3[cd]xyz")); // abccdcdcdxyz
    }

    public String decodeString(String s) {
        Stack<Integer> countStack = new Stack<>();
        Stack<StringBuilder> stringStack = new Stack<>();
        StringBuilder currentString = new StringBuilder();
        int count = 0;
        
        for (char ch : s.toCharArray()) {
            if (Character.isDigit(ch)) {
                // Parse multi-digit number
                count = count * 10 + (ch - '0');
            } else if (ch == '[') {
                // Save the current count and start a new string
                countStack.push(count);
                stringStack.push(currentString);
                currentString = new StringBuilder();
                count = 0;
            } else if (ch == ']') {
                // Pop and decode
                StringBuilder temp = currentString;
                currentString = stringStack.pop();
                int repeatCount = countStack.pop();
                
                // Append the decoded string repeatCount times
                for (int i = 0; i < repeatCount; i++) {
                    currentString.append(temp);
                }
            } else {
                // Regular character
                currentString.append(ch);
            }
        }
        
        return currentString.toString();
    }
}

