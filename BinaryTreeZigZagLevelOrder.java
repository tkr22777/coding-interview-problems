import java.util.*;

/*
 https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
 print nodes at the same depth/level alternating from left to right and
 then right to left..
*/
class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

class NodeDepth {
    TreeNode tnode;
    int depth = 0;
    NodeDepth(TreeNode tnode, int depth) {
        this.tnode = tnode;
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
            NodeDepth node = queue.poll();
            LinkedList<Integer> list = nodesByDepth.computeIfAbsent(node.depth, l -> new LinkedList<>());

            /* Starting from 0th node, left -> right */
            if (node.depth % 2 == 0) {
                list.offerLast(node.tnode.val); //left to right
            } else {
                list.offerFirst(node.tnode.val); //right to left
            }

            if (node.tnode.left != null) {
                NodeDepth leftNode = new NodeDepth(node.tnode.left, node.depth + 1);
                queue.offer(leftNode);
            }

            if (node.tnode.right != null) {
                NodeDepth rightNode = new NodeDepth(node.tnode.right, node.depth + 1);
                queue.offer(rightNode);
            }
        }
        return new LinkedList(nodesByDepth.values());
    }
}

