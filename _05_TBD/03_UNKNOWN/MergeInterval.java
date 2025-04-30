package com.company;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Map;

class Solution {

    public int[][] merge(int[][] intervals) {

        if (intervals.length == 0) {
            return new int[0][2];
        }

        Arrays.sort(intervals, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return Integer.compare(o1[0], o2[0]);
            }
        });

        ArrayList<int[]> merged = new ArrayList<>();

        int start = intervals[0][0];
        int end = intervals[0][1];

        for (int i = 1 ; i < intervals.length; i++) {
            if (start <= intervals[i][0]  && intervals[i][0] <= end) { //the beginning is inside the interval
                if (end < intervals[i][1]) {
                    end = intervals[i][1];
                }
            } else {
                int[] interval = new int[2];
                interval[0] = start;
                interval[1] = end;
                merged.add(interval);
                start = intervals[i][0];
                end = intervals[i][1];
            }
        }

        int[] interval = new int[2];
        interval[0] = start;
        interval[1] = end;
        merged.add(interval);

        int[][] mergedIntervals = new int[merged.size()][2];
        for (int i = 0; i < merged.size(); i++) {
            mergedIntervals[i] = merged.get(i);
        }
        return mergedIntervals;
    }

    private void print(Object x) {
        System.out.println(x.toString());
    }

    private void print(Object[] array) {
        System.out.println(Arrays.toString(array));
    }

    private void print(int[][] array2d) {

        if (array2d == null) {
            return;
        }

        for (int i = 0 ; i < array2d.length; i++) {
            print(Arrays.toString(array2d[i]));
        }
        System.out.println();
    }

    private void print2d(Object[][] array2d) {

        if (array2d == null) {
            return;
        }

        for (int i = 0 ; i < array2d.length; i++) {

            if (array2d[i] == null) {
                continue;
            }

            print(array2d[i]);
        }
        System.out.println();
    }

    private void print(Map map) {

        for (Object key: map.keySet()) {
            Object val = map.get(key);
            if (val instanceof int[]) {
                int[] array = (int[]) val;
                print("Key: " + key + " Value: " + Arrays.toString(array));
            } else {
                print("Key: " + key + " Value: " + val);
            }
        }
    }

    public static void main(String[] args) {
        int[][] array = {
                { 1 , 4},
                { 6 , 9},
                { 3 , 5},
                { 9 , 11}
        };
        Solution solution = new Solution();
        int[][] result = solution.merge(array);
        solution.print(result);
    }
}
