# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Given the root of a binary tree, return the number of nodes where the value
# of the node is equal to the average of the values in its subtree.
class Solution(object):
    def averageOfSubtree(self, root) -> int:
       return self.averageOfSubtreeHelper(root)[2]
        
    def averageOfSubtreeHelper(self, node):
        
        if not node:
            return (None, None, None)

        (l_count, l_total, l_result) = self.averageOfSubtreeHelper(node.left)
        (r_count, r_total, r_result) = self.averageOfSubtreeHelper(node.right)

        count = 1
        total = node.val
        # result is the number of nodes that have the same value as the average of the subtree
        result = 0

        if l_count:
            count += l_count
            total += l_total
            result += l_result
        
        if r_count:
            count += r_count
            total += r_total
            result += r_result

        # average is considered the floor on this problem
        average = int(total / count)

        # print(f"node: {node.val}, count: {count}, total: {total}, result: {result}, average: {average}")
    
        if node.val == average:
            print(f"found a match for {node.val} with average {average}")
            return (count, total, result + 1)
        else:
            return (count, total, result)

# Test case
if __name__ == "__main__":
    # Create a small test tree:
    #       4
    #      / \
    #     8   5
    #    / \   \
    #   0   1   6
    
    root = TreeNode(4)
    root.left = TreeNode(8)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    
    solution = Solution()
    result = solution.averageOfSubtree(root)
    print(f"Number of nodes equal to average of subtree: {result}, valid: {result == 5}")
