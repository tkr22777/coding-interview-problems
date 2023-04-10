import java.util.*;

class LongestIncreasingSubsequence {

    /* LIS is the Longest Increasing Subsequence */
    public static void main(String[] args) {
        int[] numbers = {10, 9, 2, 5, 3, 7, 101, 18};
        System.out.println(new LongestIncreasingSubsequence().lengthOfLIS(numbers));
        numbers = new int[]{7, 7, 7, 7, 7, 7, 7};
        System.out.println(new LongestIncreasingSubsequence().lengthOfLIS(numbers));
    }

    /*
    // Using DP, Example:
    // num: { 1, 5, 4, 7 }
    // dp: { 1, 1, 1, 1 }
    // for i = 0, DP[i] -> 1
    // for i = 1, num[i] = 5
    //     j = 0, num[j] = 1, as num[j] < num[i],  DP[1] -> DP[0] + 1 -> 1 + 1 -> 2
    // for i = 2, num[i] = 4
    //     j = 0, num[j] = 1, as num[j] < num[i], DP[2] -> DP[0] + 1 -> 1 + 1 -> 2
    //     j = 1, num[j] = 5,
    // for i = 3, num[i] = 7
    //     j = 0, num[j] = 1, as num[j] < num[i], DP[3] -> DP[0] + 1 -> 1 + 1 -> 2
    //     j = 1, num[j] = 5, as num[j] < num[i], DP[3] -> DP[1] + 1 -> 2 + 1 -> 3
    //     j = 2, num[j] = 4, as num[j] < num[i], DP[3] -> DP[3] -> 3
    */

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
