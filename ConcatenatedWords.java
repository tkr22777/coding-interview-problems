import java.io.*;
import java.util.*;
import java.util.stream.*;

class ConcatenatedWords {

    class Trie {
        HashMap<Character, Trie> nexts = new HashMap<Character, Trie>();
        boolean complete = false;
    }

    Trie root = new Trie();

    public static void main(String[] args) {
        String[] words = {"cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"};
        System.out.println(new ConcatenatedWords().findAllConcatenatedWordsInADict(words));
    }

    private void addWord(Trie root, String word) {
        Trie curr = root;
        for (int i = 0; i < word.length(); i++) {
            curr = curr.nexts.computeIfAbsent(word.charAt(i), t -> new Trie());
        }
        curr.complete = true;
    }

    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        Arrays.stream(words).forEach(word -> addWord(root, word));
        return Arrays.stream(words)
            .filter(word -> isConcatenated(root, word, 0) > 1)
            .collect(Collectors.toList());
    }

    private int isConcatenated(Trie root, String word, int start) { // start inclusive

        for (int i = start + 1; i <= word.length(); ++i) { //begining from start + 1 to discard empty string
            if (this.isSubStringAWord(root, word, start, i)) { // substring is word from start to i - 1 
                if (i == word.length()) { //from start to word.length() is a substring
                    return 1;
                } 

                int count = this.isConcatenated(root, word, i);
                if (count > 0) { /* greater than 0 means the substring is concatenated */
                    return 1 + count;
                }
            }
        }
        return 0;
    }

    private boolean isSubStringAWord(Trie root, String word, int start, int end) { //start to end - 1

        Trie current = root;
        for(int i = start; i < end; i++) {
            current = current.nexts.get(word.charAt(i));
            if (current == null) {
                return false;
            }
        }
        return current.complete;
    }
}

