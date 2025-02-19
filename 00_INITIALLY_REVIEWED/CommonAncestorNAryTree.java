/*
    Find the common ancestor of two nodes in an N-ary tree, all nodes have unique values
 */
import java.util.*;

class Node {
    String val;
    Set<Node> next = new HashSet<>();
    public Node(String val) { this.val = val;}
}

class AncestorRet {
    String val;
    boolean foundBoth;
    public AncestorRet(String val, boolean foundBoth) { this.val = val; this.foundBoth = foundBoth;}
}

class CommonAncestorNAryTree {

    public static void main(String[] args) {
        Node root = Helper.createTestTree();
        System.out.println("Common Ancestor: " + new CommonAncestorNAryTree().findAncestor(root, "B0D1E0", "B0D0E1").val);
        System.out.println("Common Ancestor: " + new CommonAncestorNAryTree().findAncestor(root, "B0D1E0", "B0D1E1").val);
        System.out.println("Common Ancestor: " + new CommonAncestorNAryTree().findAncestor(root, "B0D0", "C0").val);
    }

    public AncestorRet findAncestor(Node root, String val1, String val2) {
        if (root.val.equals(val1) || root.val.equals(val2)) { // one of the values matched current node
            String match = root.val.equals(val1)? val1: val2;

            // we want to check if the non-matched value is in the subtree
            String toFind = root.val.equals(val1)? val2: val1; // the other value to find
            for (Node next: root.next) {
                boolean found = inSubtree(next, toFind);
                if (found) {
                    return new AncestorRet(root.val, true); // current node is the common ancestor
                }
            }
            return new AncestorRet(match, false);  // single value match with the current node
        }

        // checking for val1 or val2 match in child nodes
        List<AncestorRet> results = new ArrayList<>();
        for (Node next: root.next) {
            AncestorRet res = findAncestor(next, val1, val2);
            if (res != null) {
                results.add(res);
            }
        }

        if (results.size() == 2) { //2 matches, current node is the common ancestor
            return new AncestorRet(root.val, true);
        } else if (results.size() == 1) { //maybe an ancestor or a match found, we pass it above
            return results.get(0);
        } else {
            return null; //no matches under this root
        }
    }

    public boolean inSubtree(Node node, String val) {
        if (node.val.equals(val)) { //val match on the node
            return true;
        }

        for (Node next : node.next) {
            if (inSubtree(next, val)) {
                return true;
            }
        }
        return false;
    }
}

class Helper {
    /* Helper functions to aid in testing */
    public static Node createTestTree() {
        Node root = new Node("A");
        Set<Node> bNodes = createNodes("B", 4);
        Set<Node> cNodes = createNodes("C", 4);

        root.next.addAll(bNodes);
        root.next.addAll(cNodes);

        for (Node bNode : bNodes) {
            Set<Node> eNodes = createNodes(bNode.val + "D", 4);
            for (Node eNode : eNodes) {
                eNode.next.addAll(createNodes(eNode.val + "E", 4));
            }
            bNode.next.addAll(eNodes);
        }
        return root;
    }

    private static Set<Node> createNodes(String prefix, int count) {
        Set<Node> nodeSet = new HashSet<>();
        for (int i = 0; i < count; i++) {
            nodeSet.add(new Node(prefix + "" + i));
        }
        return nodeSet;
    }
}
