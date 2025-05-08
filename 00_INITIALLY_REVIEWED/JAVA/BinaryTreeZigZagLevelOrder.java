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
    
    // Convenience constructor for leaf nodes
    public TreeNode(int val) {
        this(val, null, null);
    }
}

class BinaryTreeZigZagLevelOrder {
    
    /**
     * Core algorithm: ZigZag Level Order Traversal
     * Time Complexity: O(n) where n is the number of nodes
     * Space Complexity: O(n) for the queue and result lists
     */
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
            leftToRight = !leftToRight; // Toggle direction for next level
            
            result.add(currentLevel);
        }
        
        return result;
    }

    //=========================================================================================
    //=========================== Test Driver Code Below ======================================
    //=========================================================================================

    public static void main(String[] args) {
        runAllTests();
        System.out.println("All tests passed!");
    }
    
    private static void runAllTests() {
        BinaryTreeZigZagLevelOrder solution = new BinaryTreeZigZagLevelOrder();
        
        // Test 1: Balanced Binary Tree
        TreeNode tree1 = new TreeNode(3,
            new TreeNode(9),
            new TreeNode(20, new TreeNode(15), new TreeNode(7)));
        assertListEquals(
            Arrays.asList(
                Arrays.asList(3),
                Arrays.asList(20, 9),
                Arrays.asList(15, 7)
            ),
            solution.zigzagLevelOrder(tree1)
        );
        
        // Test 2: Left-skewed Tree
        TreeNode tree2 = new TreeNode(1,
            new TreeNode(2, new TreeNode(3), null), null);
        assertListEquals(
            Arrays.asList(
                Arrays.asList(1),
                Arrays.asList(2),
                Arrays.asList(3)
            ), 
            solution.zigzagLevelOrder(tree2)
        );
        
        // Test 3: Right-skewed Tree
        TreeNode tree3 = new TreeNode(1,
            null, new TreeNode(2, null, new TreeNode(3)));
        assertListEquals(
            Arrays.asList(
                Arrays.asList(1),
                Arrays.asList(2),
                Arrays.asList(3)
            ),
            solution.zigzagLevelOrder(tree3)
        );
        
        // Test 4: Multi-level tree with some missing nodes
        TreeNode tree4 = new TreeNode(1,
            new TreeNode(2,
                new TreeNode(4, new TreeNode(7), null),
                new TreeNode(5)),
            new TreeNode(3,
                null,
                new TreeNode(6, new TreeNode(8), new TreeNode(9))));
        assertListEquals(
            Arrays.asList(
                Arrays.asList(1),
                Arrays.asList(3, 2),
                Arrays.asList(4, 5, 6),
                Arrays.asList(9, 8, 7)
            ),
            solution.zigzagLevelOrder(tree4)
        );
        
        // Test 5: Empty tree
        assertListEquals(
            new ArrayList<>(),
            solution.zigzagLevelOrder(null)
        );
    }
    
    /**
     * Simple assertion utility for list equality
     */
    private static void assertListEquals(List<List<Integer>> expected, List<List<Integer>> actual) {
        assert expected.size() == actual.size() : 
            "Lists have different sizes: expected " + expected.size() + ", got " + actual.size();
            
        for (int i = 0; i < expected.size(); i++) {
            List<Integer> expectedList = expected.get(i);
            List<Integer> actualList = actual.get(i);
            
            assert expectedList.equals(actualList) : 
                "Lists at index " + i + " differ: expected " + expectedList + ", got " + actualList;
        }
    }
}

