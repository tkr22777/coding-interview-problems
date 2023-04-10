import java.util.*;

public class FourSum {

    public static void main(String[] args) {
        new FourSum().fourSum(new int[]{1, 3, 4, 2, 9, 5}, 12);
        new FourSum().fourSum(new int[]{1, 0, -1, 0, -2, 2}, 0);
        new FourSum().fourSum(new int[]{10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90}, 200);
        //Getting TLE for the following test case
        new FourSum().fourSum(new int[]{2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2},8 );
    }

    public List<List<Integer>> fourSum(int[] nums, int target) {
        Map<Integer, List<int[]>> twoSumToIndices = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                int twoSum = nums[i] + nums[j];
                twoSumToIndices.computeIfAbsent(twoSum, v -> new LinkedList<>())
                    .add(new int[]{i, j});
            }
        }
        //System.out.println("Figured Two sums. Total: " + twoSumToIndices.keySet().size());

        Set<List<Integer>> toRet = new HashSet<>();
        Set<Integer> completed = new HashSet<>();
        for (Integer sum: twoSumToIndices.keySet()) {
            int rest = target - sum;
            //System.out.println("Sum:" + sum + " Rest:" + rest);

            if (twoSumToIndices.containsKey(rest)) {
                if (completed.contains(sum)) {
                    continue;
                }
                completed.add(rest);
                List<int[]> indices1 = twoSumToIndices.get(sum);
                List<int[]> indices2 = twoSumToIndices.get(rest);
                for (int[] aIndices1: indices1) {
                    for (int[] aIndices2: indices2) {
                        if (aIndices1[0] == aIndices2[0] ||
                            aIndices1[0] == aIndices2[1] ||
                            aIndices1[1] == aIndices2[0] ||
                            aIndices1[1] == aIndices2[1]) {
                            continue;
                        }
                        List<Integer> theValues = Arrays.asList(nums[aIndices1[0]],
                                nums[aIndices1[1]],
                                nums[aIndices2[0]],
                                nums[aIndices2[1]]);
                        Collections.sort(theValues);
                        toRet.add(theValues);
                    }
                }
            }
        }
        //System.out.println("Sets:" + toRet.toString());
        return new LinkedList<>(toRet);
    }

    /* copied from the comments section of this solution: https://leetcode.com/problems/4sum/discuss/8609/My-solution-generalized-for-kSums-in-JAVA */
    public List<List<Integer>> fourSumOptimized(int[] nums, int target) {
        Arrays.sort(nums);
        return kSum(nums, 0, 4, target);
    }
    private List<List<Integer>> kSum (int[] nums, int start, int k, int target) {
        int len = nums.length;
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if(k == 2) { //two pointers from left and right
            int left = start, right = len - 1;
            while(left < right) {
                int sum = nums[left] + nums[right];
                if(sum == target) {
                    List<Integer> path = new ArrayList<Integer>();
                    path.add(nums[left]);
                    path.add(nums[right]);
                    res.add(path);
                    while(left < right && nums[left] == nums[left + 1]) left++;
                    while(left < right && nums[right] == nums[right - 1]) right--;
                    left++;
                    right--;
                } else if (sum < target) { //move left
                    left++;
                } else { //move right
                    right--;
                }
            }
        } else {
            for(int i = start; i < len - (k - 1); i++) {
                if(i > start && nums[i] == nums[i - 1]) continue;
                List<List<Integer>> temp = kSum(nums, i + 1, k - 1, target - nums[i]);
                for(List<Integer> t : temp) {
                    t.add(0, nums[i]);
                }
                res.addAll(temp);
            }
        }
        return res;
    }
}
