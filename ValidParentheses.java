import java.util.*;

public class ValidParentheses {

    public static void main(String[] args) {
        System.out.println("[[()]]:" + new ValidParentheses().isValid("[[()]]"));
        System.out.println("[[()()][]()]:" + new ValidParentheses().isValid("[[()()][]()]"));
        System.out.println("[[]([])]:" + new ValidParentheses().isValid("[[]([])]"));
        System.out.println("[{[}]:" + new ValidParentheses().isValid("[{[}]"));
        System.out.println("[[(([])]:" + new ValidParentheses().isValid("[[(([])]"));
    }

    public boolean isValid(String string) {
        Set<Character> open = new HashSet<>(Arrays.asList('(', '{', '['));
        Set<Character> closed = new HashSet<>(Arrays.asList(')', '}', ']'));

        Stack<Character> charStack = new Stack<>();
        for (int i = 0; i < string.length(); i++) {
            Character charI = string.charAt(i);
            if (open.contains(charI)) {
                charStack.push(charI);
                continue;
            }

            boolean closedAndMatches = closed.contains(charI)
                    && charStack.size() > 0
                    && openCloseMatch(charStack.peek(), charI);

            if (closedAndMatches) {
                charStack.pop();
            } else {
                return false;
            }
        }
        return charStack.size() == 0;
    }

    private static boolean openCloseMatch(Character open, Character close) {
        return (open == '[' && close == ']') ||
                (open == '{' && close == '}') ||
                (open == '(' && close == ')');
    }
}
