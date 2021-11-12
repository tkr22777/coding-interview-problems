import java.util.*;

class LongestIncreasingSubsequence {

    /* LIS is the Longest Increasing Subsequence */
    public static void main(String[] args) {
        int[] numbers = {10, 9, 2, 5, 3, 7, 101, 18};
        System.out.println(new LongestIncreasingSubsequence().lengthOfLIS(numbers));
        numbers = new int[]{7, 7, 7, 7, 7, 7, 7};
        System.out.println(new LongestIncreasingSubsequence().lengthOfLIS(numbers));
    }

    //Using DP, Example: 
    //Numbers: { 1, 5, 4, 7 }
    //DP: { 1, 1, 1, 1 }
    //for i = 0, DP[0] -> 1
    //for i = 1, val = 5
    //    j = 0, val = 1, update as 1 < 5, DP[1] -> DP[0] + 1 -> 1 + 1 -> 2
    //for i = 2, val = 4
    //    j = 0, val = 1, update as 1 < 4, DP[2] -> DP[0] + 1 -> 1 + 1 -> 2
    //    j = 1, val = 5,
    //for i = 3, val = 7
    //    j = 0, val = 1, update as 1 < 7, DP[3] -> DP[0] + 1 -> 1 + 1 -> 2
    //    j = 1, val = 5, update as 5 < 7, DP[3] -> DP[1] + 1 -> 2 + 1 -> 3
    //    j = 2, val = 4, update as 4 < 7, DP[3] -> DP[3] -> 3
    public int lengthOfLIS(int[] numbers) {
        int[] dp = new int[numbers.length];
        Arrays.fill(dp, 1);

        int result = 1;
        for (int i = 0; i < numbers.length; i++) {
            for (int j = 0; j < i; j++) {
                if (numbers[i] > numbers[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
            System.out.println("i: " + i + " -> " + dp[i]);
            result = Math.max(result, dp[i]);
        }
        return result;
    }
}
