import java.util.*;

class BinarySearch {
    public static void main(String[] args) {
        int[] sortedAr = {1, 2, 5, 7, 9, 11};
        System.out.println("Given Array: " + Arrays.toString(sortedAr));
        System.out.println(String.format("Search %s Result: %s", 5, search(sortedAr, 5)));
        System.out.println(String.format("Search %s Result: %s", 9, search(sortedAr, 9)));
        System.out.println(String.format("Search %s Result: %s", 6, search(sortedAr, 6)));
    }

    public static int search(int[] nums, int target) {
        int start = 0;
        int end  = nums.length - 1;

        //Target should be in range num0 <= target <= numN
        if (target < nums[start] || nums[end] < target) {
            return -1;
        }

        while (start <= end) {
            int mid = (start + end) / 2;
            
            if (nums[mid] == target) {
                return mid;
            }

            if (target > nums[mid]) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        return -1;
    }
}
