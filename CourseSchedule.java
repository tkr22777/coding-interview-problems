/*
    https://leetcode.com/problems/course-schedule/submissions/
    You have to take, courses labeled from 0 to numCourses - 1.
    The prerequisites[i] = [ai, bi] implies bi must be taken before ai.
    Return true if you can finish all courses given the params.

    The idea for the solution:
    -> there are no time limitations
    -> we can take any course unless there is pre-req
    -> for pre-reqs we can take them and then move and take the next ones
    -> we will not be able to finish if there is a cyclic pre-reqs among courses
*/

import java.util.*;

class CourseSchedule {
    public static void main(String[] args) {
        System.out.println("Compiling");
    }

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        //build the graph
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int[] edge: prerequisites) {
            /* {a, b} <- to take course a, you need to take course b first */
            graph.computeIfAbsent(edge[1], v -> new LinkedList<>())
                .add(edge[0]);
        }

        /* total courses are 0, 1, ... numCourses - 1 */
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

    public boolean containsCycleDFS(Integer courseID,
                                    Map<Integer, List<Integer>> graph,
                                    boolean[] dfsStack,
                                    boolean[] visited) {
        if (dfsStack[courseID]) return true;
        dfsStack[courseID] = true;

        if (visited[courseID]) return false;
        visited[courseID] = true;

        List<Integer> dependentCourses = graph.getOrDefault(courseID, new LinkedList<>());
        for (Integer dependentCID: dependentCourses) {
            if (containsCycleDFS(dependentCID, graph, visited, dfsStack)) {
                return true;
            }
        }
        dfsStack[courseID] = false;
        return false;
    }
}
