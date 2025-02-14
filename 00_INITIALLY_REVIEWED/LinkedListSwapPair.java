// https://leetcode.com/problems/swap-nodes-in-pairs/
//
// the invariant is such that, Prev refers to the parent node of first
//

// init:
// P - > null (no parent node for F)
// F - >
//     S - >
//     1  ->  2 -> 3 -> 4 -> 5 ->
//

// swap stage 1 (next stages in 0th iteration is trivial):
// P - > null
// F - >
//       1 -->
//             3 -> 4 -> 5 ->
//       2 -->
// S - >
//

// node updates:
//        P - >
//              F - >
//                  S - >
//     2  ->  1 ->  3 -> 4 -> 5 ->
//

// swap stage 1:
// first.next = second.next
//      P - >
//            F - >
// -> 2 ->  1 ->  3 -->
//                       5 ->
//                4 -->
//            S - >
//

// swap stage 2:
// second.next = first
//      P - >
//           F - >
// -> 2 ->  1 ->  3 -> 5 ->
//           4 -->
//       S - >
//

// swap stage 3:
// if prev != null, prev.next = second
//      P - >
//               F - >
// -> 2 -> 1 -> 4 -> 3 -> 5 ->
//         S - >
//

class ListNodeS {
    int val;
    ListNodeS next;
    ListNodeS() {}
    ListNodeS(int val) { this.val = val; }
    ListNodeS(int val, ListNodeS next) { this.val = val; this.next = next; }

    @Override
    public String toString() {
        String toStr = " -> " + val;
        if (next != null) {
            toStr += next.toString();
        }
        return toStr;
    }
}

public class LinkedListSwapPair {

    public static void main(String[] args) {
        ListNodeS seven = new ListNodeS(7);
        ListNodeS six = new ListNodeS(6, seven);
        ListNodeS five = new ListNodeS(5, six);
        ListNodeS four = new ListNodeS(4, five);
        ListNodeS three = new ListNodeS(3, four);
        ListNodeS two = new ListNodeS(2, three);
        ListNodeS head = new ListNodeS(1, two);
        System.out.println("Initial linked list:" + head);

        ListNodeS swapped = swapPairs(head);
        System.out.println("Swapped linked list:" + swapped);
    }

    public static ListNodeS swapPairs(ListNodeS head) {
        if (head == null) {
            return null;
        }

        ListNodeS newHead = head.next == null ? head: head.next;

        ListNodeS prev = null; // no prev node point to first
        ListNodeS first = head;
        ListNodeS second = first.next;

        while (first != null && second != null) {
            // swap
            first.next = second.next;
            second.next = first;
            if (prev != null) {
                prev.next = second;
            }

            // updates for iteration
            prev = first;
            first = first.next;
            if (first != null) {
                second = first.next;
            }
        }
        return newHead;
    }
}