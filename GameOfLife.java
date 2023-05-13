/*
    https://leetcode.com/problems/game-of-life/
    TODO: update logic to improve readability
 */
import java.util.*;
class GameOfLife {

    public static void main(String[] args) {
        int[][] board = {
            {0,1,0},
            {0,0,1},
            {1,1,1},
            {0,0,0}
        };

        new GameOfLife().gameOfLife(board);
        for(int[] row: board) {
            System.out.println(Arrays.toString(row));
        }
    }

    public void gameOfLife(int[][] board) {
        for (int row = 0; row < board.length; row++) {
            for (int column = 0; column < board[row].length; column++) {
                int neighbours = countNeighbours(board, row, column);
                board[row][column] = getUpdatedValueForNeighbours(board[row][column], neighbours);
            }
        }
        finalize(board);
    }

    int countNeighbours(int[][] board, int row, int column) {
        int[] shifts = {-1, 0, 1};

        int neighbours = 0;
        for (int x : shifts) {
            for (int y : shifts) {
                if (x == 0 && y == 0) {
                    continue;
                }

                if (row + x < 0 || board.length <= row + x ||
                    column + y < 0 || board[row].length <= column + y) {
                    continue;
                }

                // the following logic confusing and ties to another function, doing multiple things
                neighbours += board[row + x][column + y] % 2;
            }
        }
        return neighbours;
    }

    int getUpdatedValueForNeighbours(int val, int neighbours) {
        if (val % 2 == 1) { /* currently alive */
            if (!(neighbours >= 2 && neighbours < 4))  { /* dies */
                /* odd value flags that the cell was alive at start */
                return 3; 
            }
        } else { /* currently dead */
            if (neighbours == 3) { /* reproduces */
                /* even value flags that the cell was dead at start */
                return 2; 
            }
        }
        return val;
    }

    void finalize(int[][] board) {
        for (int row = 0; row < board.length; row++) {
            for (int column = 0; column < board[row].length; column++) {
                if (board[row][column] == 2) { /* dead to alive */
                    board[row][column] = 1;
                } else if (board[row][column] == 3) { /* alive to dead */
                    board[row][column] = 0;
                }
            }
        }
    }
}

