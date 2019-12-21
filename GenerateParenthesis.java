import java.util.*;

class GenerateParenthesis {

    public static void main(String[] args) {
        List<String> parenthesis = new GenerateParenthesis().generateParenthesis(4);
        System.out.println("All possible parenthesis combination:");
        parenthesis.stream().forEach(p -> System.out.println(p));
    }

    public List<String> generateParenthesis(int n) {
        return generateParenthesis(n, 0);
    }

    private List<String> generateParenthesis(int open, int close) {

        //Open brackets are not required anymore, only close brackets are required
        if (open == 0) {
            char[] chars = new char[close];
            Arrays.fill(chars, ')');
            return Arrays.asList(new String(chars));
        }

        //Open > 0
        List<String> results = new ArrayList<String>();

        List<String> usedOpens = generateParenthesis(open - 1, close + 1);
        for (String usedOpen: usedOpens) {
            results.add("(" + usedOpen);
        }

        if (close > 0) {
            List<String> rUsedCloses =  generateParenthesis(open, close - 1);
            for (String rUsedClose: rUsedCloses) {
                results.add(")" + rUsedClose);
            }
        }

        return results;
    }
}


