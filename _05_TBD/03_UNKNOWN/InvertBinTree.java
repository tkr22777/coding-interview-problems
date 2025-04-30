class Solution {

    public TreeNode invertTree(TreeNode root) {
        invert(root);
        return root;
    }

    private void invert(TreeNode node) {

        if (node == null) {
            return;
        }

        invert(node.left);
        invert(node.right);

        TreeNode left = node.left;
        node.left = node.right;
        node.right = left;
    }
}


