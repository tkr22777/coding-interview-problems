import java.io.*;
import java.util.*;
import java.util.stream.*;

class Solution {

  public static void main(String[] args) {
    int[][] array = {{1,3,1},
                     {1,5,1},
                     {4,2,1}};
    System.out.println( new Solution().minPathSum(array));
  }

  public int minPathSum(int[][] grid) {

    for(int col = 1; col < grid[0].length; col++) {
       grid[0][col] += grid[0][col - 1];
    }

    for(int row = 1; row < grid.length; row++) {
       grid[row][0] += grid[row - 1][0];
    }

    for(int row = 1; row < grid.length; row++) {
      for(int col = 1; col < grid[0].length; col++) {
        grid[row][col] += Math.min(grid[row][col-1], grid[row-1][col]);
      }
    }
    return grid[grid.length - 1][grid[0].length - 1];
  }
}


