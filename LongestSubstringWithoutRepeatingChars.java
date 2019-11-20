import java.util.*;

class LongestSubstringWithoutRepeatingChars {

    public static void main(String[] args) {
        System.out.println("Longest substring: " + lengthOfLongestSubstring("a"));
        System.out.println("Longest substring: " + lengthOfLongestSubstring("bbb"));
        System.out.println("Longest substring: " + lengthOfLongestSubstring("bbbbbbbb"));
        System.out.println("Longest substring: " + lengthOfLongestSubstring("mlra"));
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

        int longest = 0;

        //move the j pointer ahead and add chars to set until duplicate found.
        //since j created duplicate, s.charAt(j) must be somewhere in between i to j
        //move i just after the last incident of s.charAt(j)
        //remove all characters from i to inew

        HashSet<Character> set = new HashSet<>();
        int i = 0, j;
        for (j = 0 ; j < s.length(); ++j) {

            if (set.contains(s.charAt(j))) {

                longest = Math.max(j-i, longest);

                int inew = i;
                for (int k = i; k < j; ++k) {
                    if (s.charAt(k) == s.charAt(j)) {
                        inew = k;
                    }
                }

                for (int k = i; k <= inew; ++k) {
                    set.remove(s.charAt(k)); //removing unique chars before iNew
                }

                set.add(s.charAt(j));

                i = inew + 1;

            } else {
                set.add(s.charAt(j));
            }
        }
        return Math.max(j - i, longest);
    }
}

