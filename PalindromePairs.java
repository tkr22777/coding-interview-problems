import java.util.*;

public class PalindromePairs {

    public static void main(String[] args) {
        String[] input = {"abcd", "s", "sssll", "bat", "dcba", "lls", "tab", "cat", "a", "abc", "aba", ""};
        System.out.println(Arrays.toString(input));
        List<List<Integer>> pairs = new PalindromePairs().palindromePairs(input);
        pairs.forEach(pair -> System.out.println(pair.toString()));
    }

    class TrieNode {
        HashMap<Character, TrieNode> next = new HashMap<>();
        Set<Integer> completeIndices = new HashSet<>();
        Set<Integer> partialIndices = new HashSet<>();
    }

    public List<List<Integer>> palindromePairs(String[] words) {

        TrieNode root = new TrieNode();
        for (int i = 0; i < words.length; i++) {
            addWord(root, i, words[i], 0);
        }

        List<List<Integer>> result = new LinkedList<>();
        for (int i = 0; i < words.length; i++) {
            String wordReversed = new StringBuilder(words[i]).reverse().toString();
            Set<Integer> palindromeSet = getPalindromes(root, wordReversed, 0);
            for(Integer pIndex: palindromeSet) {
                if (i != pIndex) {
                    result.add(Arrays.asList(pIndex, i));
                }
            }
        }
        return result;
    }

    private boolean isSubstringPalindrome(String word, int charIndex) {
        String a = word.substring(charIndex);
        return new StringBuilder(a).reverse().toString().equals(a);
    }

    private void addWord(TrieNode root, int wordIndex, String word, int charIndex) {

        TrieNode current = root;
        for (int i = 0; i < word.length(); i++) {
            char charAtI = word.charAt(i);
            if (isSubstringPalindrome(word, i)) {
                current.partialIndices.add(wordIndex);
            }
            current = current.next.computeIfAbsent(charAtI, n -> new TrieNode());
        }
        current.completeIndices.add(wordIndex);
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
}

