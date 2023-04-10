import java.util.*;

class BinarySearch {
    public static void main(String[] args) {
        int[] sortedAr = {1, 2, 5, 7, 9, 11};
        System.out.println("Given Array: " + Arrays.toString(sortedAr));
        System.out.printf("Search %s Result: %s%n", 5, search(sortedAr, 5));
        System.out.printf("Search %s Result: %s%n", 9, search(sortedAr, 9));
        System.out.printf("Search %s Result: %s%n", 6, search(sortedAr, 6));
    }

    public static int search(int[] sortedNumbers, int target) {
        int begin = 0;
        int end  = sortedNumbers.length - 1;

        // target should be in range num0 <= target <= numN
        if (target < sortedNumbers[begin] || target > sortedNumbers[end]) {
            return -1;
        }

        while (begin <= end) {
            int mid = (begin + end) / 2;
            
            if (sortedNumbers[mid] == target) {
                return mid;
            }

            if (target > sortedNumbers[mid]) {
                begin = mid + 1;
            } else {
                end = mid - 1;
            }
        }
        return -1;
    }
}
