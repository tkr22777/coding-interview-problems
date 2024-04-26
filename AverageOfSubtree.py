## https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.averageOfSubtreeHelper(root)[2]
        
    def averageOfSubtreeHelper(self, node):
        
        if not node:
            return (None, None, None)

        (l_count, l_total, l_result) = self.averageOfSubtreeHelper(node.left)
        (r_count, r_total, r_result) = self.averageOfSubtreeHelper(node.right)

        count = 1
        total = node.val
        result = 0

        if l_count:
            count += l_count
            total += l_total
            result += l_result
        
        if r_count:
            count += r_count
            total += r_total
            result += r_result

        average = total / count
    
        if node.val == average:
            return (count, total, result + 1)
        else:
            return (count, total, result)