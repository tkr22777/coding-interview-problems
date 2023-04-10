import java.util.*;

/*
 https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
 print nodes at the same depth/level alternating from left to right and
 then right to left.
*/
class TreeNode {
    TreeNode left;
    TreeNode right;
    int value;

    public TreeNode(int val, TreeNode left, TreeNode right) {
        this.value = val;
        this.left = left;
        this.right = right;
    }
}

class NodeDepth {
    TreeNode node;
    int depth = 0;
    NodeDepth(TreeNode node, int depth) {
        this.node = node;
        this.depth = depth;
    }
}

class BinaryTreeZigZagLevelOrder {

    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        if (root == null) {
            return new ArrayList<>();
        }

        /* to keeps the order of lists by depth */
        TreeMap<Integer, LinkedList<Integer>> nodesByDepth = new TreeMap<>();

        Queue<NodeDepth> queue = new LinkedList<>();
        queue.offer(new NodeDepth(root, 0));

        while (queue.size() > 0) {
            NodeDepth nodeDepth = queue.poll();
            LinkedList<Integer> list = nodesByDepth.computeIfAbsent(nodeDepth.depth, l -> new LinkedList<>());

            /* Starting from 0th node, left -> right */
            if (nodeDepth.depth % 2 == 0) {
                list.offerLast(nodeDepth.node.value); //left to right
            } else {
                list.offerFirst(nodeDepth.node.value); //right to left
            }

            if (nodeDepth.node.left != null) {
                NodeDepth leftNode = new NodeDepth(nodeDepth.node.left, nodeDepth.depth + 1);
                queue.offer(leftNode);
            }

            if (nodeDepth.node.right != null) {
                NodeDepth rightNode = new NodeDepth(nodeDepth.node.right, nodeDepth.depth + 1);
                queue.offer(rightNode);
            }
        }
        return new LinkedList<>(nodesByDepth.values());
    }
}

