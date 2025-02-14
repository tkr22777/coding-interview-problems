/* https://leetcode.com/problems/reorder-data-in-log-files/ */

import java.util.*;

class ReorderLogs {

    public String[] reorderLogFiles(String[] logs) {
        ArrayList<String> digitLogs = new ArrayList<>();
        ArrayList<String[]> charLogs = new ArrayList<>();

        for (String aLog : logs) {
            String[] tokens = aLog.split(" ");
            if (Character.isDigit(tokens[1].charAt(0))) {
                digitLogs.add(aLog);
            } else {
                String rest = aLog.substring(aLog.indexOf(" ")).trim();
                String[] pair = {rest, aLog};
                charLogs.add(pair);
            }
        }

        charLogs.sort(Comparator.comparing((String[] o) -> o[0]).thenComparing(o -> o[1]));

        String[] reorderedLogs = new String[digitLogs.size() + charLogs.size()];

        for (int i = 0; i < charLogs.size(); i++) {
            reorderedLogs[i] = charLogs.get(i)[1];
        }

        for (int i = 0, j = charLogs.size(); j < reorderedLogs.length; i++, j++) {
            reorderedLogs[j] = digitLogs.get(i);
        }

        return reorderedLogs;
    }
}

