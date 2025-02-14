class Solution {

    public String longestPalindrome(String s) {

        if (s.length() < 2) {
            return s;
        }

        char[] chars = s.toCharArray();
        String highest = "";

        for (int i = 0; i < chars.length; i++) {

            if (highest.length() > 2 * (chars.length - i)) {
                break;
            }

            highest = returnCurrentHighestOdd(highest, chars, i);
        }

        for (int i = 0; i < chars.length - 1; i++) {
            if (chars[i] == chars[i+1] ) {
                String evenPanindrom = returnCurrentHighestEven(highest, chars, i);
                if (evenPanindrom.length() > highest.length()) {
                    highest = evenPanindrom;
                }
            }
        }
        return highest;
    }

    private String returnCurrentHighestOdd(String currentHighest, char[] chars, int index) {

        int pStretch = 0;

        for(int i = index - 1, j = index + 1; i >= 0 && j < chars.length ; i--, j++) {
            //System.out.println("[i:" + i + "][j:" + j + "]");
            if (chars[i] != chars[j]) {
                break;
            }
            pStretch = index - i;
        }

        if (currentHighest.length() > pStretch * 2 + 1) {
            return currentHighest;
        }

        return new String(chars, index - pStretch, pStretch * 2 + 1);
    }

    private String returnCurrentHighestEven(String currentHighest, char[] chars, int index) {
        int pStretch = 0;

        for(int i = index - 1, j = index + 2; i >= 0 && j < chars.length ; i--, j++) {
            //System.out.println("[i:" + i + "][j:" + j + "]");
            if (chars[i] != chars[j]) {
                break;
            }
            pStretch = index - i;
        }

        if (currentHighest.length() > pStretch * 2 + 2) {
            return currentHighest;
        }

        return new String(chars, index - pStretch, pStretch * 2 + 2);
    }
}



