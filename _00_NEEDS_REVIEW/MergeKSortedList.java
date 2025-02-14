package TOClean;

import java.util.PriorityQueue;

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

public class MergeKSortedList {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length == 0)  {
            return null;
        }

        PriorityQueue<ListNode> queue = new PriorityQueue<>(
            lists.length, (a,b) -> { return Integer.compare(a.val, b.val); }
        );

        for (ListNode list: lists) {
            if (list != null) {
                queue.offer(list);
            }
        }


        if (queue.size() == 0) {
            return null;
        }

        ListNode current = new ListNode(0);
        ListNode head = current;
        ListNode prev = current;

        while (queue.size() > 0) {
            ListNode pqNode = queue.poll();

            //the first node shouldn't be pointed from prev node
            if (current != head) {
                prev.next = current;
            }

            current.val = pqNode.val;
            if (pqNode.next != null) {
                queue.offer(pqNode.next);
            }

            prev = current;
            current = new ListNode(0);
        }

        return head;
    }
}
