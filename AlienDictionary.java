import java.util.*;

class AlienDictionary {

    public static void main(String[] args) {

        String[] words = { "wrt","wrf","er","ett","rftt" };

        System.out.println(new AlienDictionary().alienOrder(words));
    }

    public String alienOrder(String[] words) {
        
        Map<Character, Set<Character>> adjMat = convertToAdjMat(words);
        Set<Character> visited = new HashSet<>();
        List<Character> ordered = new ArrayList<>();
        
        for (char node: adjMat.keySet()) {
            if( dfs(node, adjMat, visited, new HashSet<>(), ordered) == -1 ) {
                return "";
            };
        }

        return toOutString(ordered);
    }
    
    public String toOutString( List<Character> ordered ) {
        Collections.reverse(ordered);
        StringBuilder sb = new StringBuilder();
        for (Character aChar: ordered) {
            sb.append(aChar);
        }
        return sb.toString();
    }
    
    public int dfs(Character cur,
                   Map<Character, Set<Character>> adjMat,
                   Set<Character> visited,
                   Set<Character> inDFSStack,
                   List<Character> ordered) {
        
        if (visited.contains(cur)) return 0;
        if (inDFSStack.contains(cur)) return -1;  
       
        inDFSStack.add(cur);
        
        Set<Character> children = adjMat.getOrDefault(cur, new HashSet<>());
        for(Character child: children) {
            if (dfs(child, adjMat, visited, inDFSStack, ordered) == -1) {
                return -1;
            }
        }
        
        inDFSStack.remove(cur);
        visited.add(cur);
        ordered.add(cur);
        return 0;
    }
    
    public Map<Character, Set<Character>> convertToAdjMat(String[] words) {
                
        Map<Character, Set<Character>> adjMat = new HashMap<>();
        
        for (int i = 1; i < words.length; i++) {
            
            String prevWord = words[i - 1];
            String currWord = words[i];
            int checkIndex = Math.min(prevWord.length(), currWord.length());
            
            for (int j = 0; j < checkIndex; j++) {
                
                if (prevWord.charAt(j) != currWord.charAt(j)) {
                    Set<Character> charSet = adjMat.getOrDefault(prevWord.charAt(j), new HashSet<>());
                    adjMat.put(prevWord.charAt(j), charSet);
                    charSet.add(currWord.charAt(j));
                    break;
                }
            }
        }
        
        /*
        for (Character aChar: adjMat.keySet()) {
            Set<Character> charSet = adjMat.get(aChar);
            System.out.println( String.format("Char: %s to Set:%s", aChar, charSet.toString()));
        }
        */
        
        return adjMat;
    }
}

