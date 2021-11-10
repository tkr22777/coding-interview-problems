/* https://leetcode.com/problems/repeated-dna-sequences */
package TOClean;
import java.util.*;

class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        Set<String> strings = new HashSet<>();
        Set<String> toReturn = new HashSet<>();

        int d = 10;
        if (s.length() < d + 1) {
            return new ArrayList<>();
        }

        for (int i = 0; i <= s.length() - d; i++) {
            String sub = s.substring(i, i + d);

            if (strings.contains(sub)) {
                toReturn.add(sub);
            } else {
                strings.add(sub);
            }
        }
        return new ArrayList<>(toReturn);
    }
}
