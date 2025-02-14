import java.io.*;
import java.util.*;
import java.util.stream.*;

class Solution {

  public static void main(String[] args) {

    int[] numbers ={10,9,2,5,3,7,101,18};
    System.out.println(new Solution().lengthOfLIS(numbers));
    System.out.println(new Solution().lengthOfLISArray(numbers));
  }

  public int lengthOfLIS(int[] nums) {

    List<int[]> results = new ArrayList<int[]>();

    for (int i = 0; i < nums.length; i++) {

      int val = nums[i];

      int[] toAddVal = {1 , val};

      for (int[] res: results) {
        if (toAddVal[1] > res[1] && res[0] >= toAddVal[0]) {
          toAddVal = new int[]{res[0] + 1, val};
        }
      }

      List<int[]> toRemove = new ArrayList<int[]>();
      for (int[] res: results) {
        if (res[0] < toAddVal[0] && res[1] >= val) {
          toRemove.add(res);
        }
      }

      results.removeAll(toRemove);
      results.add(toAddVal);
    }

    int LIS = 0;
    for (int[] result:results) {
      LIS = result[0] > LIS? result[0]: LIS;

    }
    return LIS;
  }

  //Similar to buy sell stock
  public int lengthOfLISArray(int[] nums) {

    int[] dp = new int[nums.length];
    Arrays.fill(dp, 1);

    int result = 1;
    for (int i = 0; i < nums.length; i++) {
      for(int j = 0; j < i; j++) {
        if (nums[i] >= nums[j]){
          dp[i] = Math.max(dp[i], dp[j] + 1);
        }
      }
      result = Math.max(result, dp[i]);
    }
    return result;
  }
}


