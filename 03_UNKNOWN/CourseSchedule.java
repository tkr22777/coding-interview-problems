class Solution {

    //https://leetcode.com/problems/course-schedule/submissions/

    public boolean canFinish(int numCourses, int[][] prerequisites) {

        boolean[] visited = new boolean[numCourses];
        boolean[] callStack = new boolean[numCourses];

        //build the graph
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] edge: prerequisites) {
            graph.computeIfAbsent(edge[1], v -> new LinkedList<Integer>()).add(edge[0]);
        }

        for (Integer node: graph.keySet()) {
            if (containsCycleDFS(node, graph, visited, callStack)) {
                return false;
            }
        }

        return true;
    }

    public boolean containsCycleDFS(Integer node,
                                    Map<Integer, List<Integer>> graph,
                                    boolean[] visited,
                                    boolean[] callStack) {

        if (callStack[node]) {
            return true;
        }

        if (visited[node]) {
            return false;
        }

        visited[node] = true;
        callStack[node] = true;
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

