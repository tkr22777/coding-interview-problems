package com.company;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {

    short TARGET_VAL = 0;
    short CURRENT_VAL = 1;

    class State {

        Map<Character, int[]> charHistogram = new HashMap<>();

        int foundCount = 0;
    }

    //final State state = new State(); //If one wants to reduce memory usage

    public String minWindow(String s, String pattern) {

        State state = new State();

        build(state, pattern);

        String minStr = "";

        int i = 0, j = 0;
        boolean addedSufficientJ = false;

        while (j < s.length()) {

            //Keep adding char at j until sufficient
            //Two conditions, one fits success another overflow
            while (!addedSufficientJ && j < s.length()) {
                addedSufficientJ = addChar(state, s.charAt(j));
                if (addedSufficientJ) {
                    minStr = getString(minStr, s, i, j);
                } else {
                    j++;
                }
            }

            //Remove from left until it becomes insufficient
            //Two conditions, one fits success another overflow
            boolean removeI = true;
            while (removeI && addedSufficientJ && i <= j) {
                removeI = removeChar(state, s.charAt(i));
                i++;
            }

            if (!removeI && addedSufficientJ) {
                minStr = getString(minStr, s, i - 1, j);
            }

            addedSufficientJ = false;
            j++;
        }

        print(minStr);
        return minStr;
    }

    private String getString(String currentString, String s, int i, int j) {

        if ( currentString.equals("") || currentString.length() > j + 1 - i ) {
            return s.substring(i, j + 1);
        } else {
            return currentString;
        }
    }


    private boolean addChar(State s, char c) {

        if (s.charHistogram.containsKey(c)){
            int[] array = s.charHistogram.get(c);
            array[CURRENT_VAL]++;
            if (array[CURRENT_VAL] == array[TARGET_VAL]) {
                s.foundCount++;
            }
        }

        return s.foundCount == s.charHistogram.size();
    }

    private boolean removeChar(State s, char c) {

        if (s.charHistogram.containsKey(c)) {
            int[] array = s.charHistogram.get(c);
            array[CURRENT_VAL]--;
            if (array[CURRENT_VAL] < array[TARGET_VAL]) {
                s.foundCount--;
            }
        }

        return s.foundCount == s.charHistogram.size();
    }

    private void build(State s, String t) {

        Map<Character, int[]> table = s.charHistogram;

        for (int i = 0; i < t.length(); i++) {

            int[] array;

            if (!table.containsKey(t.charAt(i))) {
                array = new int[2];
                array[TARGET_VAL] = 1;
                array[CURRENT_VAL] = 0;
                table.put(t.charAt(i), array);
            } else  {
                array = table.get(t.charAt(i));
                array[TARGET_VAL]++;
            }
        }
    }

    public String minWindow2(String s, String pattern) {

        State state = new State();

        build(state, pattern);

        String minStr = "";

        boolean addJ = true;

        for (int i = 0, j = 0; i < s.length() && j < s.length(); ) {

            if (addJ) { //need to move right

                boolean completeAfterAdd = addChar(state, s.charAt(j));
                if (completeAfterAdd) {
                    if (minStr.equalsIgnoreCase("") || (minStr.length() > j + 1 - i)) {
                        minStr = s.substring(i, j + 1);
                    }
                    addJ = false;
                } else {
                    j++;
                }

            } else {

                //whenever we are in this block, the current i to j is a valid combination
                if (minStr.equalsIgnoreCase("") || (minStr.length() > j + 1 - i)) {
                    minStr = s.substring(i, j + 1);
                }

                boolean completeAfterRemove = removeChar(state, s.charAt(i));
                if (!completeAfterRemove) {
                    addJ = true;
                    j++;
                }
                i++;
            }

        }

        return minStr;
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


