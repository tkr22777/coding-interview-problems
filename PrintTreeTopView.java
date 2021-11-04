import java.util.*;

class NodeMeta {
    TreeNode node;
    int depth;
    int horizontalDistance; //from center/root at 0
    public NodeMeta(TreeNode node, int depth, int horizontalDistance) {
        this.node = node;
        this.depth = depth;
        this.horizontalDistance = horizontalDistance;
    }
}

public class PrintTreeTopView {

    public static void main(String[] args) {
        TreeNode leftL = new TreeNode(5, null, null);
        TreeNode leftRRR = new TreeNode(8, null, null);
        TreeNode leftRR = new TreeNode(11, null, leftRRR);
        TreeNode leftR = new TreeNode(7, null, leftRR);
        TreeNode left = new TreeNode(4, leftL, leftR);
        TreeNode rightL = new TreeNode(1, null, null);
        TreeNode right = new TreeNode(9, rightL, null);
        TreeNode root = new TreeNode(4, left, right);
        System.out.println("Tree top view: " + new PrintTreeTopView().treeTopView(root));
    }

    public String treeTopView(TreeNode root) {
        //TreeMap keeps top level view from left to right
        TreeMap<Integer, Integer> viewMap = new TreeMap<>();

        Queue<NodeMeta> q = new ArrayDeque<>();
        q.offer(new NodeMeta(root, 0, 0));

        while (!q.isEmpty()) {
            NodeMeta nm = q.poll();

            /*
             * Since this is a BFS, the following condition makes sure we
             * are only storing the top most element for a horizontal distance.
             */
            if (!viewMap.containsKey(nm.horizontalDistance)) {
                viewMap.put(nm.horizontalDistance, nm.node.value);
            }

            if (nm.node.left != null) {
                q.offer(new NodeMeta(nm.node.left, nm.depth + 1, nm.horizontalDistance - 1));
            }

            if (nm.node.right != null) {
                q.offer(new NodeMeta(nm.node.right, nm.depth + 1, nm.horizontalDistance + 1));
            }
        }

        StringBuilder sb = new StringBuilder();
        for (Integer key: viewMap.keySet()) {
            sb.append(viewMap.get(key));
        }
        return sb.toString();
    }
}
