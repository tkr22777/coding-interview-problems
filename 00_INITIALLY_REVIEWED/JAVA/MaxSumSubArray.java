import java.util.*;

/*
 nums = { 1, -2, 3, -6, 8 }
 * on each step, we calculate the current max sum that includes the current element
 * then we check if the current max sum is the max sum
 for i = 0, maxAtI -> 1, max ->  1
 for i = 1, maxAtI -> max(1 + (-2), -2)    -> -1,    maxSum -> max(1, -1) -> 1
 for i = 2, maxAtI -> max(-1 + 3  , 3)     ->  3,    maxSum -> max(1, 3)  -> 3
 for i = 3, maxAtI -> max(3 + (-6), -6)    -> -3,    maxSum -> max(3, -3) -> 3
 for i = 4, maxAtI -> max(-3 + 8  , 8)     ->  8,    maxSum -> max(3, 8)  -> 8
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
        int maxSumForI = nums[0];
        int maxSum = nums[0];

        for (int i = 1; i < nums.length; ++i) {
            //System.out.println("Max sum at i:" + maxSumForI + " num:" + nums[i]);
            maxSumForI = Math.max(maxSumForI + nums[i], nums[i]);
            maxSum = Math.max(maxSum, maxSumForI);
        }
        return maxSum;
    }
}
