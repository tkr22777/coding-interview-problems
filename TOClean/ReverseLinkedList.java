package TOClean;
import java.util.*;

// Problem: https://leetcode.com/problems/reverse-linked-list-ii/submissions/

class ListNode {
     int val;
     ListNode next;
     ListNode() {}
     ListNode(int val) { this.val = val; }
     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 }

public class ReverseLinkedList {
    public ListNode reverseBetween(ListNode head, int left, int right) {

        //Input:
        //l0, l1, l2, l3, l4, l5, l6, l7
        //Output:
        //l0, l1, l5, l4, l3, l2, l6, l7

        ListNode newHead = null;
        ListNode current = head;

        //until the left node, add elements to a stack
        //say left = 3
        //stkLeft -> l1, l0
        Stack<Integer> leftStack = new Stack<Integer>();
        int i = 0;
        for (; i < left - 1; i++) {
            //System.out.println("Lf | cur value:" + current.val);
            leftStack.push(current.val);
            current = current.next;
        }

        //from left to right, add elements to a queue
        Queue<Integer> queue = new LinkedList<Integer>();
        for (; i < right; i++) {
            //System.out.println("Rv | cur value:" + current.val);
            queue.offer(current.val);
            current = current.next;
        }

        //from right to end, add to head
        Stack<Integer> rightStack = new Stack<Integer>();
        while (current != null) {
            //System.out.println("Rt | cur value:" + current.val);
            rightStack.push(current.val);
            current = current.next;
        }

        while (!rightStack.isEmpty()) {
            //rightStack.pop();
            newHead = addToHead(newHead,  rightStack.pop());
        }

        //reversing the queue elements by adding to head
        // queue -> l2, l3, l4, l5
        while (!queue.isEmpty()) {
            //queue.poll();
            newHead = addToHead(newHead,  queue.poll());
        }

        while (!leftStack.isEmpty()) {
            //leftStack.pop();
            newHead = addToHead(newHead,  leftStack.pop());
        }
        return newHead;
    }

    public ListNode addToHead(ListNode head, int value) {
        if (head == null) {
            return new ListNode(value);
        } else {
            ListNode newHead = addToHead(null, value);
            newHead.next = head;
            return newHead;
        }
    }
}