import java.util.*;
import java.util.stream.Collectors;

/*
Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
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

        int wordLen = words[0].length();
        int windowLen = wordLen * words.length;

        Set<String> wordsSet = Arrays.stream(words).collect(Collectors.toSet());
        Map<Character,Integer> charsMap = getCharFreqMap(words);
        Map<Character,Integer> windowMap = new HashMap<>();

        int charCompleteCount = 0;
        List<Integer> solution = new ArrayList<>();

        for(int i = 0; i < input.length(); i++) {

            if (i >= windowLen) {
                char toRemove = input.charAt(i - windowLen);
                charCompleteCount = remove(windowMap, charsMap, toRemove, charCompleteCount);
            }

            char charAtI = input.charAt(i);
            if (!charsMap.containsKey(charAtI)) {
                continue;
            }

            windowMap.computeIfAbsent(charAtI, v -> 0);
            windowMap.put(charAtI, windowMap.get(charAtI) + 1);
            if (windowMap.get(charAtI).intValue() == charsMap.get(charAtI).intValue()) {
                charCompleteCount++;
            }

            if (charCompleteCount == charsMap.size()) {
                Set<String> windowWords = new HashSet<>();
                int wordCounter = 0;
                int start = i - windowLen + 1;
                while (start <= i) {
                    String key = input.substring(start, start + wordLen);
                    if (!wordsSet.contains(key)) {
                        break;
                    }
                    windowWords.add(key);
                    start += wordLen;
                }

                if (windowWords.equals(wordsSet)) {
                    solution.add(i - windowLen + 1);
                }
            }
        }

        return solution;
    }

    public int remove(Map<Character,Integer> wCharsMap,
                      Map<Character,Integer> charsMap,
                      char toRemove,
                      int charCompleteCount) {

        if (charsMap.containsKey(toRemove)) {
            wCharsMap.put(toRemove, wCharsMap.get(toRemove) - 1);
            if (wCharsMap.get(toRemove).intValue() == charsMap.get(toRemove).intValue() - 1) {
                return charCompleteCount - 1;
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


