import java.util.*;
import java.util.stream.*;

class LongestCommonSubsequence {
  public static void main(String[] args) {
    String text1 = "abcde";
    String text2 = "ace";
    System.out.println(new LongestCommonSubsequence().longestCommonSubsequence(text1, text2));
  }

  /* TODO add explanation*/
  public int longestCommonSubsequence(String text1, String text2) {
    int[][] memo = new int[text1.length()][text2.length()];
    IntStream.range(0, text1.length())
        .forEach(i -> Arrays.fill(memo[i], -1));
    //return this.lcsRecursive(text1, text1.length() - 1, text2, text2.length() - 1, memo);
    return this.lcsBottomUp(text1, text2);
  }

  public int lcsRecursive(String text1, int t1End, String text2, int t2End, int[][] memo) {
    if (t1End == -1 || t2End == -1) {
      return 0;
    }

    if (memo[t1End][t2End] != -1) {
      return memo[t1End][t2End];
    }

    int retVal;
    if (text1.charAt(t1End) == text2.charAt(t2End)) {
      int ifCounted = 1 + this.lcsRecursive(text1, t1End - 1, text2, t2End - 1, memo);
      int notCounted1 = this.lcsRecursive(text1, t1End, text2, t2End - 1, memo);
      int notCounted2 = this.lcsRecursive(text1, t1End - 1, text2, t2End, memo);
      retVal = Math.max( Math.max(notCounted1, notCounted2), ifCounted);
    } else {
      int notCounted1 = this.lcsRecursive(text1, t1End, text2, t2End - 1, memo);
      int notCounted2 = this.lcsRecursive(text1, t1End - 1, text2, t2End, memo);
      retVal = Math.max(notCounted1, notCounted2);
    }

    memo[t1End][t2End] = retVal;
    return retVal;
  }

  /* To do add explanation */
  public int lcsBottomUp(String text1, String text2) {
    int[][] dp = new int[text1.length() + 1][text2.length() + 1];

    for (int i = 0; i < text1.length(); ++i) {
      for (int j = 0; j < text2.length(); ++j) {
        if (text1.charAt(i) == text2.charAt(j)) {
          int ifCounted = 1 + dp[i][j];
          int notCounted1 = dp[i][j + 1];
          int notCounted2 = dp[i + 1][j];
          dp[i + 1][j + 1] = Math.max( Math.max(notCounted1, notCounted2), ifCounted);
        } else {
          int notCounted1 = dp[i][j + 1];
          int notCounted2 = dp[i + 1][j];
          dp[i + 1][j + 1] = Math.max(notCounted1, notCounted2);
        }
      }
    }

    return dp[text1.length()][text2.length()];
  }
}

