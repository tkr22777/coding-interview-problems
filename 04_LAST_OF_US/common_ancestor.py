# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def find_path(n: 'TreeNode', v: int):
            if n is None:
                return []

            if n.val == v:
                return [v]

            left_path = find_path(n.left, v)
            right_path = find_path(n.right, v)

            if len(left_path) > 0:
                left_path.append(n.val)
                return left_path

            if len(right_path) > 0:
                right_path.append(n.val)
                return right_path

            return []

        path_p = list(reversed(find_path(root, p.val)))
        path_q = list(reversed(find_path(root, q.val)))
        # print(f"p_path:{path_p}")
        # print(f"q_path:{path_q}")

        lower_len = min(len(path_p), len(path_q))

        common_ancestor = None
        for i in range(lower_len):
            if path_q[i] != path_p[i]:
                break
            common_ancestor = path_p[i]

        return TreeNode(common_ancestor)
