package TOClean;

import java.util.Arrays;

public class MergeSortedArray {
    public static void main(String[] args) throws Exception {
        System.out.println("Merged: " + Arrays.toString(merge(new int[]{1, 3}, new int[]{ }, 2)));
        System.out.println("Merged: " + Arrays.toString(merge(new int[]{}, new int[]{ 2, 3}, 2)));
        System.out.println("Merged: " + Arrays.toString(merge(new int[]{1, 4}, new int[]{ 2, 3}, 2)));
        System.out.println("Merged: " + Arrays.toString(merge(new int[]{1, 4}, new int[]{ 2, 3}, 3)));
        System.out.println("Merged: " + Arrays.toString(merge(new int[]{1, 4}, new int[]{ 2, 3}, 4)));
        System.out.println("Merged: " + Arrays.toString(merge(new int[]{1, 4}, new int[]{ 2, 3}, 5)));
    }

    public static int[] merge(int[] sortedArray1, int[] sortedArray2, int k) throws IllegalArgumentException {
        if (sortedArray1.length + sortedArray2.length < k) {
            throw new IllegalArgumentException(String.format("Not enough elements to find to %s elements", k));
        }

        int[] sortedArray = new int[k];

        int m = 0; // index bookkeeping for array1
        int n = 0; // index bookkeeping for array2

        for (int i = 0; i < k; i++) {
            if (m >= sortedArray1.length) {
                sortedArray[i] = sortedArray2[n++];
                continue;
            }

            if (n >= sortedArray2.length) {
                sortedArray[i] = sortedArray1[m++];
                continue;
            }

            int val1 = sortedArray1[m];
            int val2 = sortedArray2[n];

            if (val1 <= val2) {
                sortedArray[i] = val1;
                m++;
            } else {
                sortedArray[i] = val2;
                n++;
            }
        }

        return sortedArray;
    }
}
