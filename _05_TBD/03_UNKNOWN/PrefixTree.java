class Trie {

    class TrieNode {
        boolean complete = false;
        HashMap<Character, TrieNode> next = new HashMap<Character, TrieNode>();
    }

    TrieNode root;
    public Trie() {
        root = new TrieNode();
    }

    /** Inserts a word into the trie. */
    public void insert(String word) {
        TrieNode current = root;
        for (int i = 0; i < word.length(); i++){
            current = current.next.computeIfAbsent(word.charAt(i), v -> new TrieNode());
        }
        current.complete = true;
    }

    /** Returns if the word is in the trie. */
    public boolean search(String word) {
        TrieNode current = root;
        for (int i = 0; i < word.length(); i++) {
            current = current.next.get(word.charAt(i));
            if (current == null) {
                return false;
            }
        }
        return current.complete;
    }

    public boolean startsWith(String prefix) {
        TrieNode current = root;
        for(int i = 0; i < prefix.length(); i++) {
            current = current.next.get(prefix.charAt(i));
            if (current == null) {
                return false;
            }
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */

