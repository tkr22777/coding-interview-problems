import java.util.*;

class DoublyListNode {
    int key;
    int value;
    DoublyListNode prev;
    DoublyListNode next;

    public DoublyListNode(int key, int value) {
        this.key = key;
        this.value = value;
    }
}

/* Could this be implemented using built in linkedList/arrayList? */
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

    int capacity = 0;
    Map<Integer, DoublyListNode> keyToNodeMap;
    DoublyListNode head = null; //keeps most recently used on head
    DoublyListNode tail = null; //keeps least recently used on tail

    public LRUCache(int capacity) {
        this.capacity = capacity;
        keyToNodeMap = new HashMap<>(capacity);
    }

    public int get(int key) {
        if (keyToNodeMap.containsKey(key)) {
            DoublyListNode node = keyToNodeMap.get(key);
            moveToHead(node);
            return node.value;
        }
        return -1;
    }

    public void put(int key, int value) {
        if (keyToNodeMap.containsKey(key)) {
            DoublyListNode node = keyToNodeMap.get(key);
            node.value = value;
            moveToHead(node);
            return;
        }

        //making a space by evicting the last element
        if (keyToNodeMap.size() == capacity) {
            removeTail();
        }

        DoublyListNode node = new DoublyListNode(key, value);
        keyToNodeMap.put(key, node);
        addToHead(node);
    }

    private void addToHead(DoublyListNode node) {
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

        node.next = head; // node.next next-> node at head
        head.prev = node; //  node <-prev node at head
        head = node; // head -> node
        node.prev = null; // null <-p node
    }

    private void moveToHead(DoublyListNode node) {
        if (node == head) {
            return;
        }

        node.prev.next = node.next; //circuit prev with next

        if (node == tail) {
            tail = node.prev; //if node is at the tail, tail should point to node.prev
        } else { 
            node.next.prev = node.prev; //or circuit next with prev
        }

        node.next = null;
        node.prev = null;
        addToHead(node);
    }

    /* Remove the last element from the list and also from the map */
    private void removeTail() {
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
        DoublyListNode node = head;
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
