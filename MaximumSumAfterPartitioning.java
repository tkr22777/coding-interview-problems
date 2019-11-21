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

        if (index >= A.length) return 0;

        if (memo.containsKey(index)) {
            return memo.get(index);
        }

        int maxInK = A[index], maxSumB = A[index];

        for (int i = index; i < index + K && i < A.length; i++) {
            maxInK = Math.max(A[i], maxInK);
            maxSumB = Math.max((maxInK * (i - index + 1)) + maxSumAfterPartitioningRec(A, i + 1, K, memo), maxSumB);
        }

        memo.put(index, maxSumB);
        return maxSumB;
    }
}

