import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Map;

//https://leetcode.com/problems/merge-intervals/submissions/

class Solution {

    public int[][] merge(int[][] intervals) {

        if (intervals.length == 0) {
            return new int[0][2];
        }

        Arrays.sort(intervals, (a,b) -> { return Integer.compare(a[0], b[0]); });

        ArrayList<int[]> merged = new ArrayList<>();

        int start = intervals[0][0];
        int end = intervals[0][1];

        for (int i = 1 ; i < intervals.length; i++) {
            if (start <= intervals[i][0]  && intervals[i][0] <= end) { //the beginning is inside the interval
                if (end < intervals[i][1]) {
                    end = intervals[i][1]; //extending endtime to merge the previous end time
                }
            } else {
                int[] interval = new int[] {start, end}; //a merged interval
                merged.add(interval);
                start = intervals[i][0];
                end = intervals[i][1];
            }
        }

        int[] interval = new int[] {start, end}; //a merged interval
        merged.add(interval);

        int[][] mergedIntervals = new int[merged.size()][2];
        for (int i = 0; i < merged.size(); i++) {
            mergedIntervals[i] = merged.get(i);
        }
        return mergedIntervals;
    }
}

