import java.util.*;

class QuickSort {

    public static void main(String[] args) {

        int[] nums = {7, -2, 1, 2, 5, 3, 7, 13, 4, 6, -3, 1};
        System.out.println("Input Array:" + Arrays.toString(nums));
        System.out.println("Sorted Array:" + Arrays.toString(new QuickSort().sortArray(nums)));
    }

    public int[] sortArray(int[] nums) {
        quickSort(nums, 0, nums.length -1);
        return nums;
    }

    public static void quickSort(int[] nums, int start, int end) {

        if (nums == null) {
            return;
        }

        if (start >= end) {
            return;
        }

        int pivot = partition(nums, start, end);
        quickSort(nums, start, pivot - 1);
        quickSort(nums, pivot + 1, end);
    }

    public static int partition(int[] nums, int start, int end) {

        int rand = Math.abs(new Random().nextInt());
        int pivot = start + (rand % (end - start + 1));
        swap(nums, end, pivot); //moving the pivot value to the end

        int left = start;
        int right = end - 1;

        while (left < right) {
            if (nums[left] > nums[end]) {
                swap(nums, left, right);
                right--;
            } else {
                left++;
            }
        }

        //left=right and we are deciding where to place the pivot
        if (nums[left] > nums[end]) {
            swap(nums, left, end);
            return left;
        } else {
            swap(nums, left + 1, end);
            return left + 1;
        }
    }

    private static void swap(int[] nums, int indexA, int indexB) {
        int c = nums[indexA];
        nums[indexA] = nums[indexB];
        nums[indexB] = c;
    }
}

