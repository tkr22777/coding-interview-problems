import java.util.*;

//Check Leetcode: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */


class BinaryTreeZigZagLevelOrder {

    class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int x) { val = x; }
    }

    public static void main(String[] args) {
    }

    class Node {
        TreeNode tnode;
        int depth = 0;
        Node(TreeNode tnode) { this.tnode = tnode; }
    }

    TreeMap<Integer, LinkedList<Integer>> map = new TreeMap<>();

    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {

        if (root == null) {
            return new ArrayList<>();
        }

        Queue<Node> queue = new LinkedList<>();
        queue.offer(new Node(root));

        while (queue.size() > 0) {

            Node node = queue.poll();

            LinkedList<Integer> list = map.getOrDefault(node.depth, new LinkedList<>());
            map.put(node.depth, list);

            if (node.depth % 2 == 0) {
                list.offerLast(node.tnode.val);
            } else {
                list.offerFirst(node.tnode.val);
            }

            if (node.tnode.left != null) {
                Node leftNode = new Node(node.tnode.left);
                leftNode.depth = node.depth + 1;
                queue.offer(leftNode);
            }

            if (node.tnode.right != null) {
                Node rightNode = new Node(node.tnode.right);
                rightNode.depth = node.depth + 1;
                queue.offer(rightNode);
            }
        }

        return new LinkedList(map.values());
    }
}

