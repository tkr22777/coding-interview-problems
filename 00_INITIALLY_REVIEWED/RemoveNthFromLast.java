/* https://leetcode.com/problems/remove-nth-node-from-end-of-list/ */

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

public class RemoveNthFromLast {
    public static void main(String[] args) {
        System.out.println("Compiling..");
    }

    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head == null) {
            return head;
        }

        ListNode current = head;
        int len = 0;
        while (current != null) {
            current = current.next;
            len++;
        }

        int k = len - n; //kth node from left

        current = head;
        ListNode priorCurrent = null;
        for (int i = 0; i < k; i++) {
            priorCurrent = current;
            current = current.next;
        }

        //If it is actually the head element
        if (current == head) {
            head = current.next;
            current.next = null;
        } else {
            priorCurrent.next = current.next;
            current.next = null;
        }

        return head;
    }
}