package TOClean;

public class MinimumSumOfMountainTriplets2 {
    public static void main(String[] args) {
//        int[] nums = new int[]{8, 6, 1, 5, 3};
//        int min_sum = new TOClean.MinimumSumOfMountainTriplets2().minimumSum(nums);
//        System.out.println("Min sum:" + min_sum);

        int[] nums_2 = new int[]{5,4,8,7,10,2};
        int min_sum = new MinimumSumOfMountainTriplets2().minimumSum(nums_2);
        System.out.println("Min sum:" + min_sum);
    }

    static class Sum {
        int i_val;
        int j_val;
        int k_val;

        public int sum() {
            if (i_val == 0 || j_val == 0 || k_val == 0)
                return  -2;
            return i_val + j_val + k_val;
        }
        public void print() {
            System.out.println("i_val" + i_val + " j_val" + j_val + " k_val" + k_val);
        }
    }

    public int minimumSum(int[] nums) {
        if (nums == null || nums.length < 3) {
            return -1;
        }

        Sum[] sums_for_j = new Sum[nums.length];
        // System.out.println("Total Nums:" + nums.length);
        for (int i = 0; i  < nums.length; i++) {
            for (int j = 1; j < nums.length - 1; j++) {
                Sum sum = sums_for_j[j];
                if (sum == null) {
                    sum = new Sum();
                    sum.j_val = nums[j];
                    sums_for_j[j] = sum;
                }

                if (j == i) {
                    continue;
                }

                if (i < j && nums[i] < nums[j]) {

                    if (sum.i_val == 0) {
                        sum.i_val = nums[i];
                    } else if (nums[i] < sum.i_val) {
                        sum.i_val = nums[i];
                    }

                } else if (i > j && nums[i] < nums[j]) {
                    if (sum.k_val == 0) {
                        sum.k_val = nums[i];
                    } else if (nums[i] < sum.k_val) {
                        sum.k_val = nums[i];
                    }
                }
            }
        }

        int min_sum = -1;
        for (int j = 1; j < sums_for_j.length - 1; j++) {
            Sum sum_for_j = sums_for_j[j];
            int sum_j = sum_for_j.sum();
            if (sum_j >= 3) {
                // sum_for_j.print();
                if (min_sum == -1) {
                    min_sum = sum_j;
                } else {
                    min_sum = Math.min(min_sum, sum_j);
                }
            }
        }

        return min_sum;
    }
}
