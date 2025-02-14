/*
  https://leetcode.com/problems/group-anagrams/
 */
import java.util.*;

class GroupAnagram {
  public static void main(String[] args) {
    String[] words = {"eat", "tea", "tan", "ate", "nat", "bat"};
    System.out.println(new GroupAnagram().groupAnagram(words));
  }

  public List<List<String>> groupAnagram(String[] words) {
    HashMap<String, ArrayList<String>> charMapToWord = new HashMap<String, ArrayList<String>>();

    for (String word: words) {
      short[] charFreq = new short[26];
      for(int i = 0; i < word.length(); i++) {
          charFreq[word.charAt(i) - 'a']++;
      }

      charMapToWord.computeIfAbsent(Arrays.toString(charFreq), v -> new ArrayList<>())
          .add(word);
    }

    return new ArrayList<List<String>>(charMapToWord.values());
  }
}
