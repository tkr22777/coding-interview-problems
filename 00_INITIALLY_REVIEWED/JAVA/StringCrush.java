/* given a string with alphabets, crush more than 2 contiguous chars
and merge the strings from the sides, return the final string when it
cannot be crushed anymore */
public class StringCrush {
    public static void main(String[] args) {
        assert nextContiguousIndex("ABBCCCCBD", 0) == -1;
        assert nextContiguousIndex("ABBCCCCBD", 1) == -1;
        assert nextContiguousIndex("ABBCCCCBD", 3) == 7;
        assert nextContiguousIndex("ABBBB", 1) == 5;

        assert "AD".equals(crush("ABBBCCCCD"));
        assert "ABBD".equals(crush("ABBCCCCD"));
        assert "AD".equals(crush("ABBCCCCBD"));
    }

    public static String crush(String input) {
        boolean crushMore = true;
        int index = 0;
        while (crushMore) {
            int nextIndex = nextContiguousIndex(input, index);
            if (nextIndex > 0) {
                input = crush(input, index, nextIndex + 1);
                index = 0;
            } else {
                index++;
                if (index >= input.length()) {
                    crushMore = false;
                }
            }
        }
        return input;
    }

    public static String crush(String input, int startIndex, int endIndex) {
        for (int i = startIndex; i < endIndex; i++) {
            input = input.substring(0, i) + "_" + input.substring(i+1);
        }
        input = input.replaceAll("_", "");
        return input;
    }

    public static int nextContiguousIndex(String input, int index) {
        Character theChar = input.charAt(index);
        int i = index + 1;
        for (; i < input.length(); i++) {
            if (!theChar.equals(input.charAt(i)) ) {
                if (i - index > 2) {
                    return i - 1;
                } else {
                    return -1;
                }
            }
        }

        if (i - index > 2) {
            return i - 1;
        } else {
            return -1;
        }
    }
}
