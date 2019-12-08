import java.util.*;

//https://leetcode.com/problems/design-search-autocomplete-system/submissions/

class AutocompleteSystem {

    TrieNode root = new TrieNode();

    HashMap<String, Integer> sentenceUsage = new HashMap<String, Integer>();

    class TrieNode {
        HashMap<Character, TrieNode> nextNodes = new HashMap<Character, TrieNode>();
        HashSet<String> sentences = new HashSet<String>();
    }

    private void addSentence(TrieNode node, String sentence, int usage) {
        sentenceUsage.put(sentence, sentenceUsage.getOrDefault(sentence, 0) + usage);
        TrieNode curr = node;
        for (int i = 0; i < sentence.length(); i++) {
            curr = curr.nextNodes.computeIfAbsent(sentence.charAt(i), tn -> new TrieNode());
            curr.sentences.add(sentence);
        }
    }

    int LIMIT = 3;
    StringBuilder searchString = new StringBuilder();

    public AutocompleteSystem(String[] sentences, int[] times) {
        for (int i = 0; i < sentences.length; i++) {
            addSentence(this.root, sentences[i], times[i]);
        }
    }

    TrieNode current = root;

    public List<String> input(char c) {
        if ( ('a' <= c && c <= 'z') || ( c == ' ') ) {
            current = current.nextNodes.computeIfAbsent(c, tn -> new TrieNode());
            searchString.append(c);
            return getTopNSentences(LIMIT, current.sentences);
        }

        if (c == '#') {
            current = this.root;
            addSentence(this.root, searchString.toString(), 1);
            searchString = new StringBuilder();
        }
        return new ArrayList<>();
    }

    class SentenceUsage {
        int usage;
        String sent;
        public SentenceUsage(String sent, int usage) { this.sent = sent; this.usage = usage;};
    }

    public List<String> getTopNSentences(int N, HashSet<String> sentences) {

        List<SentenceUsage> usage = new ArrayList();

        for (String sentence: sentences) {
            int usageCount = sentenceUsage.get(sentence);
            usage.add(new SentenceUsage(sentence, usageCount));
        }

        Collections.sort(usage, (a, b) -> {
            int comp = Integer.compare(b.usage, a.usage);
            return comp != 0? comp : a.sent.compareTo(b.sent);
        });

        ArrayList<String> toReturn = new ArrayList<String>();
        for (int i = 0; i < usage.size(); i++) {
            if (i == N) {
                break;
            }
            toReturn.add(usage.get(i).sent);
        }

        return toReturn;
    }
}

