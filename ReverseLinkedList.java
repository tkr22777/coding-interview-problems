import java.util.*;

/* Kind of stupid, fix imp */
public class ReverseLinkedList {

    public static void main(String[] args) {
        ListNode node1 = new ListNode(1);
        ListNode node2 = new ListNode(2);
        ListNode node3 = new ListNode(3);
        ListNode node4 = new ListNode(4);

        node1.next = node2;
        node2.next = node3;
        node3.next = node4;

        ListNode list1 = node1;
        ListNode listCopy = new ReverseLinkedList().deepCopy(list1);

        printList(list1);
        printList(new ReverseLinkedList().recursiveReverse(list1).head);

        printList(listCopy);
        printList(new ReverseLinkedList().iterativeReverse(listCopy));
    }

    private ListNode deepCopy(ListNode node) {
        if (node == null) {
            return null;
        }

        ListNode copyHead = new ListNode(node.val);

        ListNode copyCurrent = copyHead;
        ListNode current = node.next;
        while (current != null) {
            copyCurrent.next = new ListNode(current.val);
            current = current.next;
            copyCurrent = copyCurrent.next;
        }

        return copyHead;
    }

    static class ListNode {
        ListNode next;
        int val;
        public ListNode(int val) { this.val = val; }
    }

    static class Reversed {
        ListNode head;
        ListNode end;
    }
    
    private Reversed recursiveReverse(ListNode current) {

        if (current == null) { // to handle null list
            return null;
        } 

        if (current.next == null) {
            Reversed r = new Reversed(); r.head = current; r.end = current;
            return r;
        }

        Reversed r = recursiveReverse(current.next);
        r.end.next = current;
        r.end = r.end.next;
        r.end.next = null;
        return r;
    }

    private ListNode iterativeReverse(ListNode head) {

        ListNode temp = null;
        ListNode temp_next = null;
        ListNode curr = head;

        while(curr != null) {
            temp_next = curr;
            curr = curr.next;
            temp_next.next = temp;
            temp = temp_next;
        }

        return temp_next;
    }

    public static void printList(ListNode node) {
        ListNode cur = node;
        while (cur != null) {
            System.out.print(cur.val + " -> ");
            cur = cur.next;
        }
        System.out.println();
    }
}
