/*
 * given a string with alphabets, crush more than 2 contiguous (3 chars or more)
 * chars and merge the strings from the sides, return the final string when it
 * cannot be crushed anymore
 */
public class StringCrush {
    public static void main(String[] args) {
        assert nextContiguousIndex("ABBCCCCBD", 0) == -1;
        assert nextContiguousIndex("ABBCCCCBD", 1) == -1;
        assert nextContiguousIndex("ABBCCCCBD", 3) == 6;
        assert nextContiguousIndex("ABBBB", 1) == 4;

        assert "AD".equals(crush("ABBBCCCCD"));
        assert "ABBD".equals(crush("ABBCCCCD"));
    }

    public static int nextContiguousIndex(String input, int index) {
        if (index < 0 || index >= input.length()) {
            return -1;
        }
        char theChar = input.charAt(index);
        int i = index + 1;
        while (i < input.length() && input.charAt(i) == theChar) {
            i++;
        }
        if (i - index >= 3) {
            return i - 1;
        } else {
            return -1;
        }
    }

    public static String crush(String input) {
        boolean changed = true;
        while (changed) {
            changed = false;
            String nextInput = input;
            int scanIndex = 0;
            while(scanIndex < nextInput.length()) {
                int endIndex = nextContiguousIndex(nextInput, scanIndex);
                if (endIndex != -1) {
                    nextInput = nextInput.substring(0, scanIndex) + nextInput.substring(endIndex + 1);
                    changed = true;
                    scanIndex = 0;
                } else {
                    scanIndex++;
                }
            }
            input = nextInput;
        }
        return input;
    }
}
