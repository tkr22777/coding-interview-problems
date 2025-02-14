/*
 https://leetcode.com/problems/design-search-autocomplete-system/
*/

import java.util.*;
import java.util.stream.*;

class TrieNode {
    HashMap<Character, TrieNode> nextNodes = new HashMap<Character, TrieNode>();
    HashSet<String> sentences = new HashSet<String>();
}

class SentenceUsage {
    int usage;
    String sentence;
    public SentenceUsage(String sentence, int usage) { this.sentence = sentence; this.usage = usage;};
}

class AutoCompleteSystem {
    TrieNode root = new TrieNode();
    TrieNode current = root;
    HashMap<String, Integer> sentenceUsage = new HashMap<String, Integer>(); ;
    StringBuilder searchString = new StringBuilder();;

    public AutoCompleteSystem(String[] sentences, int[] times) {
        IntStream.range(0, sentences.length)
            .forEach(i -> addSentence(sentences[i], times[i]));
    }

    public List<String> input(char c) {
        if (('a' <= c && c <= 'z') || (c == ' ')) {
            searchString.append(c);
            current = current.nextNodes.computeIfAbsent(c, tn -> new TrieNode());
            return getTopThreeSentences(sentenceUsage, current.sentences);
        } else if (c == '#') {
            searchString = new StringBuilder();
            current = this.root;
            addSentence(searchString.toString(), 1);
        }
        return new ArrayList<>();
    }

    private void addSentence(String sentence, int usage) {
        /* Update TrieNode */
        TrieNode curr = this.root;
        for (int i = 0; i < sentence.length(); i++) {
            curr = curr.nextNodes.computeIfAbsent(sentence.charAt(i), tn -> new TrieNode());
            curr.sentences.add(sentence);
        }

        /* Update usage */
        sentenceUsage.put(sentence, sentenceUsage.getOrDefault(sentence, 0) + usage);
    }

    private List<String> getTopThreeSentences(HashMap<String, Integer> sUsage, HashSet<String> sentences) {
        List<SentenceUsage> sentenceUsages = sentences.stream()
            .map(s -> new SentenceUsage(s, sUsage.get(s)))
            .collect(Collectors.toList());

        Collections.sort(sentenceUsages, (a, b) -> {
            int comp = Integer.compare(b.usage, a.usage);
            return comp != 0? comp : a.sentence.compareTo(b.sentence);
        });

        return sentenceUsages.stream()
            .map(n -> n.sentence)
            .limit(3)
            .collect(Collectors.toList());
    }
}
