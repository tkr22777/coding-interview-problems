import java.util.*;

public class LRUCache {

    public static void main(String[] args) {

        LRUCache cache = new LRUCache(2);
        cache.put(1,1);
        cache.printList();

        cache.put(2,2);
        cache.printList();

        System.out.println(cache.get(1));
        cache.printList();

        cache.put(3,3);
        cache.printList();
        System.out.println(cache.get(2));
        cache.printList();
    }

    class ListNode {
        int key;
        int value;
        ListNode prev;
        ListNode next;

        public ListNode(int key, int value) {
            this.key = key;
            this.value = value;
        }
    }

    int capacity = 0;
    Map<Integer, ListNode> keyToNodeMap;
    ListNode head = null; //keeps most recently used on head
    ListNode tail = null; //keeps least recently used on tail

    public LRUCache(int capacity) {
        this.capacity = capacity;
        keyToNodeMap = new HashMap<>(capacity);
    }

    public int get(int key) {
        if (keyToNodeMap.containsKey(key)) {
            ListNode node = keyToNodeMap.get(key);
            makeMostRecent(node); 
            return node.value;
        } else {
            return -1;
        }
    }

    public void put(int key, int value) {

        if (keyToNodeMap.containsKey(key)) {
            ListNode node = keyToNodeMap.get(key);
            node.value = value;
            makeMostRecent(node);
            return;
        }

        //making a space by evicting the last element
        if (keyToNodeMap.size() == capacity) {
            removeLeastRecentlyUsed();
        }

        ListNode node = new ListNode(key, value);
        keyToNodeMap.put(key, node);
        addToHead(node);
    }

    private void addToHead(ListNode node) {

        if (node == null) {
            return;
        }

        if (head == null && tail == null) {
            head = node;
            tail = node;
            node.next = null;
            node.prev = null;
            return;
        }

        node.next = head;
        head.prev = node;
        head = node;
        node.prev = null;
    }

    private void makeMostRecent(ListNode node) {

        if (head == node) {
            return;
        } 

        if (tail == node) { 
            tail = node.prev; //if node is at the tail, tail should be node.prev
        } else { 
            node.next.prev = node.prev; //non-tail node's next.prev should be node prev
        }

        node.prev.next = node.next; //node's prev.next should be node next
        node.next = null;
        node.prev = null;

        addToHead(node);
    }

    /* Remove the last element from the list and also from the map */
    private void removeLeastRecentlyUsed() {
        if (head == null || tail == null) {
            return;
        }

        keyToNodeMap.remove(tail.key);

        //Single element
        if (tail.prev == null) {
            tail = null;
            head = null;
        } else {
            tail = tail.prev;
            tail.next.prev = null;
            tail.next = null;
        }
    }

    public void printList() {
        ListNode node = head;
        StringBuilder sb = new StringBuilder();
        sb.append( "From Head ->");
        while (node != null) {
            sb.append(node.key + " -> ");
            node = node.next;
        }
        sb.append("||");

        node = tail;
        sb.append( ", From Tail ->");
        while (node != null){
            sb.append(node.key + " -> ");
            node = node.prev;
        }
        sb.append("||");
        System.out.println(sb.toString());
    }
}
