import java.util.HashMap;
import java.util.List;
import java.util.Map;

/*
    Given a list of words in a dictionary, implement a check spelling
    function that returns 1. the same word if the word spelling is correct
    2. any word from the dictionary that is off by a single character 3. null
    if no word in the word dictionary matches the word or off by a single
    character.
 */
class TrieNodeS {
    Map<Character, TrieNodeS> next = new HashMap<>();
    boolean complete;
}
public class SpellingSuggestion {

    TrieNodeS root;

    public static void main(String[] args) {
        if (!"amend".equals(new SpellingSuggestion(List.of("amend", "abacus", "bottle", "bentley")).checkSpelling("amand"))){
            throw new RuntimeException("");
        }
        if (!"bottle".equals(new SpellingSuggestion(List.of("amend", "abacus", "bottle", "bentley")).checkSpelling("battle"))){
            throw new RuntimeException("");
        }
        if (!"bottle".equals(new SpellingSuggestion(List.of("amend", "abacus", "bottle", "bentley")).checkSpelling("bittle"))){
            throw new RuntimeException("");
        }
        if (!( null == new SpellingSuggestion(List.of("amend", "abacus", "bottle", "bentley")).checkSpelling("bitlle"))){
            throw new RuntimeException("");
        }
    }

    public SpellingSuggestion(List<String> words) {
        root = new TrieNodeS();
        for (String word: words) {
            addWord(word);
        }
    }

    private void addWord(String word) {
        TrieNodeS node = root;
        for (int i = 0; i < word.length(); i++) {
            node = node.next.computeIfAbsent(word.charAt(i), v -> new TrieNodeS());
        }
        node.complete = true;
    }

    public String checkSpelling(String word) {
        return checkSpelling(root, word, 0, false);
    }

    private String checkSpelling(TrieNodeS node, String word, int index, boolean missMatched) {
        if (index == word.length()) {
            return "";
        }

        Character character = word.charAt(index);
        TrieNodeS next = node.next.get(character);

        if (next == null) {
            if (missMatched) {
                return null;
            } else {
                for (Map.Entry<Character, TrieNodeS> entry: node.next.entrySet()) {
                    String value = checkSpelling(entry.getValue(), word, index + 1, true);
                    if (value != null) {
                        return entry.getKey() + value;
                    }
                }
                return null;
            }
        } else {
            if (index == word.length() - 1) {
                if (next.complete) {
                    return character + "";
                } else {
                    return null;
                }
            } else {
                String value = checkSpelling(next, word, index + 1, missMatched);
                if (value == null) {
                    return null;
                } else {
                    return character + value;
                }
            }
        }
    }
}
