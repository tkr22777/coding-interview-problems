# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def maxSumBST(self, root: Optional[TreeNode]) -> int:

        # Return values: (is_bst, subtree_sum, min_val, max_val, global_max)
        
        if not root:
            return 0

        def max_sum(node: TreeNode):
            if not node:
                return True, 0, float('inf'), float('-inf'), 0
            
            print(f"Visiting node: {node.val}")

            # Get info from left and right subtrees
            left_bst, left_sum, left_min, left_max, left_global_max = max_sum(node.left)
            right_bst, right_sum, right_min, right_max, right_global_max = max_sum(node.right)
            
            print(f"  Left subtree - BST: {left_bst}, Sum: {left_sum}, Min: {left_min}, Max: {left_max}")
            print(f"  Right subtree - BST: {right_bst}, Sum: {right_sum}, Min: {right_min}, Max: {right_max}")
            
            # Check if current subtree can form a BST
            if left_bst and right_bst and left_max < node.val < right_min:
                # Current subtree is a valid BST
                current_sum = left_sum + node.val + right_sum
                current_min = left_min if node.left else node.val
                current_max = right_max if node.right else node.val
                
                # Update global maximum
                current_global_max = max(left_global_max, right_global_max, current_sum)
                
                print(f"  Valid BST! Sum: {current_sum}, Global max so far: {current_global_max}")
                return True, current_sum, current_min, current_max, current_global_max
            else:
                # Current subtree is not a BST
                current_global_max = max(left_global_max, right_global_max)
                print(f"  Invalid BST. Global max so far: {current_global_max}")
                return False, 0, 0, 0, current_global_max

        _, _, _, _, result = max_sum(root)
        return result


# Test the solution
if __name__ == "__main__":
    # Test case: [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
    #       1
    #      / \
    #     4   3
    #    / \ / \
    #   2  4 2  5
    #          / \
    #         4   6
    
    # Expected: 20 (subtree [4,2,4,null,null,4,6] with sum 4+2+4+4+6=20)
    
    root = TreeNode(1)
    root.left = TreeNode(4)
    root.right = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(5)
    root.right.right.left = TreeNode(4)
    root.right.right.right = TreeNode(6)
    
    solution = Solution()
    result = solution.maxSumBST(root)
    print(f"\nFinal result: {result}")
    print("Expected: 20")
    
    # Test case 2: Simple BST [4,3,null,1,2]
    print("\n" + "="*50)
    print("Test case 2:")
    root2 = TreeNode(4)
    root2.left = TreeNode(3)
    root2.left.left = TreeNode(1)
    root2.left.right = TreeNode(2)
    
    result2 = solution.maxSumBST(root2)
    print(f"\nFinal result: {result2}")
    print("Expected: 2 (just the leaf node 2)")

