import java.util.*;

class QuickSort {

    public static void main(String[] args) {
        int[] numbers = {7, -2, 1, 2, 5, 3, 7, 13, 4, 6, -3, 1};
        System.out.println("Input Array:" + Arrays.toString(numbers));
        System.out.println("Sorted Array:" + Arrays.toString(new QuickSort().sortArray(numbers)));
    }

    public int[] sortArray(int[] numbers) {
        quickSort(numbers, 0, numbers.length -1);
        return numbers;
    }

    public static void quickSort(int[] numbers, int begin, int end) {
        if (numbers == null) {
            return;
        }

        if (begin >= end) {
            return;
        }

        int pivot = partition(numbers, begin, end);

        quickSort(numbers, begin, pivot - 1);
        quickSort(numbers, pivot + 1, end);
    }

    /*
     * returns the pivot index,
     * for any i < pivot, nums[i] < nums[pivot]
     * for any j > pivot, nums[j] > nums[pivot]
     */
    public static int partition(int[] numbers, int begin, int end) {
        int rand = Math.abs(new Random().nextInt());
        int pivot = begin + (rand % (end - begin + 1));
        swap(numbers, end, pivot); //moving the pivot value to the end

        int left = begin;
        int right = end - 1;

        while (left < right) {
            if (numbers[left] <= numbers[end]) {
                left++;
            } else {
                swap(numbers, left, right);
                right--;
            }
        }

        //left == right, and we are deciding where to place the pivot
        if (numbers[left] > numbers[end]) { // numbers[end] is the pivot value
            swap(numbers, left, end);
            return left;
        } else {
            swap(numbers, left + 1, end);
            return left + 1;
        }
    }

    private static void swap(int[] numbers, int indexA, int indexB) {
        int c = numbers[indexA];
        numbers[indexA] = numbers[indexB];
        numbers[indexB] = c;
    }
}

