/*
    https://leetcode.com/problems/concatenated-words/
    Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
    Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
    Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
    "dogcatsdog" can be concatenated by "dog", "cats" and "dog";
    "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
 */

import java.util.*;

class Trie {
    HashMap<Character, Trie> next = new HashMap<Character, Trie>();
    boolean complete = false; //set to true when a word ends here
}

class ConcatenatedWords {
    Trie root = new Trie();

    public static void main(String[] args) {
        String[] words = {"cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"};
        System.out.println(new ConcatenatedWords().findAllConcatenatedWordsInADict(words));
    }

    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        // creating a trie for given words
        for (String word : words) {
            addWord(root, word);
        }

        List<String> list = new ArrayList<String>();
        for (String word: words) {
            if (concatenationCount(root, word, 0) > 1) {
                list.add(word);
            }
        }
        return list;
    }

    private void addWord(Trie root, String word) {
        Trie curr = root;
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            curr = curr.next.computeIfAbsent(c, t -> new Trie());
        }
        curr.complete = true;
    }

    private int concatenationCount(Trie root, String word, int start) { // start is inclusive
        for (int end = start + 1; end <= word.length(); ++end) {
            if (isSubStringAWord(root, word, start, end)) {
                if (end == word.length()) { // at the end so (start, end) has count 1
                    return 1;
                }

                int count = this.concatenationCount(root, word, end);
                if (count > 0) { // rest of the string has concatenation too
                    return 1 + count;
                }
            }
        }
        return 0;
    }

    /* check if the words substring from start to end - 1 is in trie */
    private boolean isSubStringAWord(Trie root, String word, int start, int end) { //start to end - 1
        Trie current = root;
        for (int i = start; i < end; i++) {
            current = current.next.get(word.charAt(i));
            if (current == null) {
                return false;
            }
        }
        return current.complete;
    }
}
