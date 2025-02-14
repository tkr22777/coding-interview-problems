import java.util.*;
import java.util.stream.*;

public class TestPQ {

    static class CoOrd {
        int x;
        int y;

        public CoOrd(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public String toString() {
            return "{ x: " + this.x + " y: " + this.y + " }";
        }

        @Override
        public int hashCode() {
            return Objects.hash(this.x, this.y);
        }
    }

    public static void main(String[] args) {
        new TestPQ().testPriorityQueue();
        new TestPQ().testPriorityQueueObject();
        new TestPQ().testTreeMap();
        new TestPQ().testTreeSet();
    }

    /* Use while not empty for prority queue */
    public void testPriorityQueue() {

        System.out.println("\nTest Priority Queue:");

        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();
        Stream.of(1, 2, -1, 5, 3, 4, 5, -11, 6).forEach(a -> priorityQueue.add(a));

        StringJoiner sj1 = new StringJoiner(", ", "ForEach iteration on Integer PQ: ", ".");
        priorityQueue.stream().forEach(a -> sj1.add(a.toString()));
        System.out.println(sj1.toString());

        PriorityQueue<Character> charPriorityQueue = new PriorityQueue<>();
        Stream.of('a','m','f','n' ,'Z' ,'0','M','b','D','9').forEach(c -> charPriorityQueue.add(c));
        StringJoiner sj2 = new StringJoiner(", ", "ForEach iteration on Character PQ: ", ".");
        charPriorityQueue.stream().forEach(c -> sj2.add(c.toString()));
        System.out.println(sj2.toString());

        StringJoiner sj3 = new StringJoiner(", ", "While not empty poll on Character PQ: ", ".");
        while (!charPriorityQueue.isEmpty()) {
            char c = charPriorityQueue.poll().charValue();
            sj3.add(c + " -> " + (int) c);
        }
        System.out.println(sj3.toString());
    }

    public void testPriorityQueueObject() {

        CoOrd p1 = new CoOrd(2, 0);
        CoOrd p2a = new CoOrd(1, 1);
        CoOrd p2b = new CoOrd(1, 0);
        CoOrd p3 = new CoOrd(3, 0);

        Comparator<CoOrd> pointComparator = new Comparator<CoOrd>() {
            @Override
            public int compare(CoOrd o1, CoOrd o2) {
                int com = Integer.compare(o1.x, o2.x) ;
                return com != 0? com: Integer.compare(o1.y, o2.y);
            }
        };
        PriorityQueue<CoOrd> pQ = new PriorityQueue<>(pointComparator);

        pQ.offer(p1);
        pQ.offer(p2a);
        pQ.offer(p2b);
        pQ.offer(p3);

        System.out.println("Size of Priority Queue:" + pQ.size());

        while (!pQ.isEmpty()) {
            System.out.println(pQ.peek());
            System.out.println(pQ.poll());
        }
    }



    public void testTreeSet() {

        System.out.println("\nTest TreeSet:");

        List<CoOrd> coOrdList = Arrays.asList(new CoOrd(1, 0), new CoOrd(8, 0), new CoOrd(11, -100), new CoOrd(8, -1));
        final StringJoiner sj4 = new StringJoiner(", ", "Input CoOrdinates: " , ".");
        coOrdList.stream().forEach(c -> sj4.add(c.toString()));
        System.out.println(sj4.toString());

        Comparator<CoOrd> pointComparator = new Comparator<CoOrd>() {
            @Override
            public int compare(CoOrd o1, CoOrd o2) {
                int com = Integer.compare(o1.x, o2.x) ;
                return com != 0? com: Integer.compare(o1.y, o2.y);
            }
        };

        TreeSet<CoOrd> testTreeSet = new TreeSet<CoOrd>(pointComparator);
        coOrdList.stream().forEach(c -> testTreeSet.add(c));

        final StringJoiner sj = new StringJoiner(", ", "Stream TreeSet: ", ".");
        testTreeSet.stream().forEach(c -> sj.add(c.toString()));
        System.out.println(sj.toString());

        final StringJoiner sj2 = new StringJoiner(", ", "Poll First TreeSet: ", ".");
        while (!testTreeSet.isEmpty()) {
            sj2.add(testTreeSet.pollFirst().toString());
        }
        System.out.println(sj2.toString());

        coOrdList.stream().forEach(c -> testTreeSet.add(c));
        final StringJoiner sj3 = new StringJoiner(", ", "Poll Last TreeSet: ", ".");
        while (!testTreeSet.isEmpty()) {
            sj3.add(testTreeSet.pollLast().toString());
        }
        System.out.println(sj3.toString());
    }

    public void testTreeMap() {

        Map<Integer, Integer> intMap = Stream.iterate(0, i -> i + 1)
            .limit(10)
            .collect(Collectors.toMap(
                        a -> a,
                        a -> a * 2
                        ));

        List<CoOrd> coOrds = Stream.iterate(0, i -> i + 1)
            .limit(10)
            .map( i -> new CoOrd(i , i % 2 == 0? i : -1 * i))
            .collect(Collectors.toList());

        Comparator<CoOrd> comparator = (c1, c2) -> Integer.compare(c1.y, c2.y);
        Comparator<CoOrd> comparator1 = (c1, c2) -> {
            int comp = Integer.compare(c1.y, c2.y);
            if (comp != 0) {
                return comp;
            } else  {
                return Integer.compare(c1.x, c2.x);
            }
        };

        TreeSet<CoOrd> treeSet = new TreeSet<CoOrd>(comparator);
        treeSet.addAll(coOrds);
        CoOrd c1 = new CoOrd(77, -77);
        treeSet.add(c1);
        treeSet.remove(c1);
        c1.y = 77;
        treeSet.add(c1);
        treeSet.forEach(System.out::println);
    }


}



