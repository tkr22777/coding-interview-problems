import java.io.*;
import java.util.*;
import java.util.stream.*;

class Solution {

  public static void main(String[] args) {

    int[] numbers = {1,1,1,2,2,3};

    System.out.println(new Solution().topKFrequent(numbers, 2).toString());
  }

  public List<Integer> topKFrequent(int[] nums, int k) {

    Map<Integer, Integer> valFreq = new HashMap<Integer, Integer>();
    Arrays.stream(nums)
      .forEach( v -> {
        valFreq.put(v, valFreq.getOrDefault(v, 0) + 1);
      });


    Map<Integer, List<Integer>> freqToElems = new TreeMap<Integer, List<Integer>>();
      //((a,b) -> Integer.compare(b, a));

    valFreq.entrySet().stream()
      .forEach( entry -> {
        freqToElems.computeIfAbsent(entry.getValue(), v -> new LinkedList<Integer>())
          .add(entry.getKey());
      });

    return freqToElems.keySet().stream().limit(k).collect(Collectors.toList());
  }
}

