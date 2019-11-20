import java.util.*;
class GameOfLife {

    //Problem: https://leetcode.com/problems/game-of-life/

    public static void main(String[] args) {
        int[][] start = {
            {0,1,0},
            {0,0,1},
            {1,1,1},
            {0,0,0}
        };

        new GameOfLife().gameOfLife(start);
        for(int[] a: start) {
            System.out.println(Arrays.toString(a));
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
        for (int i = 0; i < shifts.length; i++) {
            for (int j = 0; j < shifts.length; j++) {

                int x = shifts[i];
                int y = shifts[j];

                if (x == 0 && y == 0) {
                    continue;
                }

                if (row + x < 0 || row + x >= board.length) {
                    continue;
                }

                if (column + y < 0 || column + y >= board[row].length) {
                    continue;
                }

                neighbours += board[row + x][column + y] % 2;
            }
        }
        return neighbours;
    }

    int getUpdatedValueForNeighbours(int val, int neighbours) {

        if (val % 2 == 1) { //If current val is odd
            if (neighbours < 2) {
                return 3;
            } else if (neighbours >= 2 && neighbours < 4)  {
                return 5;
            } else {
                return 3;
            }
        } else { //If current val is even

            if (neighbours == 3) {
                return 4;
            } else {
                return 2;
            }
        }
    }

    void finalize(int[][] board) {
        for (int row = 0; row < board.length; row++) {
            for (int column = 0; column < board[row].length; column++) {
                if (board[row][column] == 3 || board[row][column] == 2) {
                    board[row][column] = 0;
                } else {
                    board[row][column] = 1;
                }
            }
        }
    }
}

