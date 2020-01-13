import java.util.*;
import java.util.stream.*;

//https://leetcode.com/problems/design-search-autocomplete-system/submissions/

class AutoCompleteSystem {

    class TrieNode {
        HashMap<Character, TrieNode> nextNodes = new HashMap<Character, TrieNode>();
        HashSet<String> sentences = new HashSet<String>();
    }

    HashMap<String, Integer> sentenceUsage = new HashMap<String, Integer>(); ;

    TrieNode root = new TrieNode();
    TrieNode current = root;

    StringBuilder searchString = new StringBuilder();;

    public List<String> input(char c) {
        if (('a' <= c && c <= 'z') || (c == ' ')) {
            searchString.append(c);
            current = current.nextNodes.computeIfAbsent(c, tn -> new TrieNode());
            return getTopThreeSentences(sentenceUsage, current.sentences);
        } else if (c == '#') {
            searchString = new StringBuilder();
            current = this.root;
            addSentence(this.root, searchString.toString(), 1);
        }
        return new ArrayList<>();
    }

    private void addSentence(TrieNode node, String sentence, int usage) {

        /* Updating the TrieNode */
        TrieNode curr = node;
        for (int i = 0; i < sentence.length(); i++) {
            curr = curr.nextNodes.computeIfAbsent(sentence.charAt(i), tn -> new TrieNode());
            curr.sentences.add(sentence);
        }

        /* Updating usage */
        sentenceUsage.put(sentence, sentenceUsage.getOrDefault(sentence, 0) + usage);
    }

    public AutoCompleteSystem(String[] sentences, int[] times) {
        IntStream.range(0, sentences.length)
            .forEach( i -> addSentence(this.root, sentences[i], times[i]));
    }

    class SentenceUsage {
        int usage;
        String sentence;
        public SentenceUsage(String sentence, int usage) { this.sentence = sentence; this.usage = usage;};
    }

    private List<String> getTopThreeSentences(HashMap<String, Integer> sUsage, HashSet<String> sentences) {

        List<SentenceUsage> usage = sentences.stream()
            .map(s -> new SentenceUsage(s, sUsage.get(s)))
            .collect(Collectors.toList());

        Collections.sort(usage, (a, b) -> {
            int comp = Integer.compare(b.usage, a.usage);
            return comp != 0? comp : a.sentence.compareTo(b.sentence);
        });

        return usage.stream()
            .map(n -> n.sentence)
            .limit(3)
            .collect(Collectors.toList());
    }
}

