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

class BinaryTreeZigZagLevelOrder {

    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null) {
            return result;
        }
        
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);
        boolean leftToRight = true;
        
        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            List<Integer> currentLevel = new ArrayList<>(levelSize);
            
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                
                // Add to current level (we'll reverse later if needed)
                currentLevel.add(node.value);
                
                // Add children to queue for next level
                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }
            
            // Reverse alternate levels to create zigzag pattern
            if (!leftToRight) {
                Collections.reverse(currentLevel);
            }
            
            result.add(currentLevel);
            leftToRight = !leftToRight; // Toggle direction for next level
        }
        
        return result;
    }
}

