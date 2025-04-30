import java.io.*;
import java.util.*;
import java.util.stream.*;

class GroupAnagram {

  public static void main(String[] args) {
    String[] words = {"eat", "tea", "tan", "ate", "nat", "bat"};
    System.out.println(new GroupAnagram().groupAnagram(words));
  }

  public List<List<String>> groupAnagram(String[] words) {

    HashMap<String, ArrayList<String>> charMapToString = new HashMap<String, ArrayList<String>>();

    for(String word: words) {

      short[] charFreq = new short[26];

      for(int i = 0; i < word.length(); i++) {
        charFreq[word.charAt(i) - 'a']++;
      }

      String key = Arrays.toString(charFreq);
      charMapToString.computeIfAbsent(key, v -> new ArrayList<>()).add(word);
    }

    return new ArrayList<List<String>>(charMapToString.values());
  }
}

