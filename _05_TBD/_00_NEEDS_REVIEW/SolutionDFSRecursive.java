import java.util.*;
class Solution {

    public int findCircleNum(int[][] M) {

        int circles = 0;
        boolean[] visited = new boolean[M.length];
        for (int i = 0; i < M.length ; i++) {
            if (!visited[i]) {
                visited[i] = true;
                visitDFS(M, visited, i);
                circles++;
            }
        }
        return circles;
    }

    private void visitDFS(int[][] M, boolean[] visited, int node) {

        for (int j = 0; j < M[node].length ; j++) {
            if (M[node][j] == 1 && !visited[j]) {
                visited[j] = true;
                visitDFS(M, visited, j);
            }
        }
    }
}

