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
    public String decodeString(String s) {
        Stack<Character> theStack = new Stack<Character>();

        for (int i = 0; i < s.length(); i++) {
            Character current = s.charAt(i);
            if (current == ']') { // unroll
                String toRepeat = pullRepeatString(theStack);
                theStack.pop(); // popping the '[' char
                int repeatCount = pullRepeatCount(theStack);
                String repeatedString = repeatString(toRepeat, repeatCount);
                for (int j = 0; j < repeatedString.length(); j++) {
                    theStack.push(repeatedString.charAt(j));
                }
            } else {
                theStack.push(current);
            }
        }

        StringBuilder toReturn = new StringBuilder();
        while (!theStack.isEmpty()) {
            toReturn.append(theStack.pop());
        }
        return toReturn.reverse().toString();
    }

    private int pullRepeatCount(Stack<Character> theStack) {
        StringBuilder sb = new StringBuilder();
        while (!theStack.isEmpty() && Character.isDigit(theStack.peek())) {
            sb.append(theStack.pop());
        }
        return Integer.parseInt(sb.reverse().toString()); //data pushed into stacked gets reversed
    }

    private String pullRepeatString(Stack<Character> theStack) {
        StringBuilder sb = new StringBuilder();
        while (!theStack.isEmpty() && Character.isAlphabetic(theStack.peek())) {
            sb.append(theStack.pop());
        }
        return sb.reverse().toString(); //data pushed into stacked gets reversed
    }

    private String repeatString(String s, int num) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < num; i++) {
            sb.append(s);
        }
        return sb.toString();
    }
}

