import java.util.*;

class LongestPalindromicSubstring {

    public static void main(String[] args) {
        String lps = new LongestPalindromicSubstring().longestPalindrome("ababaaaba");
        System.out.println("Longest Palindromic Substring:" + lps);
    }

    public String longestPalindrome(String s) {

        if (s.length() < 2) {
            return s;
        }

        char[] chars = s.toCharArray();

        String highest = "";
        for (int i = 0; i < chars.length; i++) {
            highest = returnCurrentHighestOdd(highest, chars, i);
        }

        for (int i = 0; i < chars.length - 1; i++) {
            if (chars[i] == chars[i+1] ) {
                highest = returnCurrentHighestEven(highest, chars, i);
            }
        }
        return highest;
    }

    private String returnCurrentHighestOdd(String currentHighest, char[] chars, int index) {

        int left = index - 1;
        int right = index + 1;
        while (left >= 0 && right < chars.length) {
            if (chars[left] != chars[right]) {
                break;
            }
            left--;
            right++;
        }

        if (currentHighest.length() > right - left + 1) {
            return currentHighest;
        }

        return new String(chars, left, right + 1);
    }

    private String returnCurrentHighestEven(String currentHighest, char[] chars, int index) {

        int left = index - 1;
        int right = index + 2;

        while( left >= 0 && right < chars.length) {
            if (chars[left] != chars[right]) {
                break;
            }
            left--;
            right++;
        }

        if (currentHighest.length() > right - left + 1) {
            return currentHighest;
        }

        return new String(chars, left, right + 1);
    }
}
