package TOClean;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/*
Given a set of Tuples with each tuple containing 3 numbers:
# N1 = start timestamp,
# N2 = end timestamp and
# N3 = count of events that occurred in time interval N1 to N2
where
N1 < N2,
N1 > 0,
N2 > 0 and
N3 >= 0
 find all tuples that do not overlap with with any other tuples with respect to time interval.
For example, Input = [[1,2,10],[3,5,0],[4,8,1],[6,7,3],[8,10,11],[12,16,3]]
Output= [[1,2,10],[12,16,3]]

Sorted = [[1,2,10],[3,5,0],[4,8,1],[6,7,3],[8,10,11],[12,16,3]]
 */

class NonOverlapping {
    public static void main(String[] args) {
        int[][] touples = new int[][]{
            {1,2,10},{3,5,0},{4,8,1},{6,7,3},{8,10,11},{12,16,3}
        };
        int[][] nonoverlaps = findNonOverlaps(touples);

        for (int i = 0; i < nonoverlaps.length; i++) {
            System.out.println(Arrays.toString(nonoverlaps[i]));
        }
    }

    public static int[][] findNonOverlaps(int[][] touples) {
        if (touples.length == 0) {
            return new int[0][0];
        }
        Set<Integer> nonOverlaps = new HashSet<Integer>();
        Set<Integer> overlaps = new HashSet<Integer>();

        int endTime = touples[0][1];
        nonOverlaps.add(0);
        for (int i = 1; i < touples.length; i++) {
            //System.out.println(Arrays.toString(touples[i]));
            if (touples[i][0] > endTime) {
                nonOverlaps.add(i - 1);
                nonOverlaps.add(i);
            } else {
                overlaps.add(i - 1);
                overlaps.add(i);
            }
            endTime = Math.max(endTime, touples[i][1]);
        }

        nonOverlaps.removeAll(overlaps);
        int[][] toRet = new int[nonOverlaps.size()][3];
        int i = 0;
        for (Integer index: nonOverlaps) {
            toRet[i] = touples[index];
            i++;
        }
        return toRet;
    }
}
