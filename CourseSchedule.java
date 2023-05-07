/*
    https://leetcode.com/problems/course-schedule/submissions/
    Courses labeled from 0 to numCourses - 1 has to be completed.
    The prerequisites[i] = [ai, bi] implies bi must be taken before ai.
    Return true if you can finish all courses given the params.

    The idea for the solution:
    -> any course can be taken unless there is pre-req
    -> courses can't be finished if there is a cycle among pre-reqs
*/

import java.util.*;

class CourseSchedule {
    public static void main(String[] args) {
        int numCourses = 2;
        int[][] validPreReqs = {
            {1,0},
        };
        assert new CourseSchedule().canFinish(numCourses, validPreReqs);

        int[][] invalidPreReqs = {
            {1,0},
            {0,1}
        };
        assert !new CourseSchedule().canFinish(numCourses, invalidPreReqs);
    }

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, List<Integer>> courseDepGraph = new HashMap<>();
        for (int[] edge: prerequisites) {
            // {a, b} <- to take course "a", you need to take course "b" FIRST
            courseDepGraph.computeIfAbsent(edge[1], v -> new LinkedList<>())
                .add(edge[0]);
        }

        boolean[] dfsStack = new boolean[numCourses];
        boolean[] visited = new boolean[numCourses];
        for (Integer courseID: courseDepGraph.keySet()) {
            /* course schedule would be impossible if there is a cyclic dependency */
            if (cycleInCourseDependency(courseID, courseDepGraph, visited, dfsStack)) {
                return false;
            }
        }
        return true;
    }

    /* course can be finished if there are no cyclic dependency */
    public boolean cycleInCourseDependency(Integer courseID,
                                           Map<Integer, List<Integer>> graph,
                                           boolean[] visited,
                                           boolean[] dfsStack) {
        if (dfsStack[courseID]) {
            return true;
        }

        //visited check is an optimization that beats TLE
        if (visited[courseID]) {
            return false;
        }
        // the visited optimization requires setting the dfsStack after the visited check
        dfsStack[courseID] = true;
        visited[courseID] = true;

        List<Integer> dependentCourses = graph.getOrDefault(courseID, new LinkedList<>());
        for (Integer dependentCID: dependentCourses) {
            if (cycleInCourseDependency(dependentCID, graph, visited, dfsStack)) {
                return true;
            }
        }
        dfsStack[courseID] = false;
        return false;
    }
}
