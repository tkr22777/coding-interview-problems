import java.util.*;

//https://leetcode.com/problems/partition-array-for-maximum-sum/submissions/

class MaximumSumAfterPartitioning {
    public static void main(String[] args) {
        int[] ar = {1,15,7,9,2,5,10};
        System.out.println(new MaximumSumAfterPartitioning().maxSumAfterPartitioning(ar,3));
    }

    public int maxSumAfterPartitioning(int[] A, int K) {
        Map<Integer, Integer> memo = new HashMap<>();
        return maxSumAfterPartitioningRec(A, 0, K, memo);
    }

    public int maxSumAfterPartitioningRec(int[] A, int index, int K, Map<Integer, Integer> memo) {
        // base case for recursion
        if (index >= A.length) {
            return 0;
        }

        if (memo.containsKey(index)) {
            return memo.get(index);
        }

        int maxInK = A[index];
        int maxSum = A[index];
        // i goes from (index to index + K) and checks for max sum recursively
        for (int i = index; i < index + K && i < A.length; i++) {
            maxInK = Math.max(A[i], maxInK); //the max in the range index to index + K
            int ithKSum = maxInK * (i - index + 1);
            int currentMaxSum =  ithKSum + maxSumAfterPartitioningRec(A, i + 1, K, memo);
            maxSum = Math.max(currentMaxSum, maxSum);
        }

        memo.put(index, maxSum);
        return maxSum;
    }
}
