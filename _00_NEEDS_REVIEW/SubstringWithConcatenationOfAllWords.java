package com.company;

import java.util.*;

class Solution {

    public List<Integer> findSubstring(String s, String[] words) {

        List<Integer> solution = new ArrayList<>();

        if (words.length == 0) {
            return solution;
        }

        int wordLen = words[0].length();

        Map<String, Integer> wordsMapping = new HashMap<>();

        for(int i = 0; i < words.length; i++) {
            if (wordsMapping.containsKey(words[i])) {
                wordsMapping.put(words[i], wordsMapping.get(words[i]) + 1); //word to index map
            } else {
                wordsMapping.put(words[i],1);
            }
        }

        final Map<Character,Integer> charsMap = new HashMap<>();
        for(int i = 0; i < words.length; i++) {
            for(int j=0; j < words[i].length(); j++) {
                Character charAtJ = words[i].charAt(j);
                if (charsMap.containsKey(charAtJ)) {
                    charsMap.put(charAtJ, charsMap.get(charAtJ) + 1);
                } else {
                    charsMap.put(charAtJ, 1);
                }
            }
        }

        //print(wordsMapping);
        //print(charsMap);
        //print("Char Map Size:" + charsMap.size() + " string size:" + s.length() + " words len" + wordLen + " total words:" + words.length);

        Map<Character,Integer> windowMap = new HashMap<>();
        int charCompleteCount = 0;

        for(int i = 0; i < s.length(); i++) {

            /*
            if (i%100 == 0) {
                //print("i: " + i + " char complete count:" + charCompleteCount + " window map :");
                //print(windowMap);
            }
             */

            if (i >= wordLen * words.length) {

                int j = i - wordLen * words.length; //to remove

                if (charsMap.containsKey(s.charAt(j))) {
                    windowMap.put(s.charAt(j), windowMap.get(s.charAt(j)) - 1);
                    if (windowMap.get(s.charAt(j)).intValue() == charsMap.get(s.charAt(j)).intValue() - 1) {
                        charCompleteCount--;
                    }
                }
            }

            if (!charsMap.containsKey(s.charAt(i))) {
                continue;
            }

            if (windowMap.containsKey(s.charAt(i))) {
                windowMap.put(s.charAt(i), windowMap.get(s.charAt(i)) + 1);
            } else {
                windowMap.put(s.charAt(i), 1);
            }

            //print("i: " + i + " char: " + s.charAt(i) + " char complete count:" + charCompleteCount + " chars count:" + charsMap.get(s.charAt(i)) + " window count:" + windowMap.get(s.charAt(i)));

            if (windowMap.get(s.charAt(i)).intValue() == charsMap.get(s.charAt(i)).intValue()) {
                charCompleteCount++;
            }

            if (charCompleteCount == charsMap.size()) {
                Map<String,Integer> windowWordsMapping = new HashMap<>();
                int start = i - words.length * wordLen + 1;
                int wordCounter = 0;
                while (start <= i) {
                    //print(windowWordsMapping);
                    String key = s.substring(start, start + wordLen);
                    if (!wordsMapping.containsKey(key)) {
                        break;
                    }
                    windowWordsMapping.computeIfAbsent(key, t -> 0);
                    windowWordsMapping.put(key, windowWordsMapping.get(key) + 1);
                    if (windowWordsMapping.get(key) == wordsMapping.get(key)) {
                        wordCounter++;
                    }
                    start += wordLen;
                }

                if (wordCounter == wordsMapping.size()) {
                    solution.add(i - words.length * wordLen + 1);
                }
            }
        }

        //print(solution);
        return solution;
    }

    public List<Integer> findSubstringB(String s, String[] words) {

        List<Integer> solution = new ArrayList<>();

        if (words.length == 0) {
            return solution;
        }

        int wordLen = words[0].length();

        //assume words.len = 2 and wordLen = 2 and string len is 6.
        //Then string expands from 0 to 5 and we would need to check 0 to 3, 1 to 4, 2 to 5 for 4 char based
        //Size of the checking array should have len of 3
        //Thus the formula should be str.len - wordLen + 1
        List<Integer>[] found = new List[s.length() - wordLen + 1];

        for (int i = 0 ; i < found.length; i++) {
            found[i] = new ArrayList();
            for (int j = 0; j < words.length; j++) {
                String subString = s.substring(i, i + wordLen);
                if (subString.equals(words[j])) {
                    found[i].add(j);
                }
            }
        }

        for (int i = 0; i < s.length() - (wordLen * words.length) + 1; i++) {
            if (found[i].size() > 0) {
                Set<Set<Integer>> indexSets = new HashSet<>();
                for (int j = i; j < i + wordLen * words.length ; j += wordLen) {

                    if (found[j] == null) {
                        break;
                    }

                    if (indexSets.size() == 0) {
                        indexSets.add(new HashSet<>());
                    }

                    if (found[j].size() < 2) {
                        for(Set<Integer> set: indexSets) {
                            set.addAll(found[j]);
                        }
                    } else {
                        Set<Set<Integer>> newIndexSets = new HashSet<>();
                        for (Integer index: found[j]) {
                            for (Set<Integer> indexSet: indexSets) {
                                Set<Integer> copiedIndexSet = new HashSet<>();
                                for (int indexVal: indexSet){
                                    copiedIndexSet.add(indexVal);
                                }
                                copiedIndexSet.add(index);
                                newIndexSets.add(copiedIndexSet);
                            }
                        }
                        indexSets = newIndexSets;
                    }
                }
                for (Set<Integer> integerSet: indexSets) {
                    if (integerSet.size() == words.length) {
                        solution.add(i);
                    }
                }
            }
        }

        return solution;
    }

    private void print(Object x) {
        System.out.println(x.toString());
    }

    private void print(Object[] array) {
        System.out.println(Arrays.toString(array));
    }

    private void print(Object[][] array2d) {

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

    private void print(Map map) {

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

