/*
    https://leetcode.com/problems/course-schedule/submissions/
    You have to take, courses labeled from 0 to numCourses - 1.
    The prerequisites[i] = [ai, bi] implies bi must be taken before ai.
    Return true if you can finish all courses given the params.
*/

import java.util.*;

class CourseSchedule {
    public static void main(String[] args) {
        System.out.println("Compiling");
    }

    /* TODO add explanation */
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        //build the graph
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] edge: prerequisites) {
            /* {a, b} <- to take course a, you need to take course b first */
            graph.computeIfAbsent(edge[1], v -> new LinkedList<>())
                .add(edge[0]);
        }

        boolean[] visited = new boolean[numCourses];
        boolean[] dfsStack = new boolean[numCourses];
        for (Integer node: graph.keySet()) {
            /* course schedule would be impossible if there is a cyclic dependency */
            if (containsCycleDFS(node, graph, dfsStack, visited)) {
                return false;
            }
        }
        return true;
    }

    public boolean containsCycleDFS(Integer node,
                                    Map<Integer, List<Integer>> graph,
                                    boolean[] dfsStack,
                                    boolean[] visited) {
        if (dfsStack[node]) return true;
        dfsStack[node] = true;

        if (visited[node]) return false;
        visited[node] = true;

        List<Integer> adjacents = graph.getOrDefault(node, new LinkedList<>());
        for (Integer adj: adjacents) {
            if (containsCycleDFS(adj, graph, visited, dfsStack)) {
                return true;
            }
        }
        dfsStack[node] = false;
        return false;
    }
}

