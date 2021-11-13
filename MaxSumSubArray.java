import java.util.*;

/*
 nums = { 1, -2, 3, -6, 8 }
 * on each step, we calculate the current max sum that includes the current element
 * then we check if the current max sum is the max sum
 for i = 0, (cmax, max) = (1, 1)
 for i = 1, (cmax, max) = (-1, 1)
 for i = 2, (cmax, max) = (3, 2)
 for i = 3, (cmax, max) = (-3, 2)
 for i = 4, (cmax, max) = (8, 8)
*/

public class MaxSumSubArray{

    public static void main(String[] args)  {
        int[] nums = { 1, -2, 3, -6, 8 };
        int maxSum = new MaxSumSubArray().maxSubArray(nums);
        StringJoiner sj = new StringJoiner(", ", "Given Array: ", ".");
        Arrays.stream(nums).boxed().forEach(v -> sj.add(Integer.toString(v)));
        System.out.println(sj.toString());
        System.out.println("Max sum:" + maxSum);
    }

    public int maxSubArray(int[] nums) {
        int maxSum = nums[0];
        int currentSum = nums[0];

        for (int i = 1; i < nums.length; ++i) {
            //System.out.println("Current sum:" + currentSum + " num:" + nums[i]);
            currentSum = Math.max(currentSum + nums[i], nums[i]);
            maxSum = Math.max(maxSum, currentSum);
        }
        return maxSum;
    }
}
