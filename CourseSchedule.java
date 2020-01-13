import java.util.*;

class CourseSchedule {

    //https://leetcode.com/problems/course-schedule/submissions/

    public static void main(String[] args) {
        System.out.println("Compiling");
    }

    public boolean canFinish(int numCourses, int[][] prerequisites) {

        boolean[] visited = new boolean[numCourses];
        boolean[] callStack = new boolean[numCourses];

        //build the graph
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] edge: prerequisites) {
            /* {a, b} <- to take course a, you need to take course b first */
            graph.computeIfAbsent(edge[1], v -> new LinkedList<Integer>())
                .add(edge[0]);
        }

        for (Integer node: graph.keySet()) {
            /* course schedule would be impossible if there is a cycle */
            if (containsCycleDFS(node, graph, callStack, visited)) {
                return false;
            }
        }
        return true;
    }

    public boolean containsCycleDFS(Integer node,
                                    Map<Integer, List<Integer>> graph,
                                    boolean[] callStack,
                                    boolean[] visited) {

        if (callStack[node]) return true;
        callStack[node] = true;

        if (visited[node]) return false;
        visited[node] = true;

        List<Integer> adjacents = graph.getOrDefault(node, new LinkedList<>());
        for (Integer adj: adjacents) {
            if (containsCycleDFS(adj, graph, visited, callStack)) {
                return true;
            }
        }
        callStack[node] = false;
        return false;
    }
}

