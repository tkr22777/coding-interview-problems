import java.util.*;
import java.util.stream.Collectors;

/*
  Input:
    s = "barfoothefoobarman",
    words = ["foo","bar"] //give that these words are of same length
  Output:
    [0,9]
  Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
  The output order does not matter, returning [9,0] is fine too.
*/

class SubstringWithAllWords {

    public static void main(String[] args) {
        String input = "barfoothefoobarman";
        String[] words = {"foo","bar"};
        System.out.println(new SubstringWithAllWords().findSubstring(input, words));
    }

    public List<Integer> findSubstring(String input, String[] words) {
        if (words.length == 0) {
            return new ArrayList<>();
        }

        int wordLen = words[0].length(); //all words are of same length
        int windowLen = wordLen * words.length;

        Set<String> wordsSet = Arrays.stream(words).collect(Collectors.toSet());
        Map<Character,Integer> charsMap = getCharFreqMap(words);
        Map<Character,Integer> windowMap = new HashMap<>();

        int charCompleteCount = 0; //the count of unique complete characters
        List<Integer> solution = new ArrayList<>();
        for (int i = 0; i < input.length(); i++) {
            if (i >= windowLen) {
                char toRemove = input.charAt(i - windowLen);
                charCompleteCount = remove(windowMap, charsMap, toRemove, charCompleteCount);
            }

            char toAdd = input.charAt(i);
            if (!charsMap.containsKey(toAdd)) {
                continue;
            }

            charCompleteCount = add(windowMap, charsMap, toAdd, charCompleteCount);
            if (charCompleteCount == charsMap.size()) { //char complete does not mean they are composed of the words set
                Set<String> windowWords = getWindowWordSet(input, i, wordLen, windowLen);
                if (windowWords.equals(wordsSet)) {
                    solution.add(i - windowLen + 1);
                }
            }
        }
        return solution;
    }

    public Set<String> getWindowWordSet(String input, int currentIndex, int wordLen, int windowLen) {
        Set<String> windowWords = new HashSet<>();
        int start = currentIndex - windowLen + 1;
        while (start <= currentIndex) {
            String key = input.substring(start, start + wordLen);
            windowWords.add(key);
            start += wordLen;
        }
        return windowWords;
    }

    public int add(Map<Character,Integer> wCharsMap,
                      Map<Character,Integer> charsMap,
                      char toAdd,
                      int charCompleteCount) {

        wCharsMap.put(toAdd, wCharsMap.getOrDefault(toAdd, 0) + 1);
        if (wCharsMap.get(toAdd).intValue() == charsMap.get(toAdd).intValue()) {
            charCompleteCount++;
        }
        return charCompleteCount;
    }

    public int remove(Map<Character,Integer> wCharsMap,
                      Map<Character,Integer> charsMap,
                      char toRemove,
                      int charCompleteCount) {

        if (charsMap.containsKey(toRemove) && wCharsMap.containsKey(toRemove)) {
            wCharsMap.put(toRemove, wCharsMap.get(toRemove) - 1);
            if (wCharsMap.get(toRemove) == charsMap.get(toRemove) - 1) {
                charCompleteCount--;
            }
        }
        return charCompleteCount;
    }

    public Map<Character, Integer> getCharFreqMap(String[] words) {
        Map<Character,Integer> charsMap = new HashMap<>();
        for(int i = 0; i < words.length; i++) {
            for(int j=0; j < words[i].length(); j++) {
                Character charAtJ = words[i].charAt(j);
                charsMap.computeIfAbsent(charAtJ, v -> 0);
                charsMap.put(charAtJ, charsMap.get(charAtJ) + 1);
            }
        }
        return charsMap;
    }
}


