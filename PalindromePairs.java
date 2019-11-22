import java.util.*;

public class PalindromePairs {

    public static void main(String[] args) {
        String[] input = {"abcd", "s", "sssll", "bat", "dcba", "lls", "tab", "cat", "a", "abc", "aba", ""};
        System.out.println(Arrays.toString(input));
        List<List<Integer>> pairs = new PalindromePairs().palindromePairs(input);
        for(List<Integer> pair: pairs) {
            System.out.println(pair.toString());
        }
    }

    class TrieNode {
        Character c;
        HashMap<Character, TrieNode> next = new HashMap<>();
        Set<Integer> completeIndices = new HashSet<>();
        Set<Integer> partialIndices = new HashSet<>();
        TrieNode(Character c) { this.c = c; };
    }

    public List<List<Integer>> palindromePairs(String[] words) {

        TrieNode root = new TrieNode(null);
        for (int i = 0; i < words.length; i++) {
            addWord(root, i, words[i], 0);
        }

        //printTrie(root);

        List<List<Integer>> result = new LinkedList<>();
        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            Set<Integer> palindromeSet = getPalindromes(root, new StringBuilder(word).reverse().toString(), 0);
            for(Integer pIndex: palindromeSet) {
                if (i != pIndex) {
                    result.add(Arrays.asList(pIndex, i));
                }
            }
        }

        return result;
    }

    public void addWord(TrieNode node, int wordIndex, String word, int charIndex) {

        if (charIndex == word.length()) {
            node.completeIndices.add(wordIndex);
            return;
        }

        if (isSubstringPalindrome(word, charIndex)) {
            node.partialIndices.add(wordIndex);
        }

        Character aChar = word.charAt(charIndex);
        TrieNode charNode = node.next.computeIfAbsent(aChar, n -> new TrieNode(aChar));
        addWord(charNode, wordIndex, word, charIndex + 1);
    }

    public Set<Integer> getPalindromes(TrieNode node, String word, int charIndex) {

        if (node == null) {
            return new HashSet<>();
        }

        if (charIndex == word.length()) {
            Set<Integer> toReturn = new HashSet<>(node.completeIndices);
            toReturn.addAll(node.partialIndices);
            return toReturn;
        }

        Set<Integer> indices = new HashSet<>();
        if (isSubstringPalindrome(word, charIndex) && node.completeIndices.size() > 0) {
            indices.addAll(node.completeIndices);
        }

        TrieNode nextNode = node.next.get(word.charAt(charIndex));
        Set<Integer> nextIndices = getPalindromes(nextNode, word, charIndex + 1);

        indices.addAll(nextIndices);
        return indices;
    }

    public boolean isSubstringPalindrome(String word, int charIndex) {
        String a = word.substring(charIndex);
        return new StringBuilder(a).reverse().toString().equals(a);
    }

    class QueueNode {
        TrieNode node;
        String wordPrefix;
        public QueueNode(TrieNode node, String prefix) { this.node = node; this.wordPrefix = prefix; }
    }

    public void printTrie(TrieNode node) {

        System.out.println("Print trie:");

        Queue<QueueNode> q = new LinkedList<QueueNode>();
        q.offer(new QueueNode(node, "" + node.c));

        int level = 0;

        while(!q.isEmpty()) {

            int nodeAtLevel = q.size();

            for( int i = 0; i < nodeAtLevel; i++)  {
                QueueNode qNode = q.poll();
                System.out.println("Level: " + level);
                System.out.println("Node Char: " + qNode.wordPrefix);
                System.out.println("Complete Indices: " + qNode.node.completeIndices.toString());
                System.out.println("Partial Indices: " + qNode.node.partialIndices.toString());
                for(Character key: qNode.node.next.keySet()) {
                    TrieNode tn = qNode.node.next.get(key);
                    q.offer( new QueueNode(tn, qNode.wordPrefix + " -> " + tn.c));
                }
            }
            ++level;
        }
    }
}

