/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
        Set<Integer> toDelSet = Arrays.stream(to_delete).boxed().collect(Collectors.toSet());
        Result res = deleteNodes(root, toDelSet);
        List<TreeNode> toReturn = res.roots;
        if (res.node != null) {
            toReturn.add(res.node);
        }
        return toReturn;
    }

    class Result {
        TreeNode node;
        List<TreeNode> roots = new ArrayList<TreeNode>();
    }

    private Result deleteNodes(TreeNode root, Set<Integer> toDelete) {

        Result res = new Result();

        if (root == null) {
            return res;
        }

        Result resLeft = deleteNodes(root.left, toDelete);
        Result resRight = deleteNodes(root.right, toDelete);
        res.roots.addAll(resLeft.roots);
        res.roots.addAll(resRight.roots);

        if (toDelete.contains(root.val)) {
            //We are ignoring the root
            if (resLeft.node != null) {
                res.roots.add(resLeft.node);
            }

            if (resRight.node != null) {
                res.roots.add(resRight.node);
            }

        } else {
            //We are returning the root
            res.node = root;
            if (resLeft.node != null) {
                root.left = resLeft.node;
            } else {
                root.left = null;
            }

            if (resRight.node != null) {
                root.left = resLeft.node;
            } else {
                root.right = null;
            }
        }

        return res;
    }
}

