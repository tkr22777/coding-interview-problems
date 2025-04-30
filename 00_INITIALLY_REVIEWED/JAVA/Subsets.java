import java.util.*;
public class Subsets {

    public static void main(String[] args) {
        int[] testCase1 = new int[] {0, 1};
        List<List<Integer>> subsets = subsets(testCase1);

        for (List<Integer> list : subsets) {
            System.out.println(list.toString());
        }

        int[] testCase2 = new int[] {0, 1, 2, 3};
        List<List<Integer>> subsets2 = subsets(testCase2);
        for (List<Integer> list : subsets2) {
            System.out.println(list.toString());
        }
    }
    public static List<List<Integer>> subsets(int[] nums) {
        return subsets(nums, 0);
    }

    public static List<List<Integer>> subsets(int[] nums, int index) {
        if (index == nums.length - 1) {
            LinkedList<List<Integer>> list = new LinkedList<>();
            list.add(new LinkedList<>());
            LinkedList<Integer> withElement = new LinkedList<>();
            withElement.offer(nums[index]);
            list.add(withElement);
            return list;
        }

        List<List<Integer>> lists = subsets(nums, index + 1);
        List<List<Integer>> newLists = new LinkedList<>();

        for (List<Integer> aList: lists) {
            newLists.add(aList);
            LinkedList<Integer> withNumber = new LinkedList<>(aList);
            withNumber.offerFirst(nums[index]);
            newLists.add(withNumber);
        }
        return newLists;
    }
}
