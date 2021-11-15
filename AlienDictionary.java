import java.util.*;
/*
    The problem: https://leetcode.com/problems/alien-dictionary/
    The words provided sorted lexicographically, not the characters in the words.
    From the sorted word order, figure out the possible characters order.
*/

class AlienDictionary {

    public static void main(String[] args) {
        String[] words = { "wrt","wrf","er","ett","rftt" };
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

        StringBuilder sb = new StringBuilder();
        dfsOrdered.forEach(c -> sb.append(c));
        return sb.reverse().toString();// reversing the dfs depth first to last for char ordering
    }

    private int dfs(Character cur,
                   Map<Character, Set<Character>> adjMat,
                   Set<Character> visited,
                   Set<Character> inDFSStack,
                   List<Character> dfsOrdered) {

        if (inDFSStack.contains(cur)) return -1; //there's a cycle
        inDFSStack.add(cur);

        if (visited.contains(cur)) return 0; //already visited
        visited.add(cur);
        
        Set<Character> children = adjMat.getOrDefault(cur, new HashSet<>());
        for (Character child: children) {
            if (dfs(child, adjMat, visited, inDFSStack, dfsOrdered) == -1) {
                return -1;
            }
        }
        
        inDFSStack.remove(cur);
        dfsOrdered.add(cur); //The deepest in the call-stack is pushed first
        return 0;
    }

    private Map<Character, Set<Character>> convertToAdjMat(String[] words) {
        Map<Character, Set<Character>> adjMat = new HashMap<>();

        for (int i = 1; i < words.length; i++) {
            String prevWord = words[i - 1];
            String currWord = words[i];
            int maxIndex = Math.min(prevWord.length(), currWord.length());
            for (int j = 0; j < maxIndex; j++) {
                if (j >= prevWord.length() || j >= currWord.length()) {
                    break;
                }
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

