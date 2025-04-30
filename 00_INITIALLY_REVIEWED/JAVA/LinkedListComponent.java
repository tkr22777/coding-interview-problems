import java.util.HashSet;
import java.util.Set;

public class LinkedListComponent {
    static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
    public static void main(String[] args) {

    }
    public int numComponents(ListNode head, int[] nums) {
        Set<Integer> numsSet = new HashSet<>();
        for (int num: nums) {
            numsSet.add(num);
        }

        System.out.println("Numset:" + numsSet.toString());

        boolean connected = false;
        int connected_count = 0;

        ListNode current = head;
        while (current != null) {
            if (numsSet.contains(current.val)) {
                if (!connected) {
                    connected_count++;
                    connected = true;
                }
            } else {
                connected = false;
            }

            current = current.next;
        }
        return connected_count;
    }
}
