/*
 https://leetcode.com/problems/design-search-autocomplete-system/
 
 Design a search autocomplete system for a search engine. Users may input a sentence 
 (at least one word and end with a special character '#').

 The system should provide the top 3 historical hot sentences that have the same prefix 
 as the part of sentence already typed. Here are the specific rules:

 1. The hot degree for a sentence is defined as the number of times a user typed the exactly same sentence before.
 2. The returned top 3 hot sentences should be sorted by hot degree (The first is the hottest one). 
    If several sentences have the same hot degree, use ASCII-code order (smaller one appears first).
 3. If less than 3 hot sentences exist, return all of them.
 4. When the input is a special character "#", the system should save the previous input string as a hot sentence.

 Time Complexity:
 - Constructor: O(k*l) where k is number of sentences, l is average length of sentence
 - Input: O(p + q + mlog(m)) where p is length of sentence, q is number of nodes in trie, m is matched sentences
*/

import java.util.*;
import java.util.stream.*;

/*
* Trie is basically an N-ary tree
*/
class TrieNode {
    HashMap<Character, TrieNode> nextNodes = new HashMap<Character, TrieNode>();
    HashSet<String> sentences = new HashSet<String>();
}

class SentenceUsage {
    int usage;
    String sentence;

    public SentenceUsage(String sentence, int usage) {
        this.sentence = sentence;
        this.usage = usage;
    }
}

class AutoCompleteSystem {

    TrieNode root = new TrieNode();
    TrieNode current = root;
    HashMap<String, Integer> sentenceUsage = new HashMap<String, Integer>(); ;
    StringBuilder searchString = new StringBuilder();;

    public AutoCompleteSystem(String[] sentences, int[] times) {
        for (int i = 0; i < sentences.length; i++) {
            this.addSentence(sentences[i], times[i]);
        }
    }

    private void addSentence(String sentence, int usage) {
        TrieNode curr = this.root;
        for (int i = 0; i < sentence.length(); i++) {
            char c = sentence.charAt(i);
            curr = curr.nextNodes.computeIfAbsent(c, tn -> new TrieNode());
            curr.sentences.add(sentence);
        }

        // update usage
        if (this.sentenceUsage.containsKey(sentence)) {
            int currUsage = this.sentenceUsage.get(sentence);
            this.sentenceUsage.put(sentence, currUsage + usage);
        } else {
            this.sentenceUsage.put(sentence, usage);
        }
    }

    public List<String> input(char c) {
        if (('a' <= c && c <= 'z') || (c == ' ')) {
            searchString.append(c);
            current = current.nextNodes.computeIfAbsent(c, tn -> new TrieNode());
            return getTopThreeSentences(this.sentenceUsage, current.sentences);
        } else if (c == '#') {
            addSentence(searchString.toString(), 1);
            searchString.setLength(0);
            current = this.root;
        }
        return new ArrayList<>();
    }

    private List<String> getTopThreeSentences(
        HashMap<String, Integer> sUsage,
        HashSet<String> sentences
    ) {
        List<SentenceUsage> sentenceUsages = sentences.stream()
            .map(s -> new SentenceUsage(s, sUsage.get(s)))
            .collect(Collectors.toList());

        Collections.sort(sentenceUsages, (a, b) -> {
            // descending order by usage
            int comp = Integer.compare(b.usage, a.usage); 
            // ascending lexicographical order when usage is same
            return comp != 0? comp : a.sentence.compareTo(b.sentence);
        });

        return sentenceUsages.stream()
            .map(n -> n.sentence)
            .limit(3)
            .collect(Collectors.toList());
    }
}