/*
 * Problem: https://leetcode.com/problems/maximum-product-subarray/
 *
 * Solution:
 *  -> We do not need to return the indexes for max prod sub array, only the result
 *  -> using DP we consider one element from the array and check if that increases the current max
 *  -> we keep another var maxProd to store the max overall as we move
 *
 *   exArr = [ 2, 3, -2, -3 ]
 *  :considering first elem, 2
 *      cMax ----> 2
 *      cMin ----> 2
 *    maxProd ---> 2
 *
 *  :considering second elem, 3
 *     2 * 3   -> 6
 *         3   -> 3
 *
 *      cMax ----> 6
 *      cMin ----> 3
 *     maxProd --> 6
 *
 *  :considering third elem, -2
 *       6, -2 -> -12
 *       3, -2 -> -6
 *
 *      cMax ----> -6
 *      cMin ----> -12
 *     maxProd --> 6
 *
 *  :considering fourth elem, -3
 *        -6, -3 -> 18
 *       -12, -3 -> 36
 *
 *      cMax ----> 36
 *      cMin ----> 18
 *     maxProd --> 36
 */

import java.util.*;

class MaxProductSubArray {

    public static void main(String[] args) {
        System.out.println(Arrays.toString(args));
        int[] nums = {2, 3, -2, -3};
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

        /* note: i starts from 1 */
        for (int i = 1; i < nums.length; ++i) {
            int tempCurrentMax = currentMax;

            currentMax = Math.max( Math.max(currentMax * nums[i], currentMin * nums[i]), nums[i]);
            maxProd = Math.max(maxProd, currentMax);

            currentMin = Math.min( Math.min(tempCurrentMax * nums[i], currentMin * nums[i]), nums[i]);
        }
        return maxProd;
    }
}
