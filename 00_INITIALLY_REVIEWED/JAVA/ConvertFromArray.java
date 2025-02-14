package JAVA;

import java.util.*;
import java.util.stream.*;

/* 
 * Takeaways, use Arrays.stream(arr) to create a stream.
 * If the type of elements in the array is a primitive, use boxed()
 */

public class ConvertFromArray {

    public static void main(String[] args) {
        new ConvertFromArray().testArrays();
    }

    public void testArrays() {
        int[] vals = {5, 1, 2, 3, 5, 3};
        StringJoiner sjAr = new StringJoiner(", ", "Initial Array: ", ".");
        Arrays.stream(vals).forEach(v -> sjAr.add(Integer.toString(v)));
        System.out.println(sjAr);

        StringJoiner sjNAr = new StringJoiner(", ", "To new Array: ", ".");
        Integer[] newArray = Stream.of(1, 2, 4, 7, 11, 17).toArray(Integer[]::new);
        Arrays.stream(newArray).forEach(v -> sjNAr.add(Integer.toString(v)));
        System.out.println(sjNAr);

        StringJoiner sjList = new StringJoiner(", ", "List collected from stream boxed array: ", ".");
        List<Integer> integerList = Arrays.stream(vals).boxed().collect(Collectors.toList());
        integerList.forEach(v -> sjList.add(Integer.toString(v)));
        System.out.println(sjList);
            
        StringJoiner sjArList = new StringJoiner(", ", "ArrayList created from array stream: ", ".");
        ArrayList<Integer> integerArList = new ArrayList<Integer>();
        Arrays.stream(vals).forEach(v -> integerArList.add(v));
        integerArList.forEach(v -> sjArList.add(Integer.toString(v)));
        System.out.println(sjArList);

        StringJoiner sjSet = new StringJoiner(", ", "Set collected from stream boxed array: ", ".");
        Set<Integer> integerSet = Arrays.stream(vals).boxed().collect(Collectors.toSet());
        integerSet.forEach(v -> sjSet.add(Integer.toString(v)));
        System.out.println(sjSet);
            
        StringJoiner sjHSet = new StringJoiner(", ", "LinkedHashSet collected from stream boxed array: ", ".");
        LinkedHashSet<Integer> integerLHSet = new LinkedHashSet<>();
        Arrays.stream(vals).forEach(v -> integerLHSet.add(v));
        integerLHSet.forEach(v -> sjHSet.add(Integer.toString(v)));
        System.out.println(sjHSet);

        StringJoiner sjMap = new StringJoiner(", ", "Map collected from stream boxed array: ", ".");
        Map<Integer, Integer> intSquareMap = Arrays.stream(vals).boxed().distinct()
            .collect(Collectors.toMap(
                a -> a,
                a -> a * a
            ));
        intSquareMap.entrySet().stream()
            .forEach(es -> sjMap.add("{Key: " + es.getKey() + " Value: " + es.getValue() + "}"));
        System.out.println(sjMap);

        StringJoiner sjLHMap = new StringJoiner(", ", "LinkedHashMap collected from stream boxed array: ", ".");
        LinkedHashMap<Integer, Integer> intSquareLHMap = new LinkedHashMap<Integer, Integer>();
        Arrays.stream(vals).boxed().forEach(v -> intSquareLHMap.put(v, v * v));
        intSquareLHMap.entrySet().stream()
            .forEach(es -> sjLHMap.add("{Key: " + es.getKey() + " Value: " + es.getValue() + "}"));
        System.out.println(sjLHMap);

        StringJoiner sjHistMap = new StringJoiner(", ", "Histogram created from stream boxed array: ", ".");
        HashMap<Integer, Integer> intHistMap = new HashMap<Integer, Integer>();
        Arrays.stream(vals).boxed().forEach(v -> intHistMap.put(v, intHistMap.getOrDefault(v, 0) + 1));
        intHistMap.entrySet().stream()
            .forEach(es -> sjHistMap.add("{Key: " + es.getKey() + " Value: " + es.getValue() + "}"));
        System.out.println(sjHistMap);

    }
}
