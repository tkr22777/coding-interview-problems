import java.util.*;

//https://leetcode.com/problems/reorder-data-in-log-files/

class ReorderLogs {

    public String[] reorderLogFiles(String[] logs) {

        ArrayList<String> digitLogs = new ArrayList<>();
        ArrayList<String[]> charLogs = new ArrayList<>();

        for (int i = 0; i < logs.length; i++) {
            String aLog = logs[i];
            String[] tokens = aLog.split(" ");
            if (Character.isDigit(tokens[1].charAt(0))) {
                digitLogs.add(aLog);
            } else {
                String rest = aLog.substring(aLog.indexOf(" ")).trim();
                String[] pair = {rest, aLog};
                charLogs.add(pair);
            }
        }

        Collections.sort(charLogs, new Comparator<String[]>() {
            @Override
            public int compare(String[] o1, String[] o2) {
                int comp = o1[0].compareTo(o2[0]);
                return comp != 0 ? comp : o1[1].compareTo(o2[1]);
            }
        });

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

