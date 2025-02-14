package TOClean;

import java.util.HashMap;
import java.util.Map;

public class MaxOccurringSubstring {

    public static void main(String[] args) {
        String val = mostOccurring("aabbaabbeeaab", 14);
        System.out.println("Most occurred:" + val);
    }

    public static String mostOccurring(String input, int size) throws IllegalArgumentException{
        if (input == null || size == 0 || input.length() < size) {
            throw new IllegalArgumentException("");
        }
        Map<String, Integer> map = new HashMap<>();
        int mostOccurrence = 1;
        String mostOccurred = input.substring(0, size);
        for (int i = 0; i < input.length() - size + 1; i++) {
            //System.out.println("Substring:" + input.substring(i, i + size));
            String s = input.substring(i, i + size);
            map.put(s, map.getOrDefault(s, 0) + 1);
            int count = map.get(s);
            if (count > mostOccurrence) {
                mostOccurrence = count;
                mostOccurred = s;
            }
        }
        System.out.println("Most occurred:" + mostOccurred + " times:" + mostOccurrence);
        return mostOccurred;
    }
}
