import java.util.*;
/*
    The problem: https://leetcode.com/problems/alien-dictionary/
    The words provided are sorted lexicographically, but the characters in the words are not sorted.
    From the sorted word order, figure out the possible characters order.
    Assumption: the given dictionary results to a valid deterministic order of characters
*/

class AlienDictionary {

    public static void main(String[] args) {
        String[] words = {
            "wrt",
            "wrf",
            "er",
            "ett",
            "rftt"
        };
        System.out.println("words: " + Arrays.toString(words) + " char order:" + new AlienDictionary().alienOrder(words));

        words = new String[]{
            "wrt",
            "wrf",
            "mt",
            "mr"
        };
        System.out.println("words: " + Arrays.toString(words) + " char order:" + new AlienDictionary().alienOrder(words));
        System.out.println(new AlienDictionary().alienOrder(words));
    }

    public String alienOrder(String[] words) {
        Map<Character, Set<Character>> adjMat = convertToAdjMat(words);
        Set<Character> visited = new HashSet<>();
        List<Character> dfsOrdered = new LinkedList<>();
        
        for (char node: adjMat.keySet()) {
            if (dfs(node, adjMat, visited, new HashSet<>(), dfsOrdered) == -1 ) {
                return "";  /* there is a cycle (in the order) */
            };
        }

        StringBuilder stringBuilder = new StringBuilder();
        dfsOrdered.forEach(c -> stringBuilder.append(c));
        return stringBuilder.reverse().toString();// reversing the dfs depth first to, depth last for char ordering
    }

    /*
    * The visited set is mostly an optimization/memoization, it solves without the visited set
    * on the inDFS stack, the deepest in the call-stack is pushed first
    */
    private int dfs(Character cur,
                   Map<Character, Set<Character>> adjMat,
                   Set<Character> visited,
                   Set<Character> dfsStack,
                   List<Character> dfsOrdered) {

        if (dfsStack.contains(cur)) return -1; //there's a cycle
        dfsStack.add(cur);

        if (visited.contains(cur)) return 0; //already visited, through some other stack, no cycle found
        visited.add(cur);
        
        Set<Character> children = adjMat.getOrDefault(cur, new HashSet<>());
        for (Character child: children) {
            if (dfs(child, adjMat, visited, dfsStack, dfsOrdered) == -1) {
                return -1;
            }
        }
        
        dfsStack.remove(cur);
        dfsOrdered.add(cur); //The deepest in the call-stack is pushed first
        return 0;
    }

    /* the following function returns the adjacency map of the
     dependencies for characters inferred from the dictionary */
    private Map<Character, Set<Character>> convertToAdjMat(String[] words) {
        Map<Character, Set<Character>> adjMat = new HashMap<>();

        for (int i = 1; i < words.length; i++) {
            String prevWord = words[i - 1];
            String currWord = words[i];
            int maxIndex = Math.min(prevWord.length(), currWord.length());
            for (int j = 0; j < maxIndex; j++) {
                if (prevWord.charAt(j) != currWord.charAt(j)) {
                    adjMat.computeIfAbsent(prevWord.charAt(j), v -> new HashSet<>())
                        .add(currWord.charAt(j));
                    break; //as the first diff is found, we cannot infer anything else going forward
                }
            }
        }
        return adjMat;
    }
}
