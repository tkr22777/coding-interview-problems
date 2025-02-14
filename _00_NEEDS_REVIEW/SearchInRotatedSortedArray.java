import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Map;

class Solution {

    public static void main(String[] args) {

        int[] array = { 3, 5, 1};
        print(search(array,3));

        int[] array2 = {5, 1, 3};
        print(search(array,5));
    }

    public static int search(int[] nums, int target) {

        int start = 0;
        int end = nums.length - 1;

        while (start <= end) {

            int mid = (start + end) / 2;
            if (target == nums[mid]){
               return mid;
            }

            if (nums[start] <= nums[end]) { // from start to end the array is properly sorted

               if (target > nums[mid]) {
                   start = mid + 1;
               } else {
                   end = mid - 1;
               }

            } else {

                if (nums[start] > nums[mid]) {

                    if ( nums[mid] < target && target <= nums[end]) {
                        start = mid + 1;
                    } else {
                        end = mid - 1;
                    }
                } else {
                    if (nums[start] <= target && target < nums[mid]) {
                        end = mid - 1;
                    } else {
                        start = mid + 1;
                    }
                }
            }
        }
        return -1;
    }

    private static void print(Object x) {
        System.out.println(x.toString());
    }

    private static void print(Object[] array) {
        System.out.println(Arrays.toString(array));
    }

    private static void print(int[][] array2d) {

        if (array2d == null) {
            return;
        }

        for (int i = 0 ; i < array2d.length; i++) {
            print(Arrays.toString(array2d[i]));
        }
        System.out.println();
    }

    private static void print2d(Object[][] array2d) {

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

    private static void print(Map map) {

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
}

