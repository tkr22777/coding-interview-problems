import java.util.*;

public class WordLadder {

    public static void main(String[] args) {
        List<String> wordList = Arrays.asList("hot","dot","dog","lot","log","cog");
        System.out.println(new WordLadder().ladderLength("hit", "cog", wordList));
    }

    public int ladderLength(String beginWord, String endWord, List<String> wordList) {

        ArrayList<String> wordArList = new ArrayList<>(wordList);
        Map<String, Set<String>> adjMap = new HashMap<>();
        Queue<String> queue = new LinkedList<String>();
        Set<String> visited = new HashSet<String>();

        queue.offer(beginWord);

        int depth = 0;

        while(!queue.isEmpty()) {
            int breadth = queue.size();
            for(int i = 0; i < breadth; ++i) {
                String word = queue.poll();
                if (word.equals(endWord)) {
                    return depth + 1;
                }

                visited.add(word);  //visited after checks

                Set<String> neighbors = adjMap.computeIfAbsent(word, s -> getNeighbors(wordArList, word));
                for(String neighbor: neighbors) {
                    if (!visited.contains(neighbor)) {
                        queue.offer(neighbor);
                    }
                }
            }
            ++depth;
        }
        return 0;
    }

    public Set<String> getNeighbors(ArrayList<String> wordList, String word) {
        Set<String> neighbors = new HashSet<String>();
        for (int i = 0; i < wordList.size(); ++i) {
            if (isNeighbour(word, wordList.get(i))) {
                neighbors.add(wordList.get(i));
            }
        }
        return neighbors;
    }

    public boolean isNeighbour(String wordA, String wordB) {
        int diff = 0;
        for (int i = 0; i < wordA.length(); ++i) {
            if (wordA.charAt(i) != wordB.charAt(i)) {
                ++diff;
            }
        }
        return diff == 1;
    }
}

