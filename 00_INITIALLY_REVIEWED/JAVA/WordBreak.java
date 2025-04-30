import java.util.*;

public class WordBreak {
    public boolean wordBreakBFS(String s, List<String> wordDict) {

        Map<String, Boolean> wordMap = new HashMap<>();
        Map<Integer, Boolean> memo = new HashMap<>();

        int maxWordLen = 0; // optimization

        for (String word: wordDict) {
            wordMap.put(word, true);
            maxWordLen = Math.max(maxWordLen, word.length());
        }

        Queue<int[]> queue = new LinkedList<>();
        // as string.substring is used, substring indexing excludes second index
        for (int i = 1; i <= s.length() && i <= maxWordLen; i++) {
            queue.offer(new int[]{0, i});
        }

        while (queue.size() > 0) {
            int[] values = queue.poll();
            if (wordMap.containsKey(s.substring(values[0], values[1]))) {
                memo.put(values[1],true);

                if (values[1] == s.length()) {
                    return true;
                } else {
                    for (int i = values[1] + 1; i <= s.length()
                            && i <= values[1] + 1 + maxWordLen; i++) {
                        if (memo.containsKey(i)) {
                            continue;
                        }
                        queue.offer(new int[]{values[1], i});
                    }
                }
            }
        }
        return false;
    }

    public boolean wordBreakDFSStack(String s, List<String> wordDict) {

        Map<String, Boolean> wordMap = new HashMap<>();

        for (String word: wordDict) {
            wordMap.put(word, true);
        }

        Stack<int[]> stack = new Stack<>();
        // as string.substring is used, substring indexing excludes second index
        for (int i = 1; i <= s.length(); i++) {
            stack.push(new int[]{0, i});
        }

        while (stack.size() > 0) {
            int[] values = stack.pop();
            if (wordMap.containsKey(s.substring(values[0], values[1]))) {
                if (values[1] == s.length()) {
                    return true;
                } else {
                    for (int i = values[1] + 1; i <= s.length(); i++) {
                        stack.push(new int[]{values[1], i});
                    }
                }
            }
        }
        return false;
    }
}
