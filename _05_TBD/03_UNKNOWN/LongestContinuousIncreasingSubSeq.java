class Solution {

    public int findLengthOfLCIS(int[] nums) {

        if (nums == null || nums.length == 0) return 0;

        int maxLen = 1;

        for (int i = 0; i < nums.length; i++) {
            int start = i;
            while (i + 1 < nums.length && nums[i] < nums[i+1]) i++;
            if (i > start) {
                maxLen = Math.max(maxLen, i + 1 - start);
            }
        }
        return maxLen;
    }
}


