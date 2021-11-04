import java.util.*;

public class ThreeSum {

    public static void main(String[] args) {
        int[] array = { -1, 0, 1, 2 , -1, -4};
        List<List<Integer>> indicesWithZeroSum = threeSum(array);
        for (List<Integer> indexes: indicesWithZeroSum) {
            indexes.stream().forEach(System.out::print);
            System.out.println();
        }
    }

    public static List<List<Integer>> threeSum(int[] nums) {
        Map<Integer, List<List<Integer>>> twoSumToPairs = getTwoSumToOrderedPair(nums);

        List<List<Integer>> solution = new ArrayList<>();
        for (int k = 0 ; k < nums.length; k++) {
            int key = -1 * nums[k];
            if (twoSumToPairs.containsKey(key)) {
                for (List<Integer> pair: twoSumToPairs.get(key)) {
                    if (k > pair.get(0) && k > pair.get(1)) { //to avoid duplication, only consider this
                        List<Integer> triplet = new ArrayList(Arrays.asList(pair.get(0), pair.get(1), k));
                        solution.add(triplet);
                    }
                }
            }
        }
        return solution;
    }

    public static Map<Integer, List<List<Integer>>> getTwoSumToOrderedPair(int[] nums) {
        Map<Integer, List<List<Integer>>> twoSumToPairs = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length ; j++) {
                twoSumToPairs.computeIfAbsent(nums[i] + nums[j], t -> new ArrayList<>());
                twoSumToPairs.get(nums[i] + nums[j]).add(Arrays.asList(i , j));
            }
        }

        return twoSumToPairs;
    }
}
