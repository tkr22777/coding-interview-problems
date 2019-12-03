import java.util.*;

public class MaxSumSubArray{

	public static void main(String[] args)  {

		int[] nums = {-2,1,-3,4,-1,2,1,-5,4};
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
            currentSum = Math.max(currentSum + nums[i], nums[i]);
            maxSum = Math.max(maxSum, currentSum);
        }
        return maxSum;
    }
}
