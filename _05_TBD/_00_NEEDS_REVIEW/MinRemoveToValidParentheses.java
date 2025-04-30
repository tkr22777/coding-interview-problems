package TOClean;

import java.util.HashSet;
import java.util.Set;

// https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

public class MinRemoveToValidParentheses {
    public String minRemoveToMakeValid(String s) {
        boolean[] charsToRemove = new boolean[s.length()];
        Set<Integer> openChars = new HashSet<Integer>();

        for (int i = 0; i < s.length(); i++) {
            Character c = s.charAt(i);
            if ( c == '(' ) {
                openChars.add(i);
            } else if ( c == ')' ) {
                if (openChars.size() > 0) { // close parentheses neutralizes a open one
                    openChars.remove(openChars.iterator().next());
                } else { // if there are no open one the close parentheses should be removed
                    charsToRemove[i] = true;
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (!openChars.contains(i) && !charsToRemove[i]) {
                sb.append(s.charAt(i));
            }
        }

        return sb.toString();
    }
}