package TOClean;
/* https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/ */

public class LongestSubarray {

    public int longestSubarray(int[] nums) {
        if (nums.length < 2) {
            return 0;
        }

        int[] countsLeftToRight = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                countsLeftToRight[i] = 1;
            }

            if (i - 1 >= 0 && nums[i] == 1) {
                countsLeftToRight[i] += countsLeftToRight[i-1];
            }
        }

        int[] countsRightToLeft = new int[nums.length];
        for (int i = nums.length - 1; i >= 0; i--) {
            if (nums[i] == 1) {
                countsRightToLeft[i] = 1;
            }

            if (i + 1 < nums.length && nums[i] == 1) {
                countsRightToLeft[i] += countsRightToLeft[i+1];
            }
        }

        int longest = 0;
        for (int i = 0; i < nums.length; i++) {
            int total = countsLeftToRight[i];
            if ((i + 2 < nums.length) && (nums[i + 1] != 1)) {
                total = total + countsRightToLeft[i+2];
            }
            longest = Math.max(total, longest);
        }

        if (longest == nums.length) { //if all ones, we must remove one
            longest--;
        }

        return longest;
    }

    public int longestSubarrayOptimized(int[] nums) {
        int prevCount = 0, count = 0, result = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                count++;
            } else {
                //only a prior non 1 element keeps prevCount non-zero
                result = Math.max(result, count + prevCount);

                prevCount = count;
                count = 0;
            }
        }
        result = Math.max(result, count + prevCount);
        return result == nums.length ? result - 1 : result;  //if all ones, must remove one;
    }
}
