import java.util.*;

class Solution {

    public int findCircleNum(int[][] M) {

        boolean[] visited = new boolean[M.length];
        Queue < Integer > queue = new LinkedList < Integer > ();
        int circles = 0;

        //we want to visit all node unless it has been visited
        for (int node = 0; node < M.length ; node++) {
            if (!visited[node]) { 
                queue.offer(node);
                while (!queue.isEmpty()) {
                    int nextNode = queue.poll();
                    if (!visited[nextNode]) {
                        visited[nextNode] = true;
                        for (int j = 0; j < M[nextNode].length; j++) {
                            if (M[nextNode][j] == 1 && !visited[j]) {
                                queue.offer(j);
                            }
                        }
                    }
                }
                circles++;
            }
        }
        return circles;
    }
}

