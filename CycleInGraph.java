import java.util.*;

public class CycleInGraph {

    public static void main(String[] args) {

        int[][] graph01 = { 
            {0, 1, 1, 0},
            {0, 0, 0, 1},
            {0, 1, 0, 0},
            {0, 0, 1, 0}
        };

        int[][] graph02 = { 
            {0, 1, 1, 0},
            {0, 0, 0, 1},
            {0, 0, 0, 0},
            {0, 0, 1, 0}
        };

        int[][] graph03 = { 
            {0, 1, 1, 0},
            {0, 0, 0, 1},
            {0, 0, 1, 0},
            {0, 0, 1, 0}
        };

        System.out.println("Graph01 contains cycle: " + containsCycle(graph01));
        System.out.println("Graph02 contains cycle: " + containsCycle(graph02));
        System.out.println("Graph03 contains cycle: " + containsCycle(graph03));
    }

    public static boolean containsCycle(int[][] graph) {

        for (int node = 0; node < graph.length; node++) {
            if (containsCycleDFS(graph, node, new HashSet<>())){
                return true;
            }
        }
        return false;
    }

    public static boolean containsCycleDFS(int[][] graph, int node, Set<Integer> dfsStack) {

        if (dfsStack.contains(node)) {
            return true;
        }

        dfsStack.add(node);

        for (int next = 0; next < graph[node].length; next++) {
            if (graph[node][next] == 1) {
                if(containsCycleDFS(graph, next, dfsStack)) {
                    return true;
                }
            }
        }

        dfsStack.remove(node);
        return false;
    }
}


