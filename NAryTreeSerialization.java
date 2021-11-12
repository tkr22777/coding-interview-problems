import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringJoiner;

public class NAryTreeSerialization {
    public static void main(String[] args) {
        StringJoiner sj = new StringJoiner("|", "", "");
        sj.add(String.valueOf(4));
        String theString = sj.toString();
        System.out.println(theString);
        List<String> split = Arrays.asList(theString.split("|"));
        System.out.println(split.toString());

        IntNode child1 = new IntNode(1, new ArrayList<>());
        IntNode child2 = new IntNode(2, new ArrayList<>());
        IntNode root = new IntNode(0, Arrays.asList(new IntNode[]{child1, child2}));
        String data = new Codec().serialize(root);
        System.out.println("Serialized: " + data);
        IntNode dRoot = new Codec().deserialize(data);
    }
}

/*
* Problem: https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/
* this following suggested solution shows how list is converted to array and the data structure passing via function.
* https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/discuss/151421/Java-preorder-recursive-solution-using-queue
*/

class IntNode {
    public int val;
    public List<IntNode> children;

    public IntNode() {}

    public IntNode(int _val) {
        val = _val;
    }

    public IntNode(int _val, List<IntNode> _children) {
        val = _val;
        children = _children;
    }
};

class Codec {

    public String serialize(IntNode root) {
        if (root == null) {
            return "";
        }
        return _serialize(0, root);
    }

    private String _serialize(int depth, IntNode node) {
        String delim = String.format("[%d]", depth);

        StringJoiner sj = new StringJoiner(delim,"", "");
        sj.add(String.valueOf(node.val));

        if (node.children == null || node.children.size() == 0) {
            return sj.toString();
        }

        for (IntNode child: node.children) {
            sj.add( _serialize(depth + 1, child));
        }
        return sj.toString();
    }

    // Decodes your encoded data to tree.
    public IntNode deserialize(String data) {
        if (data.strip().equals("")) {
            return null;
        }
        return _deserialize(0, data);
    }

    private IntNode _deserialize(int depth, String data) {
        String delim = String.format("\\[%d\\]", depth);

        List<String> subSections = Arrays.asList(data.split(delim));
        List<IntNode> children = new ArrayList<>();

        IntNode node = new IntNode(Integer.parseInt(subSections.get(0)), children);
        for (int i = 1; i < subSections.size(); i++) {
            children.add(_deserialize(depth + 1, subSections.get(i)));
        }

        return node;
    }
}
