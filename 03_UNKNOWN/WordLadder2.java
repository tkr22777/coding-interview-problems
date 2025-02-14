package com.company;

import java.util.*;
import java.util.stream.Collectors;

class Solution {


    public static void main(String[] args) {

        String[] wordList = {"hot","dot","dog","lot","log","cog"};
        new Solution().findLadders("hit", "cog", Arrays.asList(wordList));

        String[] wordList2 =
                {"si",
                "go",
                "se",
                "cm",
                "so",
                "ph",
                "mt",
                "db",
                "mb",
                "sb",
                "kr",
                "ln",
                "tm",
                "le",
                "av",
                "sm",
                "ar",
                "ci",
                "ca",
                "br",
                "ti",
                "ba",
                "to",
                "ra",
                "fa",
                "yo",
                "ow",
                "sn",
                "ya",
                "cr",
                "po",
                "fe",
                "ho",
                "ma",
                "re",
                "or",
                "rn",
                "au",
                "ur",
                "rh",
                "sr",
                "tc",
                "lt",
                "lo",
                "as",
                "fr",
                "nb",
                "yb",
                "if",
                "pb",
                "ge",
                "th",
                "pm",
                "rb",
                "sh",
                "co",
                "ga",
                "li",
                "ha",
                "hz",
                "no",
                "bi",
                "di",
                "hi",
                "qa",
                "pi",
                "os",
                "uh",
                "wm",
                "an",
                "me",
                "mo",
                "na",
                "la",
                "st",
                "er",
                "sc",
                "ne",
                "mn",
                "mi",
                "am",
                "ex",
                "pt",
                "io",
                "be",
                "fm",
                "ta",
                "tb",
                "ni",
                "mr",
                "pa",
                "he",
                "lr",
                "sq",
                "ye"};
        new Solution().findLadders("qa", "sq", Arrays.asList(wordList2));
    }

    public List<List<String>> findLadders2(String beginWord, String endWord, List<String> wordList) {

        HashSet<String> words = new HashSet<>();
        HashSet<String> used = new HashSet<>();
        Queue<LinkedList<String>> q = new LinkedList<>();
        List<List<String>> result = new ArrayList<>();
        boolean found = false;

        for(String word:wordList) words.add(word);

        LinkedList<String> first = new LinkedList<>();
        first.add(beginWord);
        q.offer(first);
        used.add(beginWord);

        while(!q.isEmpty()){

            int size = q.size();
            System.out.println("Size : " + size);

            HashSet<String> localUsed = new HashSet<>();

            while(size>0){

                LinkedList<String> curr = q.poll(); //getting a candidate result up to the word
                char[] word = curr.getLast().toCharArray();  //the word up to we have searched

                for(int i=0;i<word.length;i++){ //for all indexes
                    char temp = word[i];
                    for(int j='a';j<='z';j++){ //for each index for all chars
                        word[i]=(char) j;
                        String s = String.valueOf(word); //a single char variation of the word
                        if(!used.contains(s) && words.contains(s)){ //if not already used and is in dictionary, move forward
                            LinkedList<String> list = new LinkedList<>(curr); //making new list
                            list.add(s); //adding the word variation
                            if(s.equals(endWord)){ //since found, we can add it to results
                                found=true;
                                result.add(list);
                                continue; //and try the next combos
                            }
                            localUsed.add(s); //not the end
                            q.offer(list); //adding to the queue, you may consider the queue as a candidate
                        }
                    }
                    word[i]=temp; //resetting word to alter another char
                }
                size--; // this will break after the first two
            }
            for(String s:localUsed) used.add(s); //updating the used.

            if(found) break;
        }

        return result;
    }

    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {

        List<List<String>> solution = new ArrayList<>();

        if (beginWord.length() != endWord.length()) {
            return solution;
        }

        if (!wordList.contains(endWord)) {
            return solution;
        }

        wordList = wordList.stream().filter( t -> t.length() == beginWord.length()).collect(Collectors.toList());

        Map<String, Set<String>> adjacencyMap = new HashMap<>();

        adjacencyMap.put(beginWord, findNeighbours(beginWord, wordList));

        for (String word: wordList) {
            adjacencyMap.put(word, findNeighbours(word, wordList));
        }

        solution = findInNeighbours(beginWord, endWord, adjacencyMap, new HashSet<>(), 0);

        if (solution == null) {
            return new ArrayList<>();
        }

        for (List<String> path: solution) {
            path.add(0, beginWord);
        }

        int minSolutionLength;
        if (solution.size() > 0) {
            minSolutionLength = solution.get(0).size();
            for (int i = 1 ; i < solution.size(); i++) {
                minSolutionLength = Math.min(minSolutionLength, solution.get(i).size());
            }
            final int minLength = minSolutionLength;
            solution = solution.stream().filter(s -> s.size() == minLength).collect(Collectors.toList());

        }

        print(solution);
        return solution;
    }

    private Set<String> findNeighbours(String givenString, List<String> wordList) {

        Set<String> toReturn = new HashSet<>();

        for (String str: wordList) {

            if (givenString.length() != str.length()) {
                continue;
            }

            if (givenString.equals(str)) {
                continue;
            }

            int charmissmatch = 0;
            for (int i = 0 ; i < str.length(); i++) {
                if (str.charAt(i) == givenString.charAt(i)) {
                    continue;
                }
                charmissmatch++;
            }

            if (charmissmatch == 1) {
                toReturn.add(str);
            }
        }
        return toReturn;
    }

    private List<List<String>> findInNeighbours(String beginWord,
                                                String endWord,
                                                Map<String, Set<String>> stringSetMap,
                                                Set<String> visited,
                                                int depth) {

        List<List<String>> toReturn = new ArrayList<>();

        Set<String> neighs = new HashSet<>(stringSetMap.get(beginWord);
        neighs.removeAll(visited);

        if (neighs.size() == 0) {
            return null;
        }

        if (neighs.contains(endWord)) {
            List<String> baseCase = new ArrayList<>();
            baseCase.add(endWord);
            toReturn.add(baseCase);
            return toReturn;
        }

        Set<String> currentVisited = new HashSet<>(visited);
        currentVisited.addAll(neighs);
        currentVisited.add(beginWord);

        for (String neigh: neighs) {

            List<List<String>> returnPaths = findInNeighbours(neigh, endWord, stringSetMap, currentVisited, depth + 1);

            if (returnPaths == null) {
                continue;
            }

            for (List<String> path: returnPaths) {
                path.add(0, neigh);
            }
            toReturn.addAll(returnPaths);
        }

        if (toReturn.size() > 0) {
            return toReturn;
        } else {
            return null;
        }
    }
}
