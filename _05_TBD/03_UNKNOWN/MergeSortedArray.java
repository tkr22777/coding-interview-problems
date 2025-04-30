class Solution {

    public void merge(int[] nums1, int m, int[] nums2, int n) {

        int oneCur = m - 1;
        int twoCur = n - 1;

        for (int i = m + n - 1; i >= 0; --i) {

            int num = 0;

            if (oneCur >= 0 && twoCur >= 0) {
                num = nums1[oneCur] > nums2[twoCur] ? nums1[oneCur--] : nums2[twoCur--];
            } else if (twoCur >= 0) {
                num = nums2[twoCur--];
            } else {
                num = nums1[oneCur--];
            }

            nums1[i] = num;
        }
    }
}

