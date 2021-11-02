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
        Arrays.stream(words)
            .forEach(word -> addWord(root, word));

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
            curr = curr.next.computeIfAbsent(word.charAt(i), t -> new Trie());
        }
        curr.complete = true;
    }

    private int concatenationCount(Trie root, String word, int start) { // start is inclusive
        for (int i = start + 1; i <= word.length(); ++i) { //beginning from start + 1 to discard empty string
            if (isSubStringAWord(root, word, start, i)) { //since substring(start, i) is a word, we check the next portion
                if (i == word.length()) { //at the end so (start, i) has count 1
                    return 1;
                }

                int count = this.concatenationCount(root, word, i);
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
        for(int i = start; i < end; i++) {
            current = current.next.get(word.charAt(i));
            if (current == null) {
                return false;
            }
        }
        return current.complete;
    }
}
