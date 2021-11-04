import java.util.*;

/* TODO add explanation, very confusing */
public class MValCommonAncestor {

    public class Node {
        String val;
        Set<Node> next = new HashSet<>();
        public Node(String val) { this.val = val;}
    }

    public class AncestorRet {
        Set<String> found;
        String ancestor;
        public AncestorRet(Set<String> found) { this.found = found;}
        public AncestorRet(Set<String> found, String ancestor) { this.found = found; this.ancestor = ancestor;}
    }

    public AncestorRet findAncestor(Node root, String a, String b) {
        Set<String> toFind = new HashSet<>(Arrays.asList(a, b));
        return findAncestor(root, toFind, toFind);
    }

    public AncestorRet findAncestor(Node root, Set<String> origin, Set<String> toFind) {

        if (origin.size() < 2) {
            return null;
        }

        if (toFind.size() == 0) {
            return new AncestorRet(new HashSet<>());
        }

        Set<String> found = new HashSet<>();
        if (toFind.contains(root.val)) {
            found.add(root.val);
        }

        if (found.equals(toFind)) {
            return new AncestorRet(new HashSet<>(found));
        }

        Set<String> notFound = new HashSet<>(toFind);
        notFound.removeAll(found);

        for (Node next: root.next) {
            AncestorRet result = findAncestor(next, origin, notFound);
            if (result.ancestor != null) {
                return result;
            }
            found.addAll(result.found);
        }

        if (found.equals(origin)) {
            return new AncestorRet(found, root.val);
        }
        return new AncestorRet(found);
    }

    /* Helper functions to aid in tests */
    public static void main(String[] args) {
        Node root = new MValCommonAncestor().createTree();
        System.out.println("Common Ancestor: " + new MValCommonAncestor().findAncestor(root, "B0D1E0", "B0D0E1").ancestor);
        System.out.println("Common Ancestor: " + new MValCommonAncestor().findAncestor(root, "B0D1E0", "B0D1E1").ancestor);
        System.out.println("Common Ancestor: " + new MValCommonAncestor().findAncestor(root, "B0D0", "C0").ancestor);
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

