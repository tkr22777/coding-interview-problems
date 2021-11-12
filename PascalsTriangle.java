/*
https://leetcode.com/problems/pascals-triangle/
            [1]
          [1, 1]
         [1, 2, 1]
        [1, 3, 3, 1]
      [1, 4, 6, 4, 1]
    [1, 5, 10, 10, 5, 1]
 */
import java.util.*;

class PascalsTriangle {
    public static void main(String[] args) {
        List<List<Integer>> rows = PascalsTriangle.generate(6);
        rows.forEach(row -> System.out.println(row.toString()));
    }

    public static List<List<Integer>> generate(int numRows) {
        Map<Integer, List<Integer>> cache = new HashMap<>();
        List<List<Integer>> toRet = new ArrayList<>();
        for (int i = 0; i < numRows; i++ ) {
            toRet.add(getRowCached(cache, i));
        }
        return toRet;
    }

    /* generating ith row */
    private static List<Integer> getRowCached(Map<Integer, List<Integer>> cache, int rowIndex) {
        if (cache.containsKey(rowIndex)) {
            return cache.get(rowIndex);
        }
        return getRow(rowIndex);
    }

    private static List<Integer> getRow(int rowIndex) {
        int totalColumn = rowIndex + 1;
        int array[][] = new int[2][totalColumn];

        /* build the row bottom up? */
        for (int row = 0; row < totalColumn; row++) { //each row grows by one
            for (int col = 0; col < row + 1; col++) { //
                if (col == 0 || col == row) {
                    //first and last col is 1
                    array[row % 2][col] = 1;
                } else {
                    //the current row's col is the sum of previous row's col and col - 1
                    array[row % 2][col] = array[(row - 1) % 2][col - 1] +  array[(row - 1) % 2][col];
                }
            }
        }

        List<Integer> values = new ArrayList<>();
        for (int i = 0; i < array[rowIndex % 2].length; i++) {
            values.add(i,array[rowIndex % 2][i]);
        }

        return values;
    }
}
