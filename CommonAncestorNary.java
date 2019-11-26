import java.util.*;

public class CommonAncestorNary {
 
    public class Node {
        String val;
        Set<Node> next = new HashSet<>();
        public Node(String val) { this.val = val;}
    }

    public class AncestorRet02 {
        boolean found = false;
        String ancestor;
        public AncestorRet02(String ancestor) {this.ancestor = ancestor;} 
        public AncestorRet02(boolean found, String ancestor) { this.found = found; this.ancestor = ancestor;} 
    }

    public AncestorRet02 findAncestor02(Node root, String loc1, String loc2) {

        if (loc1 == null) { //loc1 should not be null
            return null; 
        }

        if (loc2 == null) {
            if (root.val.equals(loc1)) { //loc1 is matches with the current node
                return new AncestorRet02(loc1); 
            } 

            for (Node next: root.next) {
                AncestorRet02 ret = findAncestor02(next, loc1, null);
                if (ret != null) { //loc1 matches with some node down the tree 
                    return ret;
                }
            }
            return null; //no matches under this root 
        }

        if (root.val.equals(loc1)) { 
            for (Node next: root.next) {
                AncestorRet02 res = findAncestor02(next, loc2, null);
                if (res != null) {
                    return new AncestorRet02(true, root.val); //current node is the common ancestor
                }
            }
            return new AncestorRet02(loc1);  //loc1 is matches with the current node
        } 

        if(root.val.equals(loc2)) {
            for (Node next: root.next) {
                AncestorRet02 res = findAncestor02(next, loc1, null);
                if (res != null) {
                    return new AncestorRet02(true, root.val); //current node is the common ancestor
                }
            }
            return new AncestorRet02(loc2);  //loc2 is matches with the current node
        } 

        List<AncestorRet02> results = new ArrayList<>();
        for (Node next: root.next) {
            AncestorRet02 res = findAncestor02(next, loc1, loc2);
            if (res != null) {
                results.add(res);
            }
        }

        if (results.size() == 0) { //no matches under this root 
            return null;
        } else if (results.size() == 1) { //one match under this root 
            return results.get(0);
        } else {
            return new AncestorRet02(true, root.val); //current node is the common ancestor
        }
    }


    /* Helper functions to aid in tests */
    public static void main(String[] args) {
        Node root = new CommonAncestorNary().createTree();
        System.out.println("Common Ancestor: " + new CommonAncestorNary().findAncestor02(root, "B0D1E0", "B0D0E1").ancestor);
        System.out.println("Common Ancestor: " + new CommonAncestorNary().findAncestor02(root, "B0D1E0", "B0D1E1").ancestor);
        System.out.println("Common Ancestor: " + new CommonAncestorNary().findAncestor02(root, "B0D0", "C0").ancestor);
    }

    private Node createTree() {
        Node root = new Node("A");
        Set<Node> bNodes = createNodes("B", 4);
        Set<Node> cNodes = createNodes("C", 4);

        root.next.addAll(bNodes);
        root.next.addAll(cNodes);

        for (Node bNode: bNodes) {
            Set<Node> eNodes = createNodes(bNode.val + "D", 4);
            for (Node eNode: eNodes) {
                eNode.next.addAll(createNodes(eNode.val + "E", 4));
            }
            bNode.next.addAll(eNodes);
        }
        return root;
    }

    private Set<Node> createNodes(String prefix, int count) {
        Set<Node> nodeSet = new HashSet<>();
        for(int i = 0 ; i < count; i++) {
            nodeSet.add(new Node(prefix + "" + i));
        }
        return nodeSet;
    }
}

