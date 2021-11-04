/*
 * Problem: https://leetcode.com/problems/maximum-product-subarray/
 */

import java.util.*;

/* TODO add explanation */
class MaxProductSubArray {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(args));
        int[] nums = {2,3,-2,4};
        int maxProd = new MaxProductSubArray().maxProduct(nums);

        StringJoiner sj = new StringJoiner(", ", "Given Array: ", ".");
        Arrays.stream(nums).boxed().forEach(v -> sj.add(Integer.toString(v)));
        System.out.println(sj.toString());

        System.out.println("Max prod:" + maxProd);
    }
    
    /* we keep the current min since a negative current min could flip to 
     * current max when current max is multiplied by another negative number */
    public int maxProduct(int[] nums) {
        int currentMax = nums[0];
        int currentMin = nums[0]; 
        int maxProd = nums[0];

        /* Note that i starts from 1 */
        for (int i = 1; i < nums.length; ++i) {
            int tempCurrentMax = currentMax;
            currentMax = Math.max( Math.max(currentMax * nums[i], currentMin * nums[i]) , nums[i]);
            currentMin = Math.min( Math.min(tempCurrentMax * nums[i], currentMin * nums[i]) , nums[i]);
            maxProd = Math.max(maxProd, currentMax);
        }
        return maxProd;
    }
}

