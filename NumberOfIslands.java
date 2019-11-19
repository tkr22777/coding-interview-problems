import java.util.*;

class NumberOfIslands {

    public static void main(String[] args) {

        char[][] grid = {
            { '1', '0'},
            { '0', '1'}
        };
        System.out.println(new NumberOfIslands().numIslands(grid));

        char[][] grid2 = {
            { '1', '1'},
            { '0', '1'}
        };
        System.out.println(new NumberOfIslands().numIslands(grid2));

        char[][] grid3 = {
            { '1', '0' , '1'},
            { '0', '1' , '1'},
            { '1', '0' , '0'}
        };
        System.out.println(new NumberOfIslands().numIslands(grid3));

        char[][] grid4 = {
            { '1', '0' , '1'},
            { '1', '1' , '1'},
            { '1', '0' , '1'}
        };
        System.out.println(new NumberOfIslands().numIslands(grid4));
    }

    public int numIslands(char[][] grid) {

        if (grid == null || grid.length == 0) {
            return 0;
        }

        short[][] visited = new short[grid.length][grid[0].length];

        int totalIslands = 0;
        for (int i = 0 ; i < grid.length ; i++) {
            for (int j = 0; j < grid[0].length ; j++) {
                if (visit(grid, visited, i, j) > 0) {
                    totalIslands++;
                }
            }
        }

        return totalIslands;
    }

    private int visit(char[][] grid, short[][] visited, int i, int j) {

        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length) {
            return 0;
        }

        if (visited[i][j] == 1) {
            return 0;
        }

        if (grid[i][j] == '1') {

            visited[i][j] = 1; //visited

            int islandArea = 1;
            islandArea += visit(grid, visited, i + 1, j);
            islandArea += visit(grid, visited, i - 1, j);
            islandArea += visit(grid, visited, i, j + 1);
            islandArea += visit(grid, visited, i, j - 1);
            return islandArea;

        } else {

            return 0;
        }
    }
}

