import java.util.*;

public class ValidParentheses {

    public static void main(String[] args) {
        System.out.println(new ValidParentheses().isValid("[[()]]"));
    }

    public boolean isValid(String s) {
        Set<Character> open = new HashSet(Arrays.asList('(', '{', '['));
        Set<Character> closed = new HashSet(Arrays.asList(')', '}', ']'));

        Stack<Character> stk = new Stack();
        for (int i = 0; i < s.length(); i++) {

            Character charI = s.charAt(i);
            if (open.contains(charI)) {
                stk.push(charI);
            } else if (closed.contains(charI) && stk.size() > 0 && openCloseMatch(stk.peek(), charI)) {
                stk.pop();
            } else {
                return false;
            }
        }

        return stk.size() == 0;
    }

    private static boolean openCloseMatch(Character open, Character close) {

        if ((open == '[' && close == ']') ||
            (open == '{' && close == '}') ||
            (open == '(' && close == ')')) {
            return true;
        } else {
            return false;
        }
    }
}

