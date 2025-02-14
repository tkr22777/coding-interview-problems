import java.lang.reflect.Array;
import java.util.*;
import java.util.stream.*;

public class InitJava {

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
        // write your code here
        new InitJava().testQueue();
        new InitJava().testStack();
        new InitJava().testLinkedHashSet();
        new InitJava().testLinkedHashMap();
        new InitJava().testLog();
        new InitJava().testBitwise();
        new InitJava().bitMaskTest();
        //stringToCharFreq("hey waddup thangaa?");
        //testStreamToMap();
        //onelineInitializers();
    }


    public void testQueue() {

        System.out.println("Test Queue:");
        Queue<String> queue = new LinkedList<>();
        queue.offer("First");
        queue.offer("Second");
        queue.offer("Third");
        queue.offer("Four");

        System.out.println("Size of queue: " + queue.size());
        while(!queue.isEmpty()) {
            System.out.println(queue.peek());
            System.out.println(queue.remove());
        }
        System.out.println();
    }

    public void testStack() {

        System.out.println("Test Stack:");
        Stack<String> stack = new Stack<>();
        stack.push("A");
        stack.push("S");
        stack.push("D");
        stack.push("F");

        System.out.println("Size of stack: " + stack.size());
        while (!stack.empty()) {
            System.out.println(stack.peek());
            System.out.println(stack.pop());
        }
    }

    public void testLinkedHashSet() {
        System.out.println("\nTest Linked Hashset");
        List<Integer> aList = Arrays.asList(18, 14, 27, 33);
        StringJoiner sjList = new StringJoiner(", ", "Input List: ", ".");
        aList.stream().forEach(elem -> sjList.add(Integer.toString(elem)));
        System.out.println(sjList.toString());

        HashSet<Integer> hashSet = new HashSet<>(aList);
        StringJoiner sjHs = new StringJoiner(", ", "HashSet stream forEach: ", ".");
        hashSet.stream().forEach(elem -> sjHs.add(Integer.toString(elem)));
        System.out.println(sjHs.toString());

        LinkedHashSet<Integer> lhSet = new LinkedHashSet<>(aList);
        StringJoiner sjLHS = new StringJoiner(", ", "LinkedHashSet stream forEach: ", ".");
        lhSet.stream().forEach(elem -> sjLHS.add(Integer.toString(elem)));
        System.out.println(sjLHS.toString());
    }


    public void onelineInitializers() {

        Set<Integer> setA = new HashSet<>(Arrays.asList(1, 2 , 3, 4, 4, 2, 7));
        Set<Integer> setB = Stream.of(3, 4, 5, 9, 11, 4).collect(Collectors.toSet());

        Map<Character, Integer> charToInt = Stream.of('a', 'b', 'c', 'd', 'e').collect(Collectors.toMap(
                    a -> a,
                    a -> (int) a
                    ));

        Map<Character, Integer> allCharToInt = Stream.iterate('a', i -> (char)(i + 1))
            .limit(26)
            .collect(Collectors.toMap(
                        a -> a,
                        a -> (int) a
                        ));
    }

    public void testStreamToMap() {
        int[][] coOrds = {
            {1, 2},
            {2, 4},
            {3, 6},
            {4, 8},
            {5, 10},
            {6, 12},
            {7, 14},
            {8, 16}
        };

        Map<Integer, int[]> xToCoOrds = Arrays.stream(coOrds).collect(Collectors.toMap(
                    a -> a[0],
                    a -> a
                    ));

        xToCoOrds.values().stream().forEach(a -> {
            System.out.println(a[0]);
            System.out.println(Arrays.toString(a));
        });
    }

    public void testArrayListToSet() {
        int[] vals = {5, 1, 2, 3, 5, 3, 1, 2};
        List<Integer> integerList = Arrays.stream(vals).boxed().collect(Collectors.toList());
        Set<Integer> integerSet = integerList.stream().collect(Collectors.toSet());
    }


    public void stringToCharFreq(String input) {
        Map<Character, Integer> freqMap = new HashMap<>();
        for(Character c: input.toCharArray()) {
            freqMap.put(c, freqMap.getOrDefault(c, 0) + 1);
        }
    }

    public void bitMaskTest() {
        System.out.println(Integer.toHexString(0xABCD & 0xF000).toUpperCase());
        System.out.println(Integer.toHexString(0xABCD & 0xF00).toUpperCase());
        System.out.println(Integer.toHexString(0xABCD & 0xF0 ).toUpperCase());
        System.out.println(Integer.toHexString(0xABCD & 0xF).toUpperCase());
    }

    public void testBitwise() {

        System.out.println("bin 101 right shift once:" + Integer.toBinaryString(0b101 >> 1)); // makes 5 -> 2, 5 / 2 ** 1
        System.out.println("bin 101 right shift twice:" + Integer.toBinaryString((0b101 >> 2))); // makes 5 -> 1, 5 / 2 **  2
        System.out.println("bin 101 right shift thrice:" + (0b101 >> 3)); // makes 5 -> 0, 5 / 2 ** 3

        System.out.println("bin 101 left shift once:" + (0b101 << 1)); // makes 5 -> 10, 5 * 2 ** 1
        System.out.println("bin 101 left shift twice:" + (0b101 << 2)); // makes 5 -> 20, 5 * 2 ** 2
        System.out.println("bin 101 left shift thrice:" + (0b101 << 3)); // makes 5 -> 40, 5 * 2 ** 3

        System.out.println(Integer.toBinaryString(0b100));
        System.out.println(Integer.toBinaryString(0b101));
        System.out.println(Integer.toBinaryString(0b110));

        System.out.println(Integer.toBinaryString(0b100) + ", inverted:" + Integer.toBinaryString(~0b100));
        System.out.println(0b100 + " bitwise inverted value:" + ~0b100); // 4 -> -5
        System.out.println(Integer.toBinaryString(0b100) + " & " + Integer.toBinaryString(0b101) + "->"
                + Integer.toBinaryString(0b100 & 0b101)); // should print 100
        System.out.println(Integer.toBinaryString(0b100) + " | " + Integer.toBinaryString(0b101) + "->"
                + Integer.toBinaryString(0b100 | 0b101)); // should print 101
        System.out.println(Integer.toBinaryString(0b100) + " ^ " + Integer.toBinaryString(0b101) + "->"
                + Integer.toBinaryString(0b100 ^ 0b101)); //should print 001

        System.out.println("bin 101 triple right shift once:" + (0b101 >>> 3)); // makes 5 -> 2, 5 / 2 ** 1
        System.out.println("bin 101 triple right shift once:" + ((-1 * 0b101) >>> 3)); // makes 5 -> 2, 5 / 2 ** 1

        int hexAB = 0xAB;
        int hexAA = 0xAA;

        double d1 = 123.4;
        double d1Sci = 1.234e2;

        float f1 = 123.4f;
        float f1Sci = 123.4e2f;
    }

    public void testLog() {
        int num = 100002;
        double y = Math.log10(num);
        double yToTheTen = Math.pow(10, y);
        System.out.println("Log base 10 of " + num + " is " + y + " and y to the 10 is :" + yToTheTen);

        num = 9;
        y = Math.log10(num);
        yToTheTen = Math.pow(10, y);
        System.out.println("Log base 10 of " + num + " is " + y + " and y to the 10 is :" + yToTheTen);

        num = 81;
        y = Math.log10(num);
        yToTheTen = Math.pow(10, y);
        System.out.println("Log base 10 of " + num + " is " + y + " and y to the 10 is :" + yToTheTen);
    }

    public void testLinkedHashMap() {

        LinkedHashMap<Integer, String> linkedHashMap = new LinkedHashMap<>();
        linkedHashMap.put(4, "Four");
        linkedHashMap.put(1, "One");
        linkedHashMap.put(7, "Seven");
        linkedHashMap.put(-1, "NegOne");

        System.out.println("Size of linkedHashMap:" + linkedHashMap.size());
        for (int key: linkedHashMap.keySet()) {
            System.out.println("Key:" + key + " Val:" + linkedHashMap.get(key));
        }
    }

    private static void print(Object x) {
        System.out.println(x.toString());
    }

    private static void print(Object[] array) {
        System.out.println(Arrays.toString(array));
    }

    private static void print(Object[][] array2d) {

        if (array2d == null) {
            return;
        }

        for (int i = 0 ; i < array2d.length; i++) {

            if (array2d[i] == null) {
                continue;
            }

            print(array2d[i]);
        }
        System.out.println();
    }

    private static void print(Map map) {

        for (Object key: map.keySet()) {
            Object val = map.get(key);
            if (val instanceof int[]) {
                int[] array = (int[]) val;
                print("Key: " + key + " Value: " + Arrays.toString(array));
            } else {
                print("Key: " + key + " Value: " + val);
            }
        }
    }
}




