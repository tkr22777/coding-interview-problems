/* https://leetcode.com/problems/number-of-islands/ */

class NumberOfIslands {
    public static void main(String[] args) {
        char[][] grid = { //two islands
            { '1', '0'},
            { '0', '1'}
        };
        System.out.println(new NumberOfIslands().numIslands(grid));

        char[][] grid2 = { //one island
            { '1', '1'},
            { '0', '1'}
        };
        System.out.println(new NumberOfIslands().numIslands(grid2));

        char[][] grid3 = { //three islands
            { '1', '0' , '1'},
            { '0', '1' , '1'},
            { '1', '0' , '0'}
        };
        System.out.println(new NumberOfIslands().numIslands(grid3));

        char[][] grid4 = { //one island
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
        for (int row = 0 ; row < grid.length ; row++) {
            for (int col = 0; col < grid[row].length ; col++) {
                if (visit(grid, visited, row, col) > 0) {
                    totalIslands++;
                }
            }
        }
        return totalIslands;
    }

    private int visit(char[][] grid, short[][] visited, int row, int col) {
        if (row < 0 || row >= grid.length || col < 0 || col >= grid[row].length) {
            return 0;
        }

        if (visited[row][col] == 1) {
            return 0;
        }

        if (grid[row][col] == '1') {
            visited[row][col] = 1; //visited
            int islandArea = 1;
            islandArea += visit(grid, visited, row + 1, col);
            islandArea += visit(grid, visited, row - 1, col);
            islandArea += visit(grid, visited, row, col + 1);
            islandArea += visit(grid, visited, row, col - 1);
            return islandArea;
        }

        return 0;
    }
}

