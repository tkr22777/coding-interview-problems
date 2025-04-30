
class Solution {

    public class ListNode {
        int val;
        ListNode next;
        ListNode(int x) { val = x; }
    }

    public ListNode mergeKLists(ListNode[] lists) {

        if (lists.length == 0)  { return null; }

        PriorityQueue<ListNode> queue = new PriorityQueue<>(
                lists.length, (a,b) -> { return Integer.compare(a.val, b.val); }
                );

        Arrays.stream(lists)
            .filter(list -> list != null)
            .forEach(list -> queue.offer(list));

        ListNode head = null;
        ListNode current = null;
        ListNode prev = null;

        while (queue.size() > 0) {

            ListNode pqNode = queue.poll();

            if (current == null) {
                current = new ListNode(0);
            }

            if (head == null) {
                head = current;
            }

            current.val = pqNode.val;
            if (pqNode.next != null) {
                queue.offer(pqNode.next);
            }

            if (prev != null) {
                prev.next = current;
            }

            prev = current;
            current = null;
        }

        return head;
    }
}

