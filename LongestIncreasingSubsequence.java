import java.io.*;
import java.util.*;
import java.util.stream.*;

class LongestIncreasingSubsequence {

    /* LIS is the Longest Increasing Subsequence */
    public static void main(String[] args) {
        int[] numbers = {10, 9, 2, 5, 3, 7, 101, 18};
        System.out.println(new LongestIncreasingSubsequence().lengthOfLIS(numbers));
        System.out.println(new LongestIncreasingSubsequence().lengthOfLISArray(numbers));
    }

    //Using DP, Example: 
    //Numbers: { 1, 5, 4, 7 }
    //DP: { 1, 1, 1, 1 }
    //for i = 0, DP[0] -> 1
    //for i = 1, val = 5
    //    j = 0, val = 1, DP[1] -> DP[0] + 1 -> 1 + 1 -> 2
    //for i = 2, val = 4
    //    j = 0, val = 1, DP[2] -> DP[0] + 1 -> 1 + 1 -> 2
    //    j = 1, val = 5
    //for i = 3, val = 7
    //    j = 0, val = 1, DP[3] -> DP[0] + 1 ->  1 + 1 -> 2
    //    j = 1, val = 5, DP[3] -> DP[1] + 1 -> 2 + 1 -> 3
    //    j = 2, val = 4, DP[3] -> DP[3] -> 3
    public int lengthOfLISArray(int[] numbers) {

        int[] dp = new int[numbers.length];
        Arrays.fill(dp, 1);

        int result = 1;
        for (int i = 0; i < numbers.length; i++) {
            for (int j = 0; j < i; j++) {
                if (numbers[i] >= numbers[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            result = Math.max(result, dp[i]);
        }
        return result;
    }

    public int lengthOfLIS(int[] numbers) {

        //We are going to keep the candidate results
        List<int[]> results = new ArrayList<int[]>();

        //for each number we are going to calculate if a 
        //number is greater than an existing result
        for (int i = 0; i < numbers.length; i++) {

            int val = numbers[i];

            int[] toAddVal = { 1, val };
            for (int[] res: results) {
                if (val > res[1] && res[0] >= toAddVal[0]) {
                    toAddVal = new int[]{res[0] + 1, val}; 
                }
            }

            List<int[]> toRemove = new ArrayList<int[]>();
            for (int[] res: results) {
                //these candidate results will not contribute
                //to the longest increasing subsequence
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
}

