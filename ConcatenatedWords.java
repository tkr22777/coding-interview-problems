import java.io.*;
import java.util.*;
import java.util.stream.*;

class ConcatenatedWords {

    public static void main(String[] args) {
        String[] words = {"cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"};
        System.out.println(new ConcatenatedWords().findAllConcatenatedWordsInADict(words));
    }

    class Trie {
        HashMap<Character, Trie> nexts = new HashMap<Character, Trie>();
        boolean complete = false;
    }

    Trie root = new Trie();

    private void addWord(Trie node, String word) {
        Trie curr = node;
        for (int i = 0; i < word.length(); i++) {
            curr = curr.nexts.computeIfAbsent(word.charAt(i), t -> new Trie());
        }
        curr.complete = true;
    }

    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        Arrays.stream(words).forEach( w -> addWord(root, w));
        return Arrays.stream(words)
            .filter(w -> isConcatenated(root, w, 0) > 1)
            .collect(Collectors.toList());
    }

    private int isConcatenated(Trie root, String word, int start) { // start inclusive

        for (int i = start + 1; i <= word.length(); ++i) { //begining from start + 1 to discard empty string
            if (this.isSubStringAWord(root, word, start, i)) { // substring is word from start to i - 1 
                if (i == word.length()) { //found the word itself as substring
                    return 1;
                } 

                int count = this.isConcatenated(root, word, i);
                if (count > 0) {
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

