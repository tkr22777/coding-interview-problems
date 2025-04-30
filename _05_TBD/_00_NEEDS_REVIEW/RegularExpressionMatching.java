package TOClean;

//https://leetcode.com/problems/regular-expression-matching/

import java.util.*;

public class RegularExpressionMatching {

    public static void main(String[] args) {
        System.out.println(new RegularExpressionMatching().isMatch("aab", "c*a*b")); //true
        System.out.println(new RegularExpressionMatching().isMatch("mississippi", "mis*is*p*.")); //false
        System.out.println(new RegularExpressionMatching().isMatch("a", ".*..")); // false
        System.out.println(new RegularExpressionMatching().isMatch("aa", "a*")); // true
        //System.out.println(new RegularExpressionMatching().isMatchR("aab", "c*a*b"));
    }

    public boolean isMatch(String s, String p) {
        return isMatchIterative(s, p);
    }

    public boolean isMatchR(String s, String p) {
        return isMatchRecursive(s, 0, p, 0);
    }

    private boolean isMatchIterative(String s, String p) {
        Queue<List<Integer>> queue = new LinkedList<>();
        queue.offer(Arrays.asList(0, 0));
        Set<List<Integer>> visited = new HashSet<>();
        while (!queue.isEmpty()) {
            List<Integer> pointers = queue.poll();
            if (visited.contains(pointers)) {
                continue;
            } else {
                visited.add(pointers);
            }

            //System.out.println("Pointers: " + pointers.toString());
            int i = pointers.get(0);
            int j = pointers.get(1);
            while (i < s.length() && j < p.length()) {
                boolean hasStar = j + 1 < p.length() && p.charAt(j + 1) == '*';
                if (s.charAt(i) == p.charAt(j) || p.charAt(j) == '.') {
                    if (hasStar) {
                        queue.offer(Arrays.asList(i, j + 2));
                        i++;
                    } else {
                        i++;
                        j++;
                    }
                } else if (hasStar) {
                    j += 2;
                } else {
                    break;
                }
            }

            if (i == s.length()) {
                while (j + 1 < p.length() && p.charAt(j + 1) == '*') {
                    j += 2;
                }

                if (j == p.length()) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean isMatchRecursive(String s, int i, String p, int j) {
        if (i > s.length() || j > p.length()) {
            return false;
        }

        boolean hasStar = j + 1 < p.length() && p.charAt(j + 1) == '*';
        if (i == s.length()) {
            if (j == p.length()) {
                return true;
            } else if (hasStar) {
                return isMatchRecursive(s, i, p, j + 2);
            } else {
                return false;
            }
        }

        if (j == p.length()) {
            return false;
        }

        if (s.charAt(i) == p.charAt(j) || p.charAt(j) == '.') {
            if (hasStar) {
                return isMatchRecursive(s, i + 1, p, j) || isMatchRecursive(s, i, p, j + 2);
            } else {
                return isMatchRecursive(s, i + 1, p, j + 1);
            }
        } else if (hasStar) {
            return isMatchRecursive(s, i, p, j + 2);
        } else {
            return false;
        }
    }
}