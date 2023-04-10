import java.util.*;

class LongestSubstringWithoutRepeatingChars {

    public static void main(String[] args) {
        System.out.println("Longest substring: " + lengthOfLongestSubstring("a"));
        System.out.println("Longest substring: " + lengthOfLongestSubstring("bbb"));
        System.out.println("Longest substring: " + lengthOfLongestSubstring("bbbbbbbb"));
        System.out.println("Longest substring: " + lengthOfLongestSubstring("mlra"));
        System.out.println("Longest substring: " + lengthOfLongestSubstring("mlraa"));
        System.out.println("Longest substring: " + lengthOfLongestSubstring("mmlraa"));
        System.out.println("Longest substring: " + lengthOfLongestSubstring("aba"));
        System.out.println("Longest substring: " + lengthOfLongestSubstring("bbbsbnsl"));
    }

    public static int lengthOfLongestSubstring(String s) {
        if (s == null) {
            return 0;
        }

        if (s.length() < 2) {
            return s.length();
        }

        int longest = 1;

        /*
        Add chars to set until duplicate found. Since char at j created duplicate,
        that char must be somewhere in between i to j - 1. Move i to right until you
        confront the char again. after the last incident of s.charAt(j)
        remove all characters from i to inew.
        How does that make the solution correct?
        */

        HashSet<Character> set = new HashSet<>();
        int i = 0, j = 0;
        while (j < s.length()) {
            if (set.contains(s.charAt(j))) {
                longest = Math.max(j - i, longest);
                while (i < j) {
                    set.remove(s.charAt(i));
                    if (s.charAt(i) == s.charAt(j)) {
                        break;
                    }
                    i++;
                }
                i++;
            } 
            set.add(s.charAt(j));
            j++;
        }
        return Math.max(j - i, longest);
    }
}

