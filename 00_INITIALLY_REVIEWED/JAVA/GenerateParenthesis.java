/*
    https://leetcode.com/problems/generate-parentheses/
    for n = 3,
    ((()))
    (()())
    (())()
    ()(())
    ()()()

    genPOC(3, 0)
    -> (
        -> ((
            -> (((
                -> ((()))
            -> (()
                -> (()(
                    -> (()())
                -> (())
                    -> (())(
                        -> (())()
        -> ()
            -> ()(
                -> ()((
                   -> ()(()
                     -> ()(())
                -> ()()
                   -> ()()(
                    -> ()()()

 */
import java.util.*;

class GenerateParenthesis {
    public static void main(String[] args) {
        System.out.println("All possible parenthesis combination:");
        new GenerateParenthesis().generateParenthesis(3)
            .forEach(System.out::println);
    }

    public List<String> generateParenthesis(int n) {
        return generateParenthesis(n, 0);
    }

    private List<String> generateParenthesis(int open, int close) {
        /* Open brackets are not required anymore, only close brackets are required */
        if (open == 0) {
            char[] chars = new char[close];
            Arrays.fill(chars, ')');
            String str = new String(chars);
            return List.of(str);
        }

        //Open > 0
        List<String> results = new ArrayList<String>();

        List<String> usedOpens = generateParenthesis(open - 1, close + 1);
        for (String usedOpen: usedOpens) {
            results.add("(" + usedOpen);
        }

        if (close > 0) {
            List<String> usedCloses =  generateParenthesis(open, close - 1);
            for (String usedClose: usedCloses) {
                results.add(")" + usedClose);
            }
        }
        return results;
    }
}
