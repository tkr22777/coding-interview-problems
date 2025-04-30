import java.io.*;
import java.util.*;
import java.util.stream.*;

class Solution {

  public static void main(String[] args) {

    System.out.println(new Solution().wordPatternMatch("ab", "aa"));
  }

  public boolean wordPatternMatch(String pattern, String str) {

    return this.wordPatternMatch(pattern, 0, new HashMap<Character, String>(), str, 0);
  }

  public boolean wordPatternMatch(String pattern,
                                  int patIndex,
                                  Map<Character,String> charToStr,
                                  String str, int strIndex) {

    if (patIndex == pattern.length() && strIndex == str.length()) {
      return true;
    }

    if (patIndex == pattern.length() || strIndex >= str.length()) {
      return false;
    }

    Character patChar = Character.valueOf(pattern.charAt(patIndex));

    if (charToStr.containsKey(patChar)) {

      String toMatch = charToStr.get(patChar);
      if(!str.startsWith(toMatch, strIndex)) {
        return false;
      }

      return wordPatternMatch(pattern, patIndex + 1, charToStr, str, strIndex + toMatch.length());
    }

    for (int end = strIndex + 1; end <= str.length(); end++) {
      String subString = str.substring(strIndex, end);
      charToStr.put(patChar, subString);
      if (wordPatternMatch(pattern, patIndex + 1, charToStr, str, end)) {
        return true;
      }
      charToStr.remove(patChar);
    }

    return false;
  }
}



