import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Map;

//https://leetcode.com/problems/merge-intervals/submissions/

class MergeIntervals {
    final int BEGIN = 0;
    final int END = 1;

    public static void main(String[] args) {
        int[][] intervals =  {{1,3},{2,6},{8,10},{15,18}};
        int[][] merged = new MergeIntervals().merge(intervals);

        Arrays.stream(merged)
            .forEach(v -> System.out.println(Arrays.toString(v)));
    }

    public int[][] merge(int[][] intervals) {
        if (intervals.length == 0) {
            return new int[0][2];
        }

        /* Sort by the begin time */
        Arrays.sort(intervals, Comparator.comparingInt(a -> a[BEGIN]));

        ArrayList<int[]> merged = new ArrayList<>();
        int begin = intervals[0][BEGIN];
        int end = intervals[0][END];
        for (int i = 1 ; i < intervals.length; i++) {
            if (begin <= intervals[i][BEGIN] && intervals[i][BEGIN] <= end) { //the beginning is inside the interval
                if (end < intervals[i][END]) {
                    end = intervals[i][END]; //extending end time to merge the previous end time
                }
                //else we don't do anything, intervals[i] is already included
            } else { //beginning is outside the current interval, add it to merged results.
                merged.add(new int[] {begin, end});  //a merged interval
                // new interval
                begin = intervals[i][BEGIN];
                end = intervals[i][END];
            }
        }

        int[] interval = new int[] {begin, end}; //the last interval
        merged.add(interval);

        int[][] mergedIntervals = new int[merged.size()][2];
        for (int i = 0; i < merged.size(); i++) {
            mergedIntervals[i] = merged.get(i);
        }
        return mergedIntervals;
    }
}

